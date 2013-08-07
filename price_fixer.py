import csv, os
headers = ["SKU", "ProductName", "Manufacturer", "MfrModelNumber",
           "ProductType", "Parentage", "ItemPrice", "Quantity", "ItemType",
           "Brand", "MainImageURL","ShippingWeight", "ShippingWeightUnitOfMeasure", 
           "SearchTerms1", "SearchTerms2", "SearchTerms3", "SearchTerms4", "SearchTerms5",
           "ParentSKU", "RelationshipType", "VariationTheme", "Color", "StyleName", 
           "BulletPoint1", "BulletPoint2", "BulletPoint3", "BulletPoint4", "BulletPoint5",
           "Description", "TargetAudience1", "TargetAudience2", "TargetAudience3", "Designer",
           "MSRP", "SalesPrice", "PlatinumKeywords1", "PlatinumKeywords2", "PlatinumKeywords3",
           "PlatinumKeywords4", "PlatinumKeywords5"]
def fix_it(item_file,prices, newfile):
    prices = open(prices, 'rt')
    price_list = list(csv.DictReader(prices))
    items = open(item_file, 'rt')
    items_list = list(csv.DictReader(items))
    with open(newfile, 'wt') as write:
        writer = csv.DictWriter(write, headers,extrasaction='ignore')
        writer.writeheader()
        newprice= None
        for line in iter(items_list):
            new = dict(line)
            for price in price_list:
                if price.get('sku') == line.get('SKU'):
                    price = round(float(price.get('realprice')),0)-.01
                    if price < 4.99:
                        price = 4.99
                    
            if line.get('Parentage') == 'Child':
                if 'PL' in line.get('ParentSKU'):
                    new['Parentage']=''
                    new['ParentSKU'] = ''
                    new['ItemPrice'] = price
                elif "Plug" in line.get('ParentSKU'): 
                    if not "Fake" in line.get('ParentSKU'): 
                        new['Parentage']=''
                        new['ParentSKU'] = ''
                        new['ItemPrice'] = price
            writer.writerow(new)
if __name__ == "__main__":
    directory = '../input/originals'
    if not os.path.exists('../input/new_originals'):
        os.makedirs('../input/new_originals')
    newdir = '../input/new_originals'
    print(os.path.abspath(newdir))
    for f in os.listdir(directory):
        ff = os.path.join(directory, f)      
        if os.path.isfile(ff):
            if f.split('.')[-1] == 'csv':
                fix_it(ff,'../output/prices.csv', os.path.join(newdir,f))
    
