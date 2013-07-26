import os, copy, shutil

def import_all():
    for root, dirs, files in os.walk(os.getcwd()):
        if "all" in dirs:
            dirs.remove('all')
        for f in files:
            if f.split('.')[-1] == 'jpg':
                shutil.copy(os.path.join(root,f), 'all')
            
if __name__ == '__main__':
    import_all()
    