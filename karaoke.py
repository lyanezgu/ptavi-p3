#!/usr/bin/python
# -*- coding: utf-8 -*-
import smallsmilhandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import os
sys.argv

def autenticar (argument):
    try:
        fich = sys.argv[1]
    except:
        
        if len(argument) != 2:
            
            sys.exit("Usage: python karaoke.py file.smile")
    return fich
def listado (lista):
    NumTotal = len(lista) / 2 
    Contador = 0
    posa = 0
    posb = 1
    while Contador < NumTotal:
        etiqueta = lista[posa]
        val = lista[posb] # contiene el atributo y el valor 
        print etiqueta + "\t",

        for atributo, valor in val.items():
            if valor != "": # cuabdo hay clave y valor 
                print atributo + "=" + '"' + valor + '"' + "\t",

        Contador = Contador + 1
        posa = posa + 2 # se pasa de dos en dos ya que son clave y valor
        posb = posb + 2
        print "\n",

def hacer_local (lista):
    NumTotal = len(lista) / 2
    Contador = 0
    posa = 0
    posb = 1
    while Contador < NumTotal:
        etiqueta = lista[posa]
        val = lista[posb]
        for atributo, valor in val.items():
            if 'src' == atributo and "http" in valor:
                recurso = valor
                os.system("wget -q " + recurso)
                recurso = recurso.split("/")[-1] # separo la cadena en cada / y me quedo con el ultimo cacho de la cadena
                val[atributo] = recurso
        Contador = Contador + 1
        posa = posa + 2
        posb = posb + 2  
        


if __name__ == "__main__":
    
    fich = autenticar(sys.argv)
    parser = make_parser()
    smallHandler = smallsmilhandler.SmallSMILHandler()
    parser.setContentHandler(smallHandler)
    parser.parse(open(fich))
    lista = smallHandler.get_tags()
    hacer_local(lista)
    print listado(lista)
        
