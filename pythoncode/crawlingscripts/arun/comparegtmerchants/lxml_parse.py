from lxml import etree

doc = etree.parse('/home/aknauhwar/Desktop/compare/test.xml')

#print doc
id="3"
text=doc.xpath('//merchants/merchant[@gt_id="3"]/address/state/text()')

merchant_name=doc.xpath('//merchants/merchant[@gt_id=%s]/name/text()'%id )
merchant_website_url=doc.xpath('//merchants/merchant[@gt_id=%s]/website_Url/text()'%id )

merchant_address_street=doc.xpath('//merchants/merchant[@gt_id=%s]/address/street/text()'%id )
merchant_address_city=doc.xpath('//merchants/merchant[@gt_id=%s]/address/city/text()'%id )
merchant_address_state=doc.xpath('//merchants/merchant[@gt_id=%s]/address/state/text()'%id )
merchant_address_country=doc.xpath('//merchants/merchant[@gt_id=%s]/address/country/text()'%id )
merchant_address_zipcode=doc.xpath('//merchants/merchant[@gt_id=%s]/address/zipcode/text()'%id )


merchant_phone=doc.xpath('//merchants/merchant[@gt_id=%s]/phone/text()'%id )
merchant_email=doc.xpath('//merchants/merchant[@gt_id=%s]/email/text()'%id )
merchant_cpc=doc.xpath('//merchants/merchant[@gt_id=%s]/cpc/text()'%id )
merchant_billing_type=doc.xpath('//merchants/merchant[@gt_id=%s]/billing_type/text()'%id )
merchant_logo_url=doc.xpath('//merchants/merchant[@gt_id=%s]/logo_Url/text()'%id )
merchant_fax=doc.xpath('//merchants/merchant[@gt_id=%s]/fax/text()'%id )


merchant_customer_service_phone=doc.xpath('//merchants/merchant[@gt_id=%s]/customer_service/phone/text()'%id )
merchant_customer_service_email=doc.xpath('//merchants/merchant[@gt_id=%s]/customer_service/email/text()'%id )
merchant_customer_service_fax=doc.xpath('//merchants/merchant[@gt_id=%s]/customer_service/fax/text()'%id )
merchant_customer_service_working_hrs=doc.xpath('//merchants/merchant[@gt_id=%s]/customer_service/working_hrs/text()'%id )


merchant_delivery_methods=doc.xpath('//merchants/merchant[@gt_id=%s]/delivery_methods/text()'%id )
merchant_return_policy=doc.xpath('//merchants/merchant[@gt_id=%s]/return_policy/text()'%id )


merchant_import_xml=doc.xpath('//merchants/merchant[@gt_id=%s]/import_xml/text()'%id )

merchant_shipping_rules_active=doc.xpath('//merchants/merchant[@gt_id=%s]/shipping_rules/active/text()'%id )
merchant_shipping_rules_ruleTag=doc.xpath('//merchants/merchant[@gt_id=%s]/shipping_rules/ruleTag/text()'%id )
merchant_shipping_rules_input=doc.xpath('//merchants/merchant[@gt_id=%s]/shipping_rules/input/text()'%id )
merchant_shipping_rules_ruleId=doc.xpath('//merchants/merchant[@gt_id=%s]/shipping_rules/ruleId/text()'%id )
merchant_shipping_rules_comment=doc.xpath('//merchants/merchant[@gt_id=%s]/shipping_rules/comment/text()'%id )


merchant_wire_transfer_string=doc.xpath('//merchants/merchant[@gt_id=%s]/wire_transfer_string/text()'%id )

merchant_payment_preference=doc.xpath('//merchants/merchant[@gt_id=%s]/payment_preference/text()'%id )


merchant_wize_commerce_seller_id=doc.xpath('//merchants/merchant[@gt_id=%s]/wize_commerce_seller_id/text()'%id )

merchant_market_id=doc.xpath('//merchants/merchant[@gt_id=%s]/market_id/text()'%id )

merchant_active_status=doc.xpath('//merchants/merchant[@gt_id=%s]/active_status/text()'%id )


merchant_billing_address_name=doc.xpath('//merchants/merchant[@gt_id=%s]/billing_address/name/text()'%id )
merchant_billing_address_name1=doc.xpath('//merchants/merchant[@gt_id=%s]/billing_address/name1/text()'%id )
merchant_billing_address_name2=doc.xpath('//merchants/merchant[@gt_id=%s]/billing_address/name2/text()'%id )
merchant_billing_address_address1=doc.xpath('//merchants/merchant[@gt_id=%s]/billing_address/address1/text()'%id )
merchant_billing_address_address2=doc.xpath('//merchants/merchant[@gt_id=%s]/billing_address/address2/text()'%id )
merchant_billing_address_city=doc.xpath('//merchants/merchant[@gt_id=%s]/billing_address/city/text()'%id )
merchant_billing_address_state=doc.xpath('//merchants/merchant[@gt_id=%s]/billing_address/state/text()'%id )
merchant_billing_address_zipcode=doc.xpath('//merchants/merchant[@gt_id=%s]/billing_address/zipcode/text()'%id )
merchant_billing_address_country=doc.xpath('//merchants/merchant[@gt_id=%s]/billing_address/country/text()'%id )
merchant_billing_address_email=doc.xpath('//merchants/merchant[@gt_id=%s]/billing_address/email/text()'%id )



merchant_pre_or_post_pay=doc.xpath('//merchants/merchant[@gt_id=%s]/pre_or_post_pay/text()'%id )
merchant_direct_debit_agreement_date=doc.xpath('//merchants/merchant[@gt_id=%s]/direct_debit_agreement_date/text()'%id )
merchant_vat=doc.xpath('//merchants/merchant[@gt_id=%s]/vat/text()'%id )



print  merchant_name
print  merchant_website_url

print  merchant_address_street
print  merchant_address_city
print  merchant_address_state
print  merchant_address_country
print  merchant_address_zipcode


print  merchant_phone
print  merchant_email
print  merchant_cpc
print  merchant_billing_type
print  merchant_logo_url
print  merchant_fax


print  merchant_customer_service_phone
print  merchant_customer_service_email
print  merchant_customer_service_fax
print  merchant_customer_service_working_hrs


print  merchant_delivery_methods
print  merchant_return_policy


print  merchant_import_xml

print  merchant_shipping_rules_active
print  merchant_shipping_rules_ruleTag
print  merchant_shipping_rules_input
print  merchant_shipping_rules_ruleId
print  merchant_shipping_rules_comment


print  merchant_wire_transfer_string

print  merchant_payment_preference


print  merchant_wize_commerce_seller_id

print  merchant_market_id

print  merchant_active_status


print  merchant_billing_address_name
print  merchant_billing_address_name1
print  merchant_billing_address_name2
print  merchant_billing_address_address1
print  merchant_billing_address_address2
print  merchant_billing_address_city
print  merchant_billing_address_state
print  merchant_billing_address_zipcode
print  merchant_billing_address_country
print  merchant_billing_address_email



print  merchant_pre_or_post_pay
print  merchant_direct_debit_agreement_date
a=[]
b=[]

if a ==[]:
    
    print "yes they are equal"

    a.append("")
    print a[0]
print  merchant_vat












