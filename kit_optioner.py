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
    list_new_file= open(new_file, 'at')
    writer = csv.DictWriter(list_new_file,('ParentSKU','ShadowSKU','CompanyID','type','var','a',))
    writer.writeheader()
    sku = open(skuSrc, 'rt')
    skuList = list(csv.DictReader(sku))
    kit = open(kitSrc, 'rt')
    kitList = csv.DictReader(kit)
    a=1
    for kiti in kitList:
        print(kiti.get('currentSKU'))
        for skui in iter(skuList):
            if skui.get(skui.get('VariationTheme')) == kiti.get('option desc'):
                if skui.get('ParentSKU') == kiti.get('parentSKU'):
                    a+=1
                    print(skui.get('ParentSKU'), kiti.get('ParentSKU'))
                    print(kiti.get('currentSKU'),skui.get(skui.get('VariationTheme')))
                    d=writer.writerow({'ParentSKU':skui.get('SKU'),
                                      'ShadowSKU':kiti.get('currentSKU'),
                                      'CompanyID':companyid,
                                      'type':skui.get('VariationTheme'),
                                      'var':skui.get(skui.get('VariationTheme')),
                                      'a':True
                                      })
                    break
            elif skui.get(skui.get('VariationTheme').capitalize()) == kiti.get('option desc'):
                if skui.get('ParentSKU') == kiti.get('parentSKU'):
                    a+=1
                    print(skui.get('ParentSKU'), kiti.get('ParentSKU'))
                    print(kiti.get('currentSKU'),skui.get(skui.get('VariationTheme').capitalize()))
                    d=writer.writerow({'ParentSKU':skui.get('SKU'),
                                      'ShadowSKU':kiti.get('currentSKU'),
                                      'CompanyID':companyid,
                                      'var':skui.get(skui.get('VariationTheme').capitalize()),
                                      'type':skui.get('VariationTheme'),
                                      'a':False})
                    break   
            elif skui.get('ParentSKU') == kiti.get('parentSKU'):
                print(skui.get('ParentSKU'), kiti.get('ParentSKU'))
                print(kiti.get('currentSKU'),'oops')
                d=writer.writerow({'ParentSKU':skui.get('SKU'),
                                  'ShadowSKU':kiti.get('currentSKU'),
                                  'CompanyID':companyid,
                                  'var':'oops!',
                                  'type':skui.get('VariationTheme'),
                                  'a':None})  
    sku.close()
    kit.close()
    list_new_file.close()
    print(a)
if __name__ == '__main__':
    print('here we go')
    for i in os.listdir('originals'):
        if os.path.isfile(i):
            if i.split('.')[-1] == 'csv':
                print('opening file: %s' %(i))
                make_shadows('shadows.csv', i , create_kitSrc('kits/current_options.csv','kits/kits.csv','kits/kitlinks.csv','kits/options.csv'),'486')
                


