# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

from os import listdir, walk
from os.path import isfile, join
import pandas  as pd

import cProfile, pstats, io

def profile(fnc):
    
    """A decorator that uses cProfile to profile a function"""
    
    def inner(*args, **kwargs):
        
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps.print_stats()
        print(s.getvalue())
        return retval

    return inner

@profile
def get_info_file(file): 
    """
    Func que obtiene la informacion del video:
        Dado 0004_F737_9F_1.txt
        Devuelve ['0004', 'F737' , '9F', '1']
    """
    name = file.split(sep = '.')[0]
    return  name.split(sep = '_')


mypath = r"C:\Users\TebaPC\Desktop\F737"
def GetListOnlyFilesInPath(mypath):
    """ Nos devuelve los archivos dentro de un path"""
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    return onlyfiles

def GetSetFilesAndFoldersInPath(mypath): 
    """ Devuelve un set de files y otro de carpetas dentro de un path"""
    filesAndFolders = {f for f in listdir(mypath)}
    files = {f for f in filesAndFolders if isfile(join(mypath, f))}
    folders = filesAndFolders - files
    
    return files, folders

def GeneratorWalk(mypath):
    """" Recuerda, aqui usamos un generador.
    Para ir accediendo a cada nivel, deberemos usar next()
    
    Devuelve una tupla por nivel
     [0] : path
     [1] : folders inside that path
     [2] : files inside that path
    """
    for (dirpath, dirnames, filenames) in walk(mypath):
        yield dirpath, dirnames, filenames

onlyfiles = GetListOnlyFilesInPath(mypath)

info = list(map(get_info_file, onlyfiles))
keys = [''.join(item) for item in info]
subkeys = ['msn' , 'flight', 'camera', 'time']

# un diccionario de diccionarios
item= (dict(zip(subkeys, ls)) for ls in info)
dicc = dict(zip(keys,item))

#done: hacerlo con pandas , creo que se itera mejor
df = pd.DataFrame(info, columns= subkeys) #mucho mas facil ostia!

# todo: probar a capturar las rutas de ambas carpetas, filtar archivos


# concatenar imagenes 