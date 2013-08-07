import csv
import os


def createPriceList(orders, prices):
    items = []
    csv_in = csv.DictReader(open(orders, 'rt'))
    csv_out = csv.DictWriter(open(prices, 'w'), ('sku','realprice','shipping','originalprice','quantity-purchased', 'order-id'),delimiter=',')
    csv_out.writeheader()
    for line in csv_in:
        if line.get('sku') not in items:
            if line.get('ship-service-level') == 'Standard' and line.get('item-promotion-discount') == '0' and line.get('shipping-price') != '0':
                items.append(line.get('sku'))
                newrow = {'sku':line.get('sku'),
                          'originalprice':line.get('item-price'),
                          'shipping':line.get('shipping-price'),
                          'quantity-purchased':line.get('quantity-purchased'),
                          'order-id':line.get('order-id'),
                          'realprice':str((float(line.get('item-price'))+float(line.get('shipping-price')))/int(line.get('quantity-purchased')))}
                csv_out.writerow(newrow)
    return(csv_out)
    

def createPrices(directory, orders, prices):
    for i in os.listdir(directory):
        f = os.path.join(directory, i)
        if os.path.isfile(f):
            if f.split('.')[-1] == 'csv':
                print('opening file: %s' %(f))
                items = open(f, 'rt')
                items = list(csv.DictReader(items))
                orders = open(orders, 'rt')
                #order = list(csv.DictReader(orders))
                #with open(prices, 'at') as prices:
                    #prices_list = csv.DictWriter()
                for o in iter(orders):


                    newrow = {'productcode':line.get('sku'),
                          'productprice':line.get('realprice'),
                          'hideproduct':'N',
                          'quantity-purchased':line.get('quantity-purchased'),
                          'order-id':line.get('order-id'),
                          'realprice':str((float(line.get('item-price'))+float(line.get('shipping-price')))/int(line.get('quantity-purchased')))}
                
                    print(o)
 
        
if __name__ == '__main__':
    #createPriceList('../input/from site/orders.csv', '../output/prices_from_orders.csv')
    createPrices('../input/from site/orders.csv',
                 createPriceList('../input/from site/orders.csv', '../output/prices_from_orders.csv'),
                 '../output/prices.csv')
                 

