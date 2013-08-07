new_headers=("productcode",'price','ship-price','ParentSKU','order', 'quantity')

import csv, os

def price_list_maker(directory, price_source, new_file ):
    orders=open(price_source, 'rt')
    orders_list = list(csv.DictReader(orders, delimiter='\t'))

    with open(new_file, 'at') as new_file:
        writer = csv.DictWriter(new_file, new_headers)
        writer.writeheader()  
        for i in os.listdir(directory):
            f = os.path.join(directory, i)
            if os.path.isfile(f):
                if f.split('.')[-1] == 'csv':
                    print('opening file: %s' %(f))
                    items =  open(f,'rt')
                    reader = list(csv.DictReader(items))
                    items_accounted_for= [] 
                    a,b,c,d,e =0,0,0,0,0
                    for line in iter(reader):
                        for item in iter(orders_list):
                            if item.get('item-promotion-discount') == '0':
                                a+=1
                                if item.get('ship-service-level')== "Standard":
                                    b+=1
                                    if item.get('ship-country') == 'US':
                                        c+=1
                                        if line.get('SKU') == item.get('sku'):
                                            d+=1
                                            if line.get('SKU') not in items_accounted_for:
                                                e+=1
                                                items_accounted_for.append(line.get('SKU'))
                                                new_row = {
                                                'ParentSKU':line.get('ParentSKU'),
                                                'productcode':line.get('SKU'),
                                                'price':item.get('item-price'),
                                                'ship-price':item.get('shipping-price'),
                                                'order':item.get('order-id'),
                                                'quantity':item.get('quantity-purchased')}
                                                writer.writerow(new_row)
                                                #print(new_row['productcode'])
                                                
    print(len(items_accounted_for),
          a,b,c,d,e)
    orders.close()
                                
if __name__ == '__main__':
    price_list_maker('../input/originals', '../input/from site/11900676233.txt','../output/prices.csv')
                        
                    
                
        


