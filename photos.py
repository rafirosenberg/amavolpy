import csv, os

def masterPhoto(src, dst):
    parents = open(dst, 'at')
    pwriter = csv.writer(parents)
    with open (src, 'rt') as src:
        reader = list(csv.DictReader(src))
        for row in reader:
            if row['Parentage'] !=  'Child':
                image = row['MainImageURL'].split('/')[-1]
                item = row['SKU']
                pwriter.writerow((item, image))
    parents.close()
    
def children_photo(src, dst1, options, options_list):
    children = open(dst1, 'at')
    cwriter = csv.writer(children)
    options = open(os.path.join(options,'masters_options.csv'),'rt')
    options_lis = list(csv.DictReader(options))
    lookup_options = open(options_list, 'rt')
    lu_reader=list(csv.DictReader(lookup_options))
    with open (src, 'rt') as src:
        reader = iter(csv.DictReader(src))
        #cycle through reader
        for row in reader:
            #get items photo
            image = row.get('MainImageURL').split('/')[-1]  
            #get item's parent
            parent = row.get('ParentSKU')
            for product in options_lis:
                
                options = product.get('optionsid')
                
                #cycle through lu_reader 
                for rows in iter(lu_reader):
                    if product.get('productcode') == parent:
                        if row.get(row.get('VariationTheme')) == rows.get('optionsdesc') and rows.get('id') in options:
                            optionId = rows['id']
                            item = '-'.join((parent, optionId))
                            print('writing %s:%s'%(item,image))
                            cwriter.writerow((item, image))
                            break                  
    children.close()
    lookup_options.close()

if __name__ == '__main__':
    directory = '../input/new_originals'
    for f in os.listdir(directory):
        ff = os.path.join(directory, f)
        if os.path.isfile(ff):
            masterPhoto(ff,'../output/photos.csv')
            children_photo(ff,'../output/children_photos.csv','../output','../output/options.csv')
            
                    
            
        
