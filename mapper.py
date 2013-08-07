new_headers=("productcode",'productweight',  "productname", 'productdescription','ischildofproductcode','hideproduct',
             "enableoptions_inventorycontrol","productprice", "listprice", "saleprice",   
             "productdescriptionshort", "productdescription", "productfeatures", "techspecs",
             "homepage_section", "autodropship", 
             "upc_code", "productkeywords", "productnameshort", "productweight", "freeshippingitem", 
              "selectedoptionids",  "photo_alttext", "hide_yousave", "productcondition", "productmanufacturer",
             "enablemultichildaddtocart", "vendor_price","categoryids", "optionids")

import csv, os

def map_it(original_file, new_file):
    
    with open(new_file, 'at') as new_file:
        writer = csv.DictWriter(new_file, new_headers)
        writer.writeheader()        
        with open(original_file,'rt') as info_to_import:
            reader = list(csv.DictReader(info_to_import))
            for line in reader:
                weight = None
                print(line.get('ShippingWeightUnitOfMeasure'))
                if isinstance(line.get('ShippingWeight') ,float):
                    if line.get('ShippingWeightUnitOfMeasure').upper() == 'OZ':
                        weight = round((line.get('ShippingWeight') * .625), 3)
                    else:
                        weight = line.get('ShippingWeight') * 1,
                new_row = {
                    'productcode':line.get('SKU'),
                    'productweight': weight,
                    'productname':line.get('ProductName'),
                    'productnameshort':' '.join(line.get('ProductName').split(' ')[:5]),
                    'productprice':line.get('ItemPrice'),
                    'listprice':line.get('MSRP'),
                    'upc_code':line.get('StandardProductID'),
                    'productkeywords':', '.join((line.get('SearchTerms1'),line.get('SearchTerms2'),line.get('SearchTerms3'),line.get('SearchTerms4'),line.get('SearchTerms5'))),
                    'productdescription':line.get('Description'),
                    'ischildofproductcode':line.get('ParentSKU'),
                    'hideproduct': 'Y' if line.get('ParentSKU') else 'N',
                    'photo_alttext':' '.join(line.get('ProductName').split(' ')[:5]),
                    'techspecs':''.join('<li>%s</li>' % item for item in ((line.get('BulletPoint1'),line['BulletPoint2'],line['BulletPoint3'],line['BulletPoint4'],line['BulletPoint5']))),
                    'enableoptions_inventorycontrol': 'Y' if line.get('Parentage') == "Parent" else "",
                    'categoryids'
                    :original_file}
                writer.writerow(new_row)
                print(new_row['productcode'])
                    
                                    
if __name__=="__main__":
    directory = '../input/new_originals'
    for f in os.listdir(directory):
            ff = os.path.join(directory, f)
            if os.path.isfile(ff):
                if f.split('.')[-1] == 'csv':
                    map_it(ff, '../output/weights.csv')
                    
                    
                
        


