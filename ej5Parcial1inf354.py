# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 22:52:33 2021

@author: hp
"""




from kanren import run, var, Relation, facts
x = var()
y = var()

padre = Relation()
facts(padre, ("Mario", "Pancho"),
              ("Mario", "Edmundo"),
              ("Mario", "Johnny"),
              ("Mario", "Daniela"),
              ("Pancho",  "Adriana"),
              ("Pancho",  "Alejandra"),
              ("Renato",  "Diego"),
              ("Renato",  "Daniel"),              
              ("Dora", "Pancho"),
              ("Dora", "Edmundo"),
              ("Dora", "Johnny"),
              ("Dora", "Daniela"),
              ("Patricia",  "Adriana"),
              ("Patricia",  "Alejandra"),
              ("Daniela",  "Diego"),
              ("Daniela",  "Daniel"),  
              )

hijo = Relation()
facts(hijo,   ("Pancho","Mario"),
              ("Edmundo","Mario"),
              ("Johnny","Mario"),
              ("Daniela","Mario"),
              ("Adriana","Pancho"),
              ("Alejandra","Pancho"),
              ("Diego","Renato"),
              ("Daniel","Renato"),              
              ("Pancho", "Dora"),
              ("Edmundo", "Dora"),
              ("Johnny", "Dora"),
              ("Daniela", "Dora"),
              ("Adriana", "Patricia"),
              ("Alejandra","Patricia"),
              ("Diego", "Daniela"),
              ("Daniel", "Daniela"),  
              )


abuelo = Relation()
facts(abuelo, ("Dora",  "Adriana"),
              ("Dora",  "Alejandra"),
              ("Dora",  "Diego"),
              ("Dora",  "Daniel"),              
              ("Mario",  "Adriana"),
              ("Mario",  "Alejandra"),
              ("Mario",  "Diego"),
              ("Mario",  "Daniel"),              
              )

tio= Relation()
facts(tio,    ("Johnny",  "Daniel"),
              ("Edmundo",  "Daniel"),
              ("Pancho",  "Daniel"),
              ("Johnny",  "Diego"),
              ("Edmundo",  "Diego"),
              ("Pancho",  "Diego"),
              ("Johnny",  "Adriana"),
              ("Edmundo",  "Adriana"),
              ("Daniela",  "Adriana"),
              ("Johnny",  "Alejandra"),
              ("Edmundo",  "Alejandra"),
              ("Daniela",  "Alejandra"),              
              )

primo = Relation()
facts(primo,  ("Adriana",  "Daniel"),
              ("Alejandra",  "Daniel"),
              ("Adriana",  "Diego"),
              ("Alejandra",  "Diego"),
              ("Daniel",  "Adriana"),
              ("Daniel",  "Alejandra"),
              ("Diego",  "Adriana"),
              ("Diego",  "Alejandra"),
              )

hermano = Relation()
facts(hermano,("Adriana",  "Alejandra"),
              ("Alejandra",  "Adriana"),
              ("Daniel",  "Diego"),
              ("Diego",  "Daniel"),
              ("Daniela",  "Johnny"),
              ("Daniela",  "Edmundo"),
              ("Daniela",  "Pancho"),
              ("Johnny",  "Daniela"),
              ("Johnny",  "Edmundo"),
              ("Johnny",  "Pancho"),
              ("Pancho",  "Daniela"),              
              ("Pancho",  "Edmundo"), 
              ("Pancho",  "Johnny"),
              ("Edmundo",  "Daniela"),
              ("Edmundo",  "Johnny"),
              ("Edmundo",  "Pancho"),
              )

print(run(2, x, abuelo(x, "Adriana")))
print(run(2, x, hijo(x, "Daniela")))
print(run(3, x, primo(x, "Diego")))
print(run(2, x, tio(x, "Daniel")))
print(run(3, x, hermano(x, "Edmundo")))
