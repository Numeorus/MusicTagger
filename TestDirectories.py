import taglib
from os import listdir
from os.path import isfile, join
from Tkinter import *
from tkFileDialog import askdirectory

print "Test_programm"


Tk().withdraw() 
mypath = askdirectory() 

#onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print(onlyfiles)


bouton=Button(fenetre, text="Fermer", command=fenetre.quit)
bouton.pack()

## Github pytaglib
# https://github.com/supermihi/pytaglib

## Tkinter pour l'interface graphique
# http://apprendre-python.com/page-tkinter-interface-graphique-python-tutoriel
# https://www.slideshare.net/r1chardj0n3s/tkinter-does-not-suck


## Voir pour modifier le filename du fichier
## apres les modifs dues au tags