#!/usr/bin/env python

import os, csv
def create_kitSrc(new_file, kitSrc, kit_linkSrc, optionsSrc):
    list_new_file = open(new_file, 'wt')
    writer = csv.DictWriter(list_new_file,('currentSKU', 'option desc', 'ParentSKU'))
    writer.writeheader()
    kit = open(kitSrc, 'rt')
    kitList = list(csv.DictReader(kit))
    kit_link = open(kit_linkSrc, 'rt')
    kit_linkList = list(csv.DictReader(kit_link))
    options = open(optionsSrc, 'rt')
    optionsList = list(csv.DictReader(options))
    for item in  iter(kitList):
        for link in iter(kit_linkList):
            if item.get('kit_id') == link.get('kit_id'):
                for option in iter(optionsList):
                    if option.get('id') == link.get('kitlnk_optionid'):
                        writer.writerow({'currentSKU':item.get('kit_isproductcode'),
                                        'option desc':option.get('optionsdesc'),
                                        'ParentSKU':item.get('kit_productcode')})
                        break
                break
    kit.close()
    kit_link.close()
    options.close()
    return new_file
    
    
def make_shadows(new_file, skuSrc, kitSrc, companyid):
    shadows = open(new_file, 'at')
    writer = csv.DictWriter(shadows,('ParentSKU','ShadowSKU','CompanyID'))
    writer.writeheader()
    sku = open(skuSrc, 'rt')
    skuList = list(csv.DictReader(sku))
    kit = open(kitSrc, 'rt')
    kitList = list(csv.DictReader(kit))
    a=1
    for kiti in iter(kitList):
        for skui in iter(skuList):
            if skui.get(skui.get('VariationTheme')) == kiti.get('option desc') and  skui.get('ParentSKU') == kiti.get('ParentSKU'):
                a+=1
                d=writer.writerow({'ParentSKU':skui.get('SKU'),
                                  'ShadowSKU':kiti.get('currentSKU'),
                                  'CompanyID':companyid,
                                  })
                break
            elif skui.get(skui.get('VariationTheme').capitalize()) == kiti.get('option desc') and skui.get('ParentSKU') == kiti.get('ParentSKU'):
                a+=1
                d=writer.writerow({'ParentSKU':skui.get('SKU'),
                                  'ShadowSKU':kiti.get('currentSKU'),
                                  'CompanyID':companyid,})
                break   
        
    sku.close()
    kit.close()
    shadows.close()
    print(a)
if __name__ == '__main__':
    print('here we go')
    for f in os.listdir('../originals'):
        ff = os.path.join('../originals', f)
        if os.path.isfile(ff):
            if f.split('.')[-1] == 'csv':
                print('opening file: %s' %(f))
                make_shadows('../shadows.csv', ff , create_kitSrc('../kits/current_options.csv','../kits/kits.csv','../kits/kitlinks.csv','../kits/options.csv'),'486')
                


