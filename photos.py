import csv, os

def masterPhoto(src, dst):
    parents = open(dst, 'at')
    pwriter = csv.writer(parents)
    with open (src, 'rt') as src:
        reader = csv.DictReader(src)
        for row in reader:
            if row['Parentage'] !=  'Child':
                image = row['MainImageURL'].split('/')[-1]
                item = row['SKU']
                pwriter.writerow((item, image))
    parents.close()
    
def children_photo(src, dst1, options_list):
    children = open(dst1, 'at')
    cwriter = csv.writer(children)
    lookup_options = open(options_list, 'rt')
    lu_reader=list(csv.DictReader(lookup_options))
    with open (src, 'rt') as src:
        reader = csv.DictReader(src)
        #cycle through reader
        for row in reader:
            #get items photo
            image = row['MainImageURL'].split('/')[-1]  
            #get item's parent
            parent= row['ParentSKU']
            if parent:
                #cycle through lu_reader 
                for rows in iter(lu_reader):
                    if row[row['VariationTheme']] == rows['optionsdesc']:
                        optionId = rows['id']
                        item = '-'.join((parent, optionId))
                        print('writing %s:%s'%(item,image))
                        cwriter.writerow((item, image))
                        break                  
    children.close()
    lookup_options.close()

if __name__ == '__main__':
    for i in os.listdir(os.getcwd()):
        print("opening: ",i)
        if i.split('.')[-1] == 'csv':
            masterPhoto(i,'master_list.csv','results/photos.csv')
            children_photo(i,'master_list.csv','results/children_photos.csv','options.csv')
            
                    
            
        
