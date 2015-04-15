#! /usr/bin/env python 
#coding: utf-8

from State import state
from Node import node

class problem:
	
	def __init__(self):
		self.meta=state(0,2)
		self.initialState = node(state(0,0),None,None,0)

	#Checa se o node tem o estado meta 
	#State - Estado recebido
	#Return true se o no tem o estado meta senão retorna false
	def goalTest(self,state):
		return(state==self.meta)
			
	#Metodo que cria uma lista de action que um no pode realizar 
	#State - Estado recebido
	#Return a lista de ações possiveis de ser realizado por aquele state
	def actions(self,state):
		resp=list()
		if(state.j3!=0):
			resp.append("JOGAR34")
		if(state.j4!=0):
			resp.append("JOGAR43")
		if(state.j3!=3):
			resp.append("ENCHER3")
		if(state.j4!=4):
			resp.append("ENCHER4")
		if(state.j3!=0):
			resp.append("ESVAZIAR3")
		if(state.j4!=0):
			resp.append("ESVAZIAR4")
		return resp
	
	#Cria um novo estado baseado nos parametros dados
	#stat - Estado que vai sofrer a ação
	#action - Ação que vai ser executada no state
	#Return um novo estado resultado da ação de action aplicada no estado state
	def result(self,stat,action):
		resp=state(stat.j3,stat.j4)
		if(action=="ENCHER3"):
			resp.encher3()
		if(action=="ENCHER4"):
			resp.encher4()
		if(action=="ESVAZIAR3"):
			resp.esvaziar3()
		if(action=="ESVAZIAR4"):
			resp.esvaziar4()
		if(action=="JOGAR34"):
			resp.jogar34()
		if(action=="JOGAR43"):
			resp.jogar43()
		return resp
	
	#state - Estado que vai ter o custo calculado
	#action - Ação que vai ser executada no state
	#Return o inteiro que representa o custo de fazer essa ação nesse estado
	def stepCost(self,state,action):
		return 1	
	
	
