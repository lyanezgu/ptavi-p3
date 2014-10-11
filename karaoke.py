#!/usr/bin/python
# -*- coding: utf-8 -*-
import smallsmilhandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import os
sys.argv


def autenticar(argument):
    try:
        fich = sys.argv[1]
    except:

        if len(argument) != 2:

            sys.exit("Usage: python karaoke.py file.smile")
    return fich


class KaraokeLocal(smallsmilhandler.SmallSMILHandler):

    def __init__(self, fichero):
        parser = make_parser()
        smallHandler = smallsmilhandler.SmallSMILHandler()
        parser.setContentHandler(smallHandler)
        parser.parse(open(fich))
        self.lista = smallHandler.get_tags()

    def __str__(self):
        lista = self.lista
        NumTotal = len(lista) / 2
        Contador = 0
        posa = 0
        posb = 1
        while Contador < NumTotal:
            etiqueta = lista[posa]
            val = lista[posb]  # contiene el atributo y el valor
            print etiqueta + "\t",

            for atributo, valor in val.items():
                if valor != "":  # cuabdo hay clave y valor
                    print atributo + "=" + '"' + valor + '"' + "\t",

            Contador = Contador + 1
            posa = posa + 2  # se pasa de dos en dos ya que son clave y valor
            posb = posb + 2
            print "\n",

    def do_local(self):
        lista = self.lista
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
                    # separo cadena cada / quedo con el final de cadena
                    recurso = recurso.split("/")[-1]
                    val[atributo] = recurso
            Contador = Contador + 1
            posa = posa + 2
            posb = posb + 2


if __name__ == "__main__":
    fich = autenticar(sys.argv)
    KarLocal = KaraokeLocal(autenticar(fich))
    KarLocal.__str__()
    KarLocal.do_local()
    KarLocal.__str__()
