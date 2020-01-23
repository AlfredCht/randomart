from random import *
from tkinter import *


def random_couleur():#creation d'une fonction générant un code couleur aléatoirement
    code_hexa =['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    code_couleur = '#'
    for i in range(0,6):
        code_couleur = code_couleur + choice(code_hexa)
        i+=1
    return code_couleur


fenetre = Tk()

toile = Canvas(fenetre,width=400,height=400,background='white')
toile.grid(row=0,column=0)
for i in range (0,100):
    x1=randint(0,500)
    y1=randint(0,500)
    x2=randint(0,500)
    y2=randint(0,500)
    random_width=randint(1,10)
    toile.create_line(x1,y1,x2,y2,fill = random_couleur(),width =randint(1,5))#dessiner des lignes
    toile.create_arc(x1, y1, x2, y2, start=0,extent=210, outline=random_couleur(), width=randint(1,5));#dessiner des arcs de cercle
    toile.update()
fenetre.mainloop()
