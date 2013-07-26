import csv, os

def masterPhoto(src, dst1, options_list):
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
                    if row[row['VariationTheme'].capitalize()] == rows['optionsdesc']:
                        optionId = rows['id']
                        item = '-'.join((parent, optionId))
                        print('writing %s:%s'%(item,image))
                        cwriter.writerow((item, image))
                        break                  
    children.close()
    lookup_options.close()
    

if __name__ == '__main__':
    for i in os.listdir(os.getcwd()):
        if i.split('.')[-1] == 'csv':
            print("opening: ",i)
            masterPhoto(i,'results/children_photos.csv','results/options.csv')
            
                    
            
        