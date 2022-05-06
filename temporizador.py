# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 14:30:14 2021

@author: dajos
"""

import time
print("Recuerde que debe ingresar max 60seg, max60min y las horas que desee")
a=int(input("Ingrese las horas: "))
b=int(input("Ingrese los minutos: "))
c=int(input("Ingrese los segundos: "))

while True:
    if(b==-1):
        b=60
        a -=1
    if(c==-1):
        c=60
        b -=1
    else:
        print(str(a)+">>"+str(b)+">>"+str(c), end=" \n")
    time.sleep(1)
    c -= 1
    time.sleep(1)
    if(a==0 and b==0 and c==-1):
        print("El tiempo se acabo!", end="\r")
        break
