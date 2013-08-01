import csv
import os


def createPriceList(orders, prices):
    items = []
    csv_in = csv.reader(open(orders, 'rb'), delimiter='\t')
    csv_out = csv.writer(open(prices, 'w'), delimiter=',')
    for line in csv_in:
        if line[7] not in items:
            if line[17] == 'Standard':
                items.append(line[7])
                csv_out.writerow(line[],line[],line[])
                print(line[81])
    print(len(items))
    

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
                    print(o)
 
        
if __name__ == '__main__':
    #getprices('../originals', '../11900676233-1.txt', 'prices.csv')
    createPriceList('../11900676233-1.txt', '../output/prices.csv')

