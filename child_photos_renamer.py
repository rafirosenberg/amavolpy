import os, csv, shutil


def rename(dire):
    files = [f for f in os.listdir(dire) if os.path.isfile(f) if not f.startswith('.')]
    for f in files:
        if '-' in f:
            first, last = f.rsplit('-',1)   
            if last == '0.jpg':
                os.remove(f)
                print('removed %s' %(f))
            elif last == '1.jpg':
                newname = '.'.join((first+'-S','jpg'))
                os.rename(f, newname) 
                print('changed %s to %s' % (f, newname))  
            elif last == '2T.jpg':
                newname = '.'.join((first+'-T','jpg'))
                os.rename(f, newname) 
                print('changed %s to %s' % (f, newname))  
            elif last == '2.jpg':
                newname = '.'.join((first,'jpg'))
                os.rename(f, newname) 
                print('changed %s to %s' % (f, newname))  
             
if __name__ == '__main__':
    rename(os.getcwd())

