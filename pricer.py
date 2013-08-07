new_headers=('ParentSKU',"productcode",'price')

import csv, os

def map_it(directory, price_source, new_file ):
    orders=open(price_source, 'rt')
    orders_list = list(csv.DictReader(orders))
    items_accounted_for= []

    with open(new_file, 'at') as new_file:
        writer = csv.DictWriter(new_file, new_headers)
        writer.writeheader()
        for i in os.listdir(directory):
            f = os.path.join(directory, i)
            if os.path.isfile(f):
                if f.split('.')[-1] == 'csv':
                    print('opening file: %s' %(f))
                    with open(f,'rt') as originals:
                        reader = csv.DictReader(originals)
                        for line in reader:
                            for item in iter(orders_list):
                                if line.get('SKU') == item.get('sku'):
                                    if item.get('item-promotion-discount') == '0' and item.get('ship-service-level')=="Standard":
                                        if line.get('SKU') not in items_accounted_for:
                                            items_accounted_for.append(line.get('SKU'))
                                            new_row = {
                                            'ParentSKU':item.get('ParentSKU'),
                                            'productcode':item.get('SKU'),
                                            'price':item.get('price')}
                                            writer.writerow(new_row)
                                            print(new_row)
    print(items_accounted_for)
    orders.close()
                                
if __name__ == '__main__':
    map_it('../input/originals', '../input/from site/orders.csv','../output/prices.csv')
                        
                    
                
        


