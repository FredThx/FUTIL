#!/usr/bin/env python
# -*- coding:utf-8 -*

import logging

class ma_classe():
	'''Pour test
	'''
	def __init__(self):
		'''Init
		'''
		logging.info("objet ma_classe créé")
		
	def __del__(self):
		logging.warning("Un objet ma_classe se meurt!")
		
	def plante(self):
		raise SyntaxError
	
	def plante_pas(self):
		try:
			0/0
		except Exception, e:
			logging.error("une '%s' a été évité" % e)