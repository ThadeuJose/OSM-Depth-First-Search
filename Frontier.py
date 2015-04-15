#! /usr/bin/env python 
#coding: utf-8

from collections import deque

class frontier(deque):

	def __init__(self,maxSize=0):
		self.maxSize = maxSize
		self.stateSet=set()
	 	self.queue=deque()
			
 	def append(self,nod):
 		if(nod not in self.stateSet):
 			self.queue.append(nod)
 			self.stateSet.add(nod)
 			print "StateSet:"
			print ",".join(str(e) for e in self.stateSet)
			print len(self.stateSet) 			
 			print "Child:"
			print str(nod)+str(nod in self.stateSet)
			print "______________________________________________"
 			
 	def __contains__(self,key):
 		return key in self.stateSet
 
 	def __len__(self):
 		return len(self.queue)
 	
 	def pop(self):
 		element=self.queue.popleft()
 		self.stateSet.remove(element)
		return element
		
	def __str__(self):
		string=""
		string+=",".join(str(e) for e in self.queue)
		return string
