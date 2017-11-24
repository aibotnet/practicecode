from bs4 import BeautifulSoup as BS
import xml.dom.minidom
from lxml import etree
import re
f1=open('/home/aknauhwar/Desktop/compare/gt_merchant_data_.xml' , "r")

f2=open('/home/aknauhwar/Desktop/compare/gt_merchant_data_old.xml' , "r")

f3=open('/home/aknauhwar/Desktop/compare/new_gt_id.txt' , "r")

f4=open('/home/aknauhwar/Desktop/compare/old_gt_id.txt' , "r")

#test=open('/home/aknauhwar/Desktop/compare/test.xml' , "r")

output=open('/home/aknauhwar/Desktop/compare/output.txt' , "w")

notfound=open('/home/aknauhwar/Desktop/compare/notfoundinold.txt' , "w")

new_id=f3.readlines()
old_id=f4.readlines()


l=[]

#count=0

doc1 = etree.parse('/home/aknauhwar/Desktop/compare/gt_merchant_data_.xml')
doc2 = etree.parse('/home/aknauhwar/Desktop/compare/gt_merchant_data_old.xml')


def match(doc1 , doc2 , id2 , output):
    
    id=id2.strip("\n")
    
    
    merchant_name_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/name/text()'%id )
    merchant_website_url_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/website_Url/text()'%id )
    
    merchant_address_street_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/address/street/text()'%id )
    merchant_address_city_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/address/city/text()'%id )
    merchant_address_state_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/address/state/text()'%id )
    merchant_address_country_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/address/country/text()'%id )
    merchant_address_zipcode_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/address/zipcode/text()'%id )
    
    
    merchant_phone_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/phone/text()'%id )
    merchant_email_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/email/text()'%id )
    merchant_cpc_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/cpc/text()'%id )
    merchant_billing_type_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/billing_type/text()'%id )
    merchant_logo_url_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/logo_Url/text()'%id )
    merchant_fax_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/fax/text()'%id )
    
    
    merchant_customer_service_phone_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/customer_service/phone/text()'%id )
    merchant_customer_service_email_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/customer_service/email/text()'%id )
    merchant_customer_service_fax_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/customer_service/fax/text()'%id )
    merchant_customer_service_working_hrs_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/customer_service/working_hrs/text()'%id )
    
    
    merchant_delivery_methods_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/delivery_methods/text()'%id )
    merchant_return_policy_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/return_policy/text()'%id )
    
    
    merchant_import_xml_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/import_xml/text()'%id )
    
    merchant_shipping_rules_active_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/shipping_rules/active/text()'%id )
    merchant_shipping_rules_ruleTag_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/shipping_rules/ruleTag/text()'%id )
    merchant_shipping_rules_input_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/shipping_rules/input/text()'%id )
    merchant_shipping_rules_ruleId_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/shipping_rules/ruleId/text()'%id )
    merchant_shipping_rules_comment_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/shipping_rules/comment/text()'%id )
    
    
    merchant_wire_transfer_string_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/wire_transfer_string/text()'%id )
    
    merchant_payment_preference_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/payment_preference/text()'%id )
    
    
    merchant_wize_commerce_seller_id_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/wize_commerce_seller_id/text()'%id )
    
    merchant_market_id_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/market_id/text()'%id )
    
    merchant_active_status_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/active_status/text()'%id )
    
    
    merchant_billing_address_name_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/billing_address/name/text()'%id )
    merchant_billing_address_name1_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/billing_address/name1/text()'%id )
    merchant_billing_address_name2_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/billing_address/name2/text()'%id )
    merchant_billing_address_address1_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/billing_address/address1/text()'%id )
    merchant_billing_address_address2_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/billing_address/address2/text()'%id )
    merchant_billing_address_city_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/billing_address/city/text()'%id )
    merchant_billing_address_state_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/billing_address/state/text()'%id )
    merchant_billing_address_zipcode_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/billing_address/zipcode/text()'%id )
    merchant_billing_address_country_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/billing_address/country/text()'%id )
    merchant_billing_address_email_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/billing_address/email/text()'%id )
    
    
    
    merchant_pre_or_post_pay_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/pre_or_post_pay/text()'%id )
    merchant_direct_debit_agreement_date_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/direct_debit_agreement_date/text()'%id )
    merchant_vat_new=doc1.xpath('//merchants/merchant[@gt_id=%s]/vat/text()'%id )
    
    
    
    
    
    #####################################################################################################################################
    
    merchant_name_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/name/text()'%id )
    merchant_website_url_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/website_Url/text()'%id )
    
    merchant_address_street_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/address/street/text()'%id )
    merchant_address_city_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/address/city/text()'%id )
    merchant_address_state_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/address/state/text()'%id )
    merchant_address_country_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/address/country/text()'%id )
    merchant_address_zipcode_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/address/zipcode/text()'%id )
    
    
    merchant_phone_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/phone/text()'%id )
    merchant_email_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/email/text()'%id )
    merchant_cpc_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/cpc/text()'%id )
    merchant_billing_type_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/billing_type/text()'%id )
    merchant_logo_url_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/logo_Url/text()'%id )
    merchant_fax_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/fax/text()'%id )
    
    
    merchant_customer_service_phone_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/customer_service/phone/text()'%id )
    merchant_customer_service_email_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/customer_service/email/text()'%id )
    merchant_customer_service_fax_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/customer_service/fax/text()'%id )
    merchant_customer_service_working_hrs_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/customer_service/working_hrs/text()'%id )
    
    
    merchant_delivery_methods_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/delivery_methods/text()'%id )
    merchant_return_policy_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/return_policy/text()'%id )
    
    
    merchant_import_xml_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/import_xml/text()'%id )
    
    merchant_shipping_rules_active_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/shipping_rules/active/text()'%id )
    merchant_shipping_rules_ruleTag_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/shipping_rules/ruleTag/text()'%id )
    merchant_shipping_rules_input_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/shipping_rules/input/text()'%id )
    merchant_shipping_rules_ruleId_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/shipping_rules/ruleId/text()'%id )
    merchant_shipping_rules_comment_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/shipping_rules/comment/text()'%id )
    
    
    merchant_wire_transfer_string_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/wire_transfer_string/text()'%id )
    
    merchant_payment_preference_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/payment_preference/text()'%id )
    
    
    merchant_wize_commerce_seller_id_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/wize_commerce_seller_id/text()'%id )
    
    merchant_market_id_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/market_id/text()'%id )
    
    merchant_active_status_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/active_status/text()'%id )
    
    
    merchant_billing_address_name_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/billing_address/name/text()'%id )
    merchant_billing_address_name1_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/billing_address/name1/text()'%id )
    merchant_billing_address_name2_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/billing_address/name2/text()'%id )
    merchant_billing_address_address1_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/billing_address/address1/text()'%id )
    merchant_billing_address_address2_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/billing_address/address2/text()'%id )
    merchant_billing_address_city_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/billing_address/city/text()'%id )
    merchant_billing_address_state_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/billing_address/state/text()'%id )
    merchant_billing_address_zipcode_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/billing_address/zipcode/text()'%id )
    merchant_billing_address_country_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/billing_address/country/text()'%id )
    merchant_billing_address_email_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/billing_address/email/text()'%id )
    
    
    
    merchant_pre_or_post_pay_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/pre_or_post_pay/text()'%id )
    merchant_direct_debit_agreement_date_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/direct_debit_agreement_date/text()'%id )
    merchant_vat_old=doc2.xpath('//merchants/merchant[@gt_id=%s]/vat/text()'%id )
    
    
    
    
    
    ################################################################################################################################
    if ( merchant_name_new ==[] ) :        
          merchant_name_new.append("")
    if ( merchant_website_url_new ==[] ) :    
              merchant_website_url_new.append("")
    if ( merchant_address_street_new ==[] ) :  
                merchant_address_street_new.append("")
    if ( merchant_address_city_new ==[] ) :    
              merchant_address_city_new.append("")
    if ( merchant_address_state_new ==[] ) :    
              merchant_address_state_new.append("")
    if ( merchant_address_country_new ==[] ) :   
               merchant_address_country_new.append("")
    if ( merchant_address_zipcode_new ==[] ) :    
              merchant_address_zipcode_new.append("")
    if ( merchant_phone_new ==[] ) :      
            merchant_phone_new.append("")
    if ( merchant_email_new ==[] ) :   
               merchant_email_new.append("")
    if ( merchant_cpc_new ==[] ) : 
            
             merchant_cpc_new.append("")
    if ( merchant_billing_type_new ==[] ) :   
               merchant_billing_type_new.append("")
    if ( merchant_logo_url_new ==[] ) :  
                merchant_logo_url_new.append("")
    if ( merchant_fax_new ==[] ) :    
              merchant_fax_new.append("")
    if ( merchant_customer_service_phone_new ==[] ) :  
                merchant_customer_service_phone_new.append("")
    if ( merchant_customer_service_email_new ==[] ) :  
                merchant_customer_service_email_new.append("")
    if ( merchant_customer_service_fax_new ==[] ) :  
                merchant_customer_service_fax_new.append("")
    if ( merchant_customer_service_working_hrs_new ==[] ) :  
                merchant_customer_service_working_hrs_new.append("")
    if ( merchant_delivery_methods_new ==[] ) : 
                 merchant_delivery_methods_new.append("")
    if ( merchant_return_policy_new ==[] ) :  
                merchant_return_policy_new.append("")
    if ( merchant_import_xml_new ==[] ) :  
                merchant_import_xml_new.append("")
    if ( merchant_shipping_rules_active_new ==[] ) : 
                 merchant_shipping_rules_active_new.append("")
    if ( merchant_shipping_rules_ruleTag_new ==[] ) :  
                merchant_shipping_rules_ruleTag_new.append("")
    if ( merchant_shipping_rules_input_new ==[] ) :  
                merchant_shipping_rules_input_new.append("")
    if ( merchant_shipping_rules_ruleId_new ==[] ) :  
                merchant_shipping_rules_ruleId_new.append("")
    if ( merchant_shipping_rules_comment_new ==[] ) :  
                merchant_shipping_rules_comment_new.append("")
    if ( merchant_wire_transfer_string_new ==[] ) :   
               merchant_wire_transfer_string_new.append("")
    if ( merchant_payment_preference_new ==[] ) :  
                merchant_payment_preference_new.append("")
    if ( merchant_wize_commerce_seller_id_new ==[] ) :  
                merchant_wize_commerce_seller_id_new.append("")
    if ( merchant_market_id_new ==[] ) :    
              merchant_market_id_new.append("")
    if ( merchant_active_status_new ==[] ) :   
               merchant_active_status_new.append("")
    if ( merchant_billing_address_name_new ==[] ) :   
               merchant_billing_address_name_new.append("")
    if ( merchant_billing_address_name1_new ==[] ) :  
                merchant_billing_address_name1_new.append("")
    if ( merchant_billing_address_name2_new ==[] ) :  
                merchant_billing_address_name2_new.append("")
    if ( merchant_billing_address_address1_new ==[] ) :   
               merchant_billing_address_address1_new.append("")
    if ( merchant_billing_address_address2_new ==[] ) :   
               merchant_billing_address_address2_new.append("")
    if ( merchant_billing_address_city_new ==[] ) :   
               merchant_billing_address_city_new.append("")
    if ( merchant_billing_address_state_new ==[] ) :   
               merchant_billing_address_state_new.append("")
    if ( merchant_billing_address_zipcode_new ==[] ) :   
               merchant_billing_address_zipcode_new.append("")
    if ( merchant_billing_address_country_new ==[] ) :   
               merchant_billing_address_country_new.append("")
    if ( merchant_billing_address_email_new ==[] ) :   
               merchant_billing_address_email_new.append("")
    if ( merchant_pre_or_post_pay_new ==[] ) :  
                merchant_pre_or_post_pay_new.append("")
    if ( merchant_direct_debit_agreement_date_new ==[] ) :   
               merchant_direct_debit_agreement_date_new.append("")
    if ( merchant_vat_new ==[] ) :      
             merchant_vat_new.append("")

    
    ######################################################################################################################################
    
    if ( merchant_name_old ==[] ) : 
                 merchant_name_old.append("")
    if ( merchant_website_url_old ==[] ) :  
                merchant_website_url_old.append("")
    if ( merchant_address_street_old ==[] ) :
                  merchant_address_street_old.append("")
    if ( merchant_address_city_old ==[] ) :   
               merchant_address_city_old.append("")
    if ( merchant_address_state_old ==[] ) :    
              merchant_address_state_old.append("")
    if ( merchant_address_country_old ==[] ) :  
                merchant_address_country_old.append("")
    if ( merchant_address_zipcode_old ==[] ) :  
                merchant_address_zipcode_old.append("")
    if ( merchant_phone_old ==[] ) :   
               merchant_phone_old.append("")
    if ( merchant_email_old ==[] ) :    
              merchant_email_old.append("")
    if ( merchant_cpc_old ==[] ) : 
                 merchant_cpc_old.append("")
    if ( merchant_billing_type_old ==[] ) : 
                 merchant_billing_type_old.append("")
    if ( merchant_logo_url_old ==[] ) :   
               merchant_logo_url_old.append("")
    if ( merchant_fax_old ==[] ) :    
              merchant_fax_old.append("")
    if ( merchant_customer_service_phone_old ==[] ) :  
                merchant_customer_service_phone_old.append("")
    if ( merchant_customer_service_email_old ==[] ) :  
                merchant_customer_service_email_old.append("")
    if ( merchant_customer_service_fax_old ==[] ) :   
               merchant_customer_service_fax_old.append("")
    if ( merchant_customer_service_working_hrs_old ==[] ) :  
       merchant_customer_service_working_hrs_old.append("")
    if ( merchant_delivery_methods_old ==[] ) :    
              merchant_delivery_methods_old.append("")
    if ( merchant_return_policy_old ==[] ) :   
               merchant_return_policy_old.append("")
    if ( merchant_import_xml_old ==[] ) :    
              merchant_import_xml_old.append("")
    if ( merchant_shipping_rules_active_old ==[] ) : 
                 merchant_shipping_rules_active_old.append("")
    if ( merchant_shipping_rules_ruleTag_old ==[] ) :  
                merchant_shipping_rules_ruleTag_old.append("")
    if ( merchant_shipping_rules_input_old ==[] ) :  
                merchant_shipping_rules_input_old.append("")
    if ( merchant_shipping_rules_ruleId_old ==[] ) :   
               merchant_shipping_rules_ruleId_old.append("")
    if ( merchant_shipping_rules_comment_old ==[] ) :   
               merchant_shipping_rules_comment_old.append("")
    if ( merchant_wire_transfer_string_old ==[] ) :   
               merchant_wire_transfer_string_old.append("")
    if ( merchant_payment_preference_old ==[] ) :       
           merchant_payment_preference_old.append("")
    if ( merchant_wize_commerce_seller_id_old ==[] ) :    
              merchant_wize_commerce_seller_id_old.append("")
    if ( merchant_market_id_old ==[] ) : 
                 merchant_market_id_old.append("")
    if ( merchant_active_status_old ==[] ) :   
               merchant_active_status_old.append("")
    if ( merchant_billing_address_name_old ==[] ) :   
               merchant_billing_address_name_old.append("")
    if ( merchant_billing_address_name1_old ==[] ) :  
                merchant_billing_address_name1_old.append("")
    if ( merchant_billing_address_name2_old ==[] ) :  
                merchant_billing_address_name2_old.append("")
    if ( merchant_billing_address_address1_old ==[] ) :  
                merchant_billing_address_address1_old.append("")
    if ( merchant_billing_address_address2_old ==[] ) : 
                 merchant_billing_address_address2_old.append("")
    if ( merchant_billing_address_city_old ==[] ) :  
                merchant_billing_address_city_old.append("")
    if ( merchant_billing_address_state_old ==[] ) :    
              merchant_billing_address_state_old.append("")
    if ( merchant_billing_address_zipcode_old ==[] ) :   
               merchant_billing_address_zipcode_old.append("")
    if ( merchant_billing_address_country_old ==[] ) :
                  merchant_billing_address_country_old.append("")
    if ( merchant_billing_address_email_old ==[] ) :  
                merchant_billing_address_email_old.append("")
    if ( merchant_pre_or_post_pay_old ==[] ) :   
               merchant_pre_or_post_pay_old.append("")
    if ( merchant_direct_debit_agreement_date_old ==[] ) :    
              merchant_direct_debit_agreement_date_old.append("")
    if ( merchant_vat_old ==[] ) : 
                  merchant_vat_old.append("")
    
    
    ##########################################################################################################################################
        
        
    if ( merchant_name_new      !=       merchant_name_old )  : 
        output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_name"+"|"+merchant_name_new[0]+"|"+merchant_name_old[0]+'\n')
        
        
    if ( merchant_website_url_new      !=       merchant_website_url_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_website_url"+"|"+merchant_website_url_new[0]+"|"+merchant_website_url_old[0]+'\n')
         
         
    if ( merchant_address_street_new      !=       merchant_address_street_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_address_street"+"|"+merchant_address_street_new[0]+"|"+merchant_address_street_old[0]+'\n')
         
         
    if ( merchant_address_city_new      !=       merchant_address_city_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_address_city"+"|"+merchant_address_city_new[0]+"|"+merchant_address_city_old[0]+'\n')
         
         
    if ( merchant_address_state_new      !=       merchant_address_state_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_address_state"+"|"+merchant_address_state_new[0]+"|"+merchant_address_state_old[0]+'\n')
         
         
    if ( merchant_address_country_new      !=       merchant_address_country_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_address_country"+"|"+merchant_address_country_new[0]+"|"+merchant_address_country_old[0]+'\n')
         
         
    if ( merchant_address_zipcode_new      !=       merchant_address_zipcode_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_address_zipcode"+"|"+merchant_address_zipcode_new[0]+"|"+merchant_address_zipcode_old[0]+'\n')
         
         
    if ( merchant_phone_new      !=       merchant_phone_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_phone"+"|"+merchant_phone_new[0]+"|"+merchant_phone_old[0]+'\n')
         
         
    if ( merchant_email_new      !=       merchant_email_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_email"+"|"+merchant_email_new[0]+"|"+merchant_email_old[0]+'\n')
         
         
    if ( merchant_cpc_new      !=       merchant_cpc_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_cpc"+"|"+merchant_cpc_new[0]+"|"+merchant_cpc_old[0]+'\n')
         
         
    if ( merchant_billing_type_new      !=       merchant_billing_type_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_billing_type"+"|"+merchant_billing_type_new[0]+"|"+merchant_billing_type_old[0]+'\n')
         
         
    if ( merchant_logo_url_new      !=       merchant_logo_url_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_logo_url"+"|"+merchant_logo_url_new[0]+"|"+merchant_logo_url_old[0]+'\n')
         
         
    if ( merchant_fax_new      !=       merchant_fax_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_fax"+"|"+merchant_fax_new[0]+"|"+merchant_fax_old[0]+'\n')
         
         
    if ( merchant_customer_service_phone_new      !=       merchant_customer_service_phone_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_customer_service_phone"+"|"+merchant_customer_service_phone_new[0]+"|"+merchant_customer_service_phone_old[0]+'\n')
         
         
    if ( merchant_customer_service_email_new      !=       merchant_customer_service_email_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_customer_service_email"+"|"+merchant_customer_service_email_new[0]+"|"+merchant_customer_service_email_old[0]+'\n')
         
         
    if ( merchant_customer_service_fax_new      !=       merchant_customer_service_fax_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_customer_service_fax"+"|"+merchant_customer_service_fax_new[0]+"|"+merchant_customer_service_fax_old[0]+'\n')
         
         
    if ( merchant_customer_service_working_hrs_new      !=       merchant_customer_service_working_hrs_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_customer_service_working_hrs"+"|"+merchant_customer_service_working_hrs_new[0]+"|"+merchant_customer_service_working_hrs_old[0]+'\n')
         
         
    if ( merchant_delivery_methods_new      !=       merchant_delivery_methods_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_delivery_methods"+"|"+merchant_delivery_methods_new[0]+"|"+merchant_delivery_methods_old[0]+'\n')
         
         
    if ( merchant_return_policy_new      !=       merchant_return_policy_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_return_policy"+"|"+merchant_return_policy_new[0]+"|"+merchant_return_policy_old[0]+'\n')
         
         
    if ( merchant_import_xml_new      !=       merchant_import_xml_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_import_xml"+"|"+merchant_import_xml_new[0]+"|"+merchant_import_xml_old[0]+'\n')
         
         
    if ( merchant_shipping_rules_active_new      !=       merchant_shipping_rules_active_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_shipping_rules_active"+"|"+merchant_shipping_rules_active_new[0]+"|"+merchant_shipping_rules_active_old[0]+'\n')
         
         
    if ( merchant_shipping_rules_ruleTag_new      !=       merchant_shipping_rules_ruleTag_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_shipping_rules_ruleTag"+"|"+merchant_shipping_rules_ruleTag_new[0]+"|"+merchant_shipping_rules_ruleTag_old[0]+'\n')
         
         
    if ( merchant_shipping_rules_input_new      !=       merchant_shipping_rules_input_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_shipping_rules_input"+"|"+merchant_shipping_rules_input_new[0]+"|"+merchant_shipping_rules_input_old[0]+'\n')
         
         
    if ( merchant_shipping_rules_ruleId_new      !=       merchant_shipping_rules_ruleId_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_shipping_rules_ruleId"+"|"+merchant_shipping_rules_ruleId_new[0]+"|"+merchant_shipping_rules_ruleId_old[0]+'\n')
         
         
    if ( merchant_shipping_rules_comment_new      !=       merchant_shipping_rules_comment_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_shipping_rules_comment"+"|"+merchant_shipping_rules_comment_new[0]+"|"+merchant_shipping_rules_comment_old[0]+'\n')
         
         
    if ( merchant_wire_transfer_string_new      !=       merchant_wire_transfer_string_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_wire_transfer_string"+"|"+merchant_wire_transfer_string_new[0]+"|"+merchant_wire_transfer_string_old[0]+'\n')
         
         
    if ( merchant_payment_preference_new      !=       merchant_payment_preference_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_payment_preference"+"|"+merchant_payment_preference_new[0]+"|"+merchant_payment_preference_old[0]+'\n')
         
         
    if ( merchant_wize_commerce_seller_id_new      !=       merchant_wize_commerce_seller_id_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_wize_commerce_seller_id"+"|"+merchant_wize_commerce_seller_id_new[0]+"|"+merchant_wize_commerce_seller_id_old[0]+'\n')
         
         
    if ( merchant_market_id_new      !=       merchant_market_id_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_market_id"+"|"+merchant_market_id_new[0]+"|"+merchant_market_id_old[0]+'\n')
         
         
    if ( merchant_active_status_new      !=       merchant_active_status_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_active_status"+"|"+merchant_active_status_new[0]+"|"+merchant_active_status_old[0]+'\n')
         
         
    if ( merchant_billing_address_name_new      !=       merchant_billing_address_name_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_billing_address_name"+"|"+merchant_billing_address_name_new[0]+"|"+merchant_billing_address_name_old[0]+'\n')
         
         
    if ( merchant_billing_address_name1_new      !=       merchant_billing_address_name1_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_billing_address_name1"+"|"+merchant_billing_address_name1_new[0]+"|"+merchant_billing_address_name1_old[0]+'\n')
         
         
    if ( merchant_billing_address_name2_new      !=       merchant_billing_address_name2_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_billing_address_name2"+"|"+merchant_billing_address_name2_new[0]+"|"+merchant_billing_address_name2_old[0]+'\n')
         
         
    if ( merchant_billing_address_address1_new      !=       merchant_billing_address_address1_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_billing_address_address1"+"|"+merchant_billing_address_address1_new[0]+"|"+merchant_billing_address_address1_old[0]+'\n')
         
         
    if ( merchant_billing_address_address2_new      !=       merchant_billing_address_address2_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_billing_address_address2"+"|"+merchant_billing_address_address2_new[0]+"|"+merchant_billing_address_address2_old[0]+'\n')
         
         
    if ( merchant_billing_address_city_new      !=       merchant_billing_address_city_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_billing_address_city"+"|"+merchant_billing_address_city_new[0]+"|"+merchant_billing_address_city_old[0]+'\n')
         
         
    if ( merchant_billing_address_state_new      !=       merchant_billing_address_state_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_billing_address_state"+"|"+merchant_billing_address_state_new[0]+"|"+merchant_billing_address_state_old[0]+'\n')
         
         
    if ( merchant_billing_address_zipcode_new      !=       merchant_billing_address_zipcode_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_billing_address_zipcode"+"|"+merchant_billing_address_zipcode_new[0]+"|"+merchant_billing_address_zipcode_old[0]+'\n')
         
         
    if ( merchant_billing_address_country_new      !=       merchant_billing_address_country_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_billing_address_country"+"|"+merchant_billing_address_country_new[0]+"|"+merchant_billing_address_country_old[0]+'\n')
         
         
    if ( merchant_billing_address_email_new      !=       merchant_billing_address_email_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_billing_address_email"+"|"+merchant_billing_address_email_new[0]+"|"+merchant_billing_address_email_old[0]+'\n')
         
         
    if ( merchant_pre_or_post_pay_new      !=       merchant_pre_or_post_pay_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_pre_or_post_pay"+"|"+merchant_pre_or_post_pay_new[0]+"|"+merchant_pre_or_post_pay_old[0]+'\n')
         
         
    if ( merchant_direct_debit_agreement_date_new      !=       merchant_direct_debit_agreement_date_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_direct_debit_agreement_date"+"|"+merchant_direct_debit_agreement_date_new[0]+"|"+merchant_direct_debit_agreement_date_old[0]+'\n')
         
         
    if ( merchant_vat_new      !=       merchant_vat_old )  :
         output.write(str(id)+"|"+merchant_wize_commerce_seller_id_new[0]+'|'+"merchant_vat_new"+"|"+merchant_vat_new[0]+"|"+merchant_vat_old[0]+'\n')
         
         
    output.flush()


















def main():
        count=0
        for id in new_id :
            #break
            if id in old_id :
                #print id
              if id not in l :  
                    l.append(id)
                    count=count+1
                    #print count
              
              match(doc1 , doc2 , id , output)      
                    
                
        
            else :
                
                notfound.write(id.strip("\n")+'\n')
                notfound.flush()

        notfound.write(str(count)+'\n')
        notfound.flush()
        f1.close()
        f2.close()
        f3.close()
        f4.close()
        output.close()
        notfound.close()

main()

