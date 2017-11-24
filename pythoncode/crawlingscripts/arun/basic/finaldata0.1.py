from contextlib import nested
from decorator import decorator
import os.path
import string
from urlparse import urljoin
from xml.dom.minidom import Document

from paste import httpexceptions
from paste.deploy.converters import asbool
from pylons import tmpl_context as c, config, request, response, url

from veetwo.lib import affiliates, constants, emailnotification, helpers as h, product_lib, snippets as snippets_lib, topics
from veetwo.lib.base import BaseController, releasing
from veetwo.lib.cache import cache_response
from veetwo.models.navigation import NAVIGATION_CATEGORY_ROOT_ID
from veetwo.lib.search import solr as solr_search
from veetwo.lib.utils.xml import append_new_element
from veetwo.models import db, betawize,betasite #for api machine for other m/c change to wize and site n do corresponding changes

from xml.dom import minidom
import time
import sys
#from apifunctionchanged.py import *

assert len(sys.argv) > 1, "Pass directory name as a parameter"
file_path= sys.argv[1]

'''def start_output(status=STATUS_OK, output):
    doc =  output 
    response_node = append_new_element(doc, 'response')
    response_node.setAttribute('status', status)
    return doc, response_node    ''' 
    
    
    

def _0_1_get_product_reviews(output , product_id):
        MAX_NUMBER_OF_SEARCH_RESULTS = 100
        DEFAULT_NUMBER_OF_SEARCH_RESULTS = 10
        NUMBER_OF_FILTERS = 5

        '''product_id = request.GET.get('product_id')
        nextag_ptitle_id = request.GET.get('nextag_ptitle_id')
        topic_id = request.GET.get('topic_id')
        rating = request.GET.get('rating')
        sort_order = request.GET.get('sort') '''
        limit = h.get_int_or_none(request.GET.get('limit', DEFAULT_NUMBER_OF_SEARCH_RESULTS))
        beta_id_shift = 50000000
        log.info('Entered into the review function')
        if product_id:
            product_id = h.get_int_or_none(product_id)
        elif nextag_ptitle_id:
            nextag_ptitle_id = h.get_int_or_none(nextag_ptitle_id)
        else:
            raise ServiceException(ERROR_MISSING_PRODUCT_ID)
        if topic_id:
            topic_id = h.get_int_or_none(topic_id)
            if topic_id > beta_id_shift:
                topic_id = topic_id - beta_id_shift 
        if rating:
            rating = h.get_int_or_none(rating)

        if not limit or limit <= 0 or limit > MAX_NUMBER_OF_SEARCH_RESULTS:
            raise ServiceException(ERROR_INVALID_SEARCH_RESULT_LIMIT % MAX_NUMBER_OF_SEARCH_RESULTS)

        is_beta_product = False
        
        if product_id:
            if product_id < beta_id_shift:
                product = product_lib.get_product_by_id(product_id, dbschema=db.betawize)
            else:
                product = product_lib.get_product_by_id(product_id - beta_id_shift, dbschema = db.betawize)
                is_beta_product = True
        elif nextag_ptitle_id:
            product = product_lib.get_product_by_nextag_ptitle_id(nextag_ptitle_id)
            if not product:
                product = product_lib.get_product_by_nextag_ptitle_id(nextag_ptitle_id, dbschema = db.betawize)
                is_beta_product = True
        else:
            raise ServiceException(ERROR_INVALID_PRODUCT_ID)
        if not product:
            raise ServiceException(ERROR_NO_RESULTS)
#        log.info('code is running for product ID %s',product.id)
        dbschema = None
        id_shift = 0
        if is_beta_product:
#            log.info('Running for beta products')
            dbschema = db.betawize
            navigation = dbschema.query(Navigation).get(product.category_id)
#            product_content = None
            id_shift = beta_id_shift
        else:
            navigation = c.navigation_hierarchy.get_navigation_by_category_id(product.category_id)
        product_content = product_lib.get_product_content(product.id)
        
        try:
            display_rvw_count = product_lib.get_product_displayable_review(product.id,config.get('wize.undisplayable_source_ids', '0').split(','),dbschema)
        except:
            display_rvw_count = 0 

        product.pro_count, product.con_count = product_lib.get_product_recommendation_count(product.id, dbschema)
        star_ratings = product_lib.get_star_ratings_by_product(product.id, dbschema)
        pro_filters, con_filters, topic_filters, neutral_topic_filters = topics.get_product_review_filters(product.id,dbschema = dbschema,limit=NUMBER_OF_FILTERS)
        for filter in pro_filters + topic_filters:
            filter.pro_count, filter.con_count = topics.get_product_recommendation_count(product.id, filter.id,dbschema = dbschema)
        if topic_id:
            snippet_list, snippet_count = snippets_lib.get_snippets_by_topic(product.id, product.category_id, topic_id, limit, None,dbschema = dbschema)
        elif rating:
            snippet_list, snippet_count = snippets_lib.get_snippets_by_star_rating(product.id, rating, limit, None)
        else:
            snippet_list = snippets_lib.get_snippets_for_product(product.id, product.category_id, max(DEFAULT_NUMBER_OF_SEARCH_RESULTS, 2 * limit), use_solr=False, dbschema=dbschema)[:limit]

        #doc, response_node = start_output()
        doc =  output 
        response_node = append_new_element(doc, 'response')
        response_node.setAttribute('status', status)
        #return doc, response_node

        product_node = append_new_element(response_node, 'product')
        product_node.setAttribute('id', unicode(product.id + id_shift))
        product_node.setAttribute('name', product.name)
        if product.nextag_product_id:
            product_node.setAttribute('nextag_product_id', unicode(product.nextag_product_id))
        if product.nextag_ptitle_id:
            product_node.setAttribute('nextag_ptitle_id', unicode(product.nextag_ptitle_id))
        product_node.setAttribute('overall_rating', unicode(product.get_wizerank_out_of_five()))
        product_node.setAttribute('recommended_count', unicode(product.pro_count))
        if product.release_date:
            product_node.setAttribute('release_date', product.release_date.strftime('%Y-%m-%d'))
        if product.stats:
            product_node.setAttribute('review_count', unicode(product.stats.review_count))
            product_node.setAttribute('sources_count', unicode(product.stats.site_count))
            if int(display_rvw_count)>0:
                product_node.setAttribute('displayable_review_count',unicode(display_rvw_count))
            
        product_node.setAttribute('url', url('product', product=product))
        product_node.setAttribute('wizerank', unicode(product.get_wizerank()))
        if product_content:
            
            content_node = append_new_element(product_node, 'content')
            if product_content['bottom_line']:
            content_bottom_line_node = append_new_element(content_node, 'bottom_line')
            content_bottom_line_node.appendChild(doc.createCDATASection(h.balance_tags(product_content['bottom_line'])))
            for bullet in product_content['bullets']:
                content_bullet_node = append_new_element(content_node, 'bullet')
                content_bullet_node.appendChild(doc.createCDATASection(bullet))
            content_body_node = append_new_element(content_node, 'body')
            content_body_node.appendChild(doc.createCDATASection(product_content['body']))

        if star_ratings:
            MAX_STARS = 5
            rating_list_node = append_new_element(product_node, 'rating_list')
            for index, review_count in enumerate(reversed(star_ratings)):
                rating_node = append_new_element(rating_list_node, 'rating')
                rating_node.setAttribute('rating', unicode(MAX_STARS - index))
                rating_node.setAttribute('review_count', unicode(review_count))

        displayable_source_average_ratings = [s for s in product.source_average_ratings if s.source_id not in config.get('wize.undisplayable_source_ids', '0').split(',')]
        if displayable_source_average_ratings:
            source_list_node = append_new_element(product_node, 'source_list')
            for source in displayable_source_average_ratings:
                source_node = append_new_element(source_list_node, 'source')
                source_node.setAttribute('id', unicode(source.id + id_shift))
                source_node.setAttribute('name', source.name)
                source_node.setAttribute('average_rating', unicode(source.average_rating))
                source_node.setAttribute('review_count', unicode(source.review_count))
                if source.image_url:
                    source_node.setAttribute('image_url', 'http://d14a29lqfzq7m7.cloudfront.net' + source.image_url)

        if topic_filters:
            topic_list_node = append_new_element(product_node, 'topic_list')
            for topic_filter in topic_filters:
                topic_filter_node = append_new_element(topic_list_node, 'topic')
                topic_filter_node.setAttribute('id', unicode(topic_filter.id))
                topic_filter_node.setAttribute('name', topic_filter.name)
                topic_filter_node.setAttribute('score', unicode(topic_filter.score))
                topic_filter_node.setAttribute('product_url', urljoin(c.widget_site, url('product', product=product, anchor='t=%d' % topic_filter.id)))
                topic_filter_node.setAttribute('recommended_count', unicode(topic_filter.pro_count))
                topic_filter_node.setAttribute('topic_url', urljoin(c.widget_site, url('topic', topic=topic_filter, navigation=navigation)))

        if pro_filters:
            pro_list_node = append_new_element(product_node, 'pro_list')
            for pro_filter in pro_filters:
                pro_filter_node = append_new_element(pro_list_node, 'pro')
                pro_filter_node.setAttribute('id', unicode(pro_filter.id))
                pro_filter_node.setAttribute('name', pro_filter.name)
                pro_filter_node.setAttribute('score', unicode(pro_filter.score))
                pro_filter_node.setAttribute('product_url', urljoin(c.widget_site, url('product', product=product, anchor='t=%d' % pro_filter.id)))
                pro_filter_node.setAttribute('recommended_count', unicode(pro_filter.pro_count))
                pro_filter_node.setAttribute('topic_url', urljoin(c.widget_site, url('topic', topic=pro_filter, navigation=navigation)))

        if snippet_list:
            review_list_node = append_new_element(product_node, 'review_list')
            for snippet in snippet_list:
                review_node = append_new_element(review_list_node, 'review')
                if snippet.author:
                    review_node.setAttribute('author', snippet.author)
                review_node.setAttribute('id', unicode(snippet.review_id + id_shift))
                review_node.setAttribute('published', unicode(snippet.pub_date)[:10])
                review_node.setAttribute('rating', unicode(snippet.normalized_rating))
                review_node.setAttribute('source_id', unicode(snippet.source_id + id_shift))
                review_node.setAttribute('url', snippet.review_url)
                if snippet.title:
                    text_node = append_new_element(review_node, 'title')
                    text_node.appendChild(doc.createCDATASection(h.balance_tags(snippet.title)))
                text_node = append_new_element(review_node, 'text')
                text_node.appendChild(doc.createCDATASection(h.balance_tags(snippet.review_text)))
                if snippet.before:
                    before_node = append_new_element(review_node, 'before')
                    before_node.appendChild(doc.createCDATASection(h.balance_tags(snippet.before)))
                snippet_node = append_new_element(review_node, 'snippet')
                snippet_node.appendChild(doc.createCDATASection(h.balance_tags(snippet.text)))
                if snippet.after:
                    after_node = append_new_element(review_node, 'after')
                    after_node.appendChild(doc.createCDATASection(h.balance_tags(snippet.after)))

        #return doc.toxml()
        a=doc.toxml()
        output.write(a)








def start_Operations():
    betawize.init("mysql://root@127.0.0.1:3306/betawize?charset=utf8")   #wize2 change dns too
    betasite.init("mysql://root@127.0.0.1:3306/betasite?charset=utf8")#site
    print "Connection set-up with DB"
    
    inputfile =open(file_path , 'r')
    t=time.time() 
    
    output = open('/home/pylons/production/veetwo/xml/xml.%s.xml'%t , "a")
    i=0


    with nested(betawize.Session(autoflush=False, autocommit=False),betasite.Session(autoflush=False, autocommit=False)):
	#Now start running the loop for 10K products each
	
	
                    
            for line  in inputfile :
                
                if(!line) :
                    output.close() 
                    break
                    
                if(i<10000) :
                    
                    _0_1_get_product_reviews(output , line)
                    i++
                else :
                    
                    output.close()
                    t=time.time()
                    output = open('/home/pylons/production/veetwo/xml/xml.%s.xml'%t , "w")
                    _0_1_get_product_reviews(output , line)
                    i=1
                    
                    
            inputfile.close()
            
            
start_Operations() 
            
            
	
	
	
	
	
	
	
	