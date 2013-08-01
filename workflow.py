#!/usr/bin/env python
w
import photos, photos_children, mapper, optioner, child_photos_renamer
import shutil, os, csv


def just_do_it():
    print('starting mapper.py')
    mapper.map_it(os.getcwd(), 'results/master_list.csv')
    print('starting optioner.py')
    start=1
    for i in os.listdir(os.getcwd()):
        if os.path.isfile(i):
            if i.split('.')[-1] == 'csv':
                print(start,'opening file: %s' %(i))
                a = optioner.make_optionIds(i,start)
                start = a
    print('starting main photos')
    for i in os.listdir(os.getcwd()):
        if i.split('.')[-1] == 'csv':
            photos.masterPhoto(i, 'results/photos.csv')
    print('starting children photos')
    for i in os.listdir(os.getcwd()):
        if i.split('.')[-1] == 'csv':
            photos.children_photo(i, 'results/photos_children.csv','results/options.csv')
    
if __name__ == '__main__':
    just_do_it()
