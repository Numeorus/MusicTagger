import taglib
from os import listdir
from os.path import isfile, join
from Tkinter import Tk
from tkFileDialog import askdirectory

print "Test_programm"


Tk().withdraw() 
mypath = askdirectory() 

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
print(onlyfiles)

## Github pytaglib
# https://github.com/supermihi/pytaglib

## Tkinter pour l'interface graphique
# http://apprendre-python.com/page-tkinter-interface-graphique-python-tutoriel


## Voir pour modifier le filename du fichier
## après les modifs dues au tags