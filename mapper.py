new_headers=("productcode", "vendor_partno", "productname", "displaybegindate", "displayenddate", "hideproduct", "stockstatus", "lastmodified", "options_cloned_from", "photos_cloned_from", "share_stockstatus_with", "ischildofproductcode", "ischildofproductcode_productid", "options_cloned_from_productid", "photos_cloned_from_productid", "share_stockstatus_with_productid", "homepage_section", "autodropship", "donotallowbackorders", "upc_code", "productkeywords", "productnameshort", "productweight", "freeshippingitem", "allowpriceedit", "productprice", "listprice", "saleprice", "selectedoptionids", "metatag_title", "metatag_description", "photo_subtext", "photo_alttext", "fixed_shippingcost", "fixed_shippingcost_outside_localregion", "uses_product_keytypes", "price_subtext", "price_subtext_short", "listprice_name", "productprice_name", "saleprice_name", "hide_yousave", "productcondition", "productmanufacturer", "hide_when_outofstock", "enablemultichildaddtocart", "vendor_price", "enableoptions_inventorycontrol", "photourl_small", "photourl_large", "productdescriptionshort", "productdescription", "productfeatures", "techspecs", "extinfo", "orderfinished_note", "metatag_keywords", "productdescription_abovepricing", "custom_metatags_override", "categoryids", "optionids")

import csv, os

def combine_all_files(directory, new_file):
    with open(new_file, 'at') as new_file:
        writer = csv.DictWriter(new_file, new_headers)
        writer.writeheader()
        for i in os.listdir(directory):
            if os.path.isfile(i):
                if i.split('.')[-1] == 'csv':
                    print('opening file: %s' %(i))
                    with open(i,'rt') as info_to_import:
                        reader = csv.DictReader(info_to_import)
                        for line in reader:
                            new_row = {
                                'productcode':line['SKU'],
                                'productname':line['ProductName'],
                                'productnameshort':' '.join(line['ProductName'].split(' ')[:5]),
                                'productprice':line['ItemPrice'],
                                'listprice':line['MSRP'],
                                'upc_code':line['StandardProductID'],
                                'productkeywords':', '.join((line['SearchTerms1'],line['SearchTerms2'],line['SearchTerms3'],line['SearchTerms4'],line['SearchTerms5'])),
                                
                                'ischildofproductcode':line['ParentSKU'],
                                'hideproduct':'Y'if line['Parentage'] == 'Child' else 'N',
                                'photo_alttext':' '.join(line['ProductName'].split(' ')[:5]),
                                'techspecs':''.join('<li>%s</li>' % item for item in ((line['BulletPoint1'],line['BulletPoint2'],line['BulletPoint3'],line['BulletPoint4'],line['BulletPoint5']))),
                                'enableoptions_inventorycontrol':'Y'if line['Parentage'] == 'Parent' else '',}
                            writer.writerow(new_row)
                                
if __name__ == '__main__':
    combine_all_files(os.getcwd(), 'results/cobinedfiles.csv')
                        
                    
                
        


