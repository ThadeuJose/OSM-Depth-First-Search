#! /usr/bin/env python 
#coding: utf-8

from copy import deepcopy

class state:

	def __init__(self,jarra3,jarra4):
		self.j3=jarra3
		self.j4=jarra4
		
	def encher3(self):
		self.j3=3
		
	def encher4(self):
		self.j4=4
	
	def esvaziar3(self):
		self.j3=0
		
	def esvaziar4(self):
		self.j4=0
		
	#jogar 3 em 4	
	def jogar34(self):
		while(self.j3!=0):
			if(self.j4==4):
				break
			self.j3-=1
			self.j4+=1
		
	#jogar 4 em 3
	def jogar43(self):
		while(self.j4!=0):
			if(self.j3==3):
				break
			self.j3+=1
			self.j4-=1
	
	def __eq__(self,other):
		return (self.j3==other.j3 and self.j4==other.j4)
	
	def __ne__(self,other):
		return not(__eq__(self,other))
	
	def __hash__(self):
		return hash((self.j3,self.j4))
		
	def __str__(self):
		return str(str(self.j3)+" "+str(self.j4))

