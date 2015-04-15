#! /usr/bin/env python 
#coding: utf-8

#mainState

from collections import deque

from State import state
from Node import node
from Problem import problem
from Frontier import frontier

#Depth First Search
#Realiza uma busca em profundidade para achar a solução de um problema

#Cria um no filho
#problem - Problema a ser resolvido
#parent - pai do no a ser criado
#action - String que representa a ação que vai ser executada no pai para que o filho seja gerado
#Return o no filho
def childNode(problem,parent,action):
	return node(
		problem.result(parent.state,action),
		parent,
		action,
		parent.pathCost+problem.stepCost(parent.state,action))
	

#Imprime a sequencia de estado que leva do estado incial a solução
def solution(node):
	if(node.parent is None):
		return str(node.state)
	else:
		return solution(node.parent)+" "+node.action+" "+str(node.state)
#Main
exe=True
i=0
problem=problem()
nod = problem.initialState
frontier=frontier()
frontier.append(nod)
explored = list() 
if(problem.goalTest(nod.state)): 
	print solution(nod)
while(exe):
	if(len(frontier)==0):
		print "FAILURE"
		break
	nod = frontier.pop()
	explored.append(nod.state)
	print "State: "+str(nod.state)
	print "EXPLORED SET"
	for state in explored:
		print state
	for action in problem.actions(nod.state):
		child=childNode(problem,nod,action)
		if (child.state not in explored) or (child not in frontier):
			if(problem.goalTest(child.state)):
				print solution(child)
				exe=False
				break
			#if(i==50):
			#	exe=False
			#	break 
			frontier.append(child)
			i+=1
