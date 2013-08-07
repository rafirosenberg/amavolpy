#!/usr/bin/env python

import photos, mapper, optioner, child_photos_renamer
import os, csv


def just_do_it(directory, results_dir):
    print('starting mapper.py')
    for f in os.listdir(directory):
        ff = os.path.join(directory, f)
        if os.path.isfile(ff):
            if f.split('.')[-1] == 'csv':
                mapper.map_it(ff, os.path.join(results_dir, 'products.csv'))
    print('starting optioner.py')
    start=1
    for f in os.listdir(directory):
        ff = os.path.join(directory, f)
        if os.path.isfile(ff):
            if f.split('.')[-1] == 'csv':
                print('opening file: %s' %(f))
                a = optioner.make_optionIds(ff,start,results_dir)
                start = a
    print('starting main photos')
    for f in os.listdir(directory):
        ff = os.path.join(directory, f)
        if os.path.isfile(ff):
            if f.split('.')[-1] == 'csv':
                photos.masterPhoto(ff, os.path.join(results_dir,'photos.csv'))
    print('starting children photos')
    for f in os.listdir(directory):
        ff = os.path.join(directory, f)
        if os.path.isfile(ff):
            if f.split('.')[-1] == 'csv':
                photos.children_photo(ff, os.path.join(results_dir,'photos_children.csv'), os.path.join(results_dir,'options.csv'))
    
if __name__ == '__main__':
    just_do_it('../input/new_originals', '../output')
