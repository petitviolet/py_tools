# -*- encoding:utf-8 -*-
import pickle
import os


def load_pickle(fname):
    ''' load pickled object from file(fname)
    Args:
        fname: file name which contains pickled object you want to load
    Return:
        file_content: if fname exists, load and return pickled object
                      otherwise, return None
    '''
    if not os.path.exists(fname):
        print('{0} not found.'.format(fname))
        return None
    with open(fname, 'rb') as f:
        content = pickle.load(f)
    return content


def dump_pickle(fname, obj, overwrite=True):
    ''' save pickled object(obj) into file(fname)
    Args:
        fname: file name you want to save object
        obj: any object can be pickled you want to save
        overwrite: if file whose file name is fname exists,
                    False(confirm overwrite) or True(anyway overwrite)
    Return:
        Bool: Success or not pickle obj into fname
    '''
    if os.path.exists(fname) and not overwrite:
        confirm = input('Overwrite?(y or n) => ')
        if confirm == 'y':
            pass
        else:
            return False
    with open(fname, 'wb') as f:
        pickle.dump(obj, f)
    return True
