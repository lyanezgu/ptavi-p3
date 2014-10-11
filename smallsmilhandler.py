#!/usr/bin/python
# -*- coding: utf-8 -*-
from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

	def __init__ (self):
		#defino un diccionario para cada etiqueta y lo meto en nuna lista
		self.RootLay = {}
		self.Reg= {}
		self.Img = {}
		self.Audio ={}
		self.TextS={}
		self.lista= []


	def startElement(self, name, attrs):

		if name == 'root-layout':

			atributo=attrs.get('width',"") #coger el valor del atributo
			self.RootLay['width']=atributo #almacena el atributo en dicc
			atributo=attrs.get('height',"")
			self.RootLay['height']=atributo
			atributo=attrs.get('background-color',"")
			self.RootLay['background-color']=atributo
			self.lista.append('root-layout')
			self.lista.append(self.RootLay)

		if name == 'region':
			atributo=attrs.get('id',"") 
			self.Reg['id']=atributo
			atributo=attrs.get('top',"") 
			self.Reg['top']=atributo
			atributo=attrs.get('bottom',"") 
			self.Reg['bottom']=atributo
			atributo=attrs.get('left',"") 
			self.Reg['left']=atributo
			atributo=attrs.get('right',"") 
			self.Reg['right']=atributo
			self.lista.append('region')
			self.lista.append(self.Reg)
			
		if name == 'img':

			atributo=attrs.get('src',"") 
			self.Img['src']=atributo
			atributo=attrs.get('region',"") 
			self.Img['region']=atributo
			atributo=attrs.get('begin',"") 
			self.Img['begin']=atributo
			atributo=attrs.get('dur',"") 
			self.Img['dur']=atributo
			self.lista.append('img')
			self.lista.append(self.Img)
			
		if name == 'audio':
			atributo=attrs.get('src',"") 
			self.Audio['src']=atributo
			atributo=attrs.get('begin',"") 
			self.Audio['begin']=atributo
			atributo=attrs.get('dur',"") 
			self.Audio['dur']=atributo
			self.lista.append('audio')
			self.lista.append(self.Audio)
			
		if name == 'textstream':
			atributo=attrs.get('src',"") 
			self.TextS['src']=atributo
			atributo=attrs.get('region',"") 
			self.TextS['region']=atributo
			self.lista.append('textstream')
			self.lista.append(self.TextS)


	def get_tags(self):
		return self.lista

if __name__ == "__main__":

	parser= make_parser()
	smallHandler= SmallSMILHandler()
	parser.setContentHandler(smallHandler)
	parser.parse(open('karaoke.smil'))
	print smallHandler.get_tags()
