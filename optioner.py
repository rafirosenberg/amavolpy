#!/usr/bin/env python

import os, csv

def make_optionIds(src, start, results):
    options = []
    parents_w_options = []
    oid = start
    options_list = open(os.path.join(results,'options.csv'), 'at')
    writer1 = csv.DictWriter(options_list,('optionsdesc','id','optioncatid'))
    writer1.writeheader()
    options_ids_list = open(os.path.join(results,'masters_options.csv'), 'at')
    writer2 = csv.DictWriter(options_ids_list,('productcode', 'optionsid'))
    writer2.writeheader()

    with open(src, 'rt') as source:
        reader = list(csv.DictReader(source))
        for line in iter(reader):
            #get all option descriptions
            if line.get('Parentage') == 'Child':
                optDesc = line.get(line.get('VariationTheme'))
                options.append({'optionsdesc':optDesc, 'id':oid,'optioncatid':line['VariationTheme'] })
                oid+=1
        for line in iter(reader):
            if line.get('Parentage') == 'Parent':
                alloptions = []
                alloptionsids = []
                for i in iter(reader):
                    if i['ParentSKU'] == line['SKU']:
                        option_id=i[line['VariationTheme']]
                        alloptions.append(option_id)                
                for o in alloptions:     
                    for i in options:
                        if o == i['optionsdesc']:
                            a = i['id']
                            alloptionsids.append(str(a))
                            break
                parents_w_options.append({'productcode':line['SKU'],'optionsid':', '.join(alloptionsids)})

    writer2.writerows(parents_w_options)
    writer1.writerows(options)
    print(len(options), len(parents_w_options))
    options_list.close()
    options_ids_list.close()
    return oid
if __name__ == '__main__':
    start=1
    for i in os.listdir(os.getcwd()):
        if os.path.isfile(i):
            if i.split('.')[-1] == 'csv':
                print(start,'opening file: %s' %(i))
                a = make_optionIds(i,start,wherever)
                start = a
                
