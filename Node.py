#! /usr/bin/env python 
#coding: utf-8

from copy import deepcopy

class node:

	def __init__(self,state,parent,action,pathCost):
		self.state=deepcopy(state) #Estado do no 
		self.parent=deepcopy(parent)#Pai do no
		self.action=action#acão no pai que gera esse no
		self.pathCost=pathCost#custo do caminho
		
	def __eq__(self,other):
		return (self.state==other.state)
		
	def __hash__(self):
		return hash(hash(self.state))	
		
	def __str__(self):
		return str(self.state)
