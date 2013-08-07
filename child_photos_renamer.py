import os, csv


def rename(dire):
    for f in os.listdir(dire):
        ff=os.path.join('../output/options',f)
        if os.path.isfile(ff):
            if not f.startswith('.'):
                print(f)
                if '-' in f:
                    first, last = f.rsplit('-',1)   
                    if last == '0.jpg':
                        os.remove(ff)
                        print('removed %s' %(f))
                    elif last == '1.jpg':
                        newname = '.'.join((first+'-S','jpg'))
                        os.rename(ff, os.path.join('../output/options',newname)) 
                        print('changed %s to %s' % (ff, newname))  
                    elif last == '2T.jpg':
                        newname = '.'.join((first+'-T','jpg'))
                        os.rename(ff, os.path.join('../output/options',newname))
                        print('changed %s to %s' % (ff, newname))  
                    elif last == '2.jpg':
                        newname = '.'.join((first,'jpg'))
                        os.rename(ff, os.path.join('../output/options',newname))
                        print('changed %s to %s' % (ff, newname))  
             
if __name__ == '__main__':
    rename('../output/options')

