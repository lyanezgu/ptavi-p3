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



if __name__ == "__main__":
    
    fich = autenticar(sys.argv)
