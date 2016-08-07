import json
import random

from collections import defaultdict


def question1(s, t):
	# q1 = [('udacity', 'ty'),('tyudacity', 'ty'),('elephant', 'cart')]
	length = len(s)
	#subStrings =  [s[i:j+1] for i in xrange(length) for j in xrange(i,length)]

	for i in xrange(length):
		for j in xrange(i,length):
			word = s[i:j+1]
			table = defaultdict(list)
			table[''.join(sorted(word.lower()))].append(word)
			table[''.join(sorted(t.lower()))].append(t)
			if [v for k,v in table.items() if len(v)>1]:
				return True
	return False


def question2(a):
    possibleChoices = []
    for j in range(0,len(a)+1):
        for i in range(0,len(a)+1):
            if len(str(a[j:i]))>0 and str(a[j:i]) == str(a[j:i])[::-1]:
            	possibleChoices.append(str(a[j:i]))
    return max(possibleChoices, key=len) if possibleChoices else 'none found'


def question3(G):
	chosenVertex = []
	chosenEdges = []
	s32 = G
	chosenVertex.append(random.choice(s32.keys()))
	weightTable = []
	for key in s32:
	    for val in s32[key]:
	        v = sorted([key, val[0]])
	        if [val[1],v[0],v[1]] not in weightTable:
	            weightTable.append([val[1],v[0],v[1]]) 
	weightTable =  sorted(weightTable)
	completeVertexes = sorted(list(set([key for key in s32 for val in s32[key] ] + 
	                            [val[0] for key in s32 for val in s32[key]])))
	while(chosenVertex != completeVertexes):   
	    for val in weightTable:
	        if val[1] in chosenVertex or val[2] in chosenVertex: # not a != (not b)
	            if val[1] not in chosenVertex or val[2] not in chosenVertex:
	                if val not in chosenEdges:
	                    chosenEdges.append(val)
	                chosenVertex.append(val[2] if val[2] not in chosenVertex else val[1])
	                chosenVertex = sorted(chosenVertex)
	                break
	answer = {}
	for val in chosenVertex:
		for edge in chosenEdges:
			if val in edge:
				if val in answer:
					answer[val].append((edge[2] if val!= edge[2] else edge[1],edge[0]))
				else:
					answer[val] = [(edge[2] if val!= edge[2] else edge[1],edge[0])]
	return answer    


def question4(T, r, n1, n2): # question4(tree, 4,1,12)
	
	class Node:
		def __init__(self, val):
			self.value = val+1
			self.connects = []
		def addConnect(self, node):
			self.connects.append(node)
		def printConnect(self):
			return self.value

	arrayOfNodes =  [ Node(node) for node in range(10)]
	for i, row in enumerate(T):
		for inode, j in enumerate(row):
			if j == 1: 
				arrayOfNodes[i].addConnect(arrayOfNodes[inode])

	class dynamicTree:
		def __init__(self, val):
		 	self.roots = []

		def lca(r, n1, n2):
			chooseableNode = []
			self.roots.append(arrayOfNodes[r-1]) # remove value

			if arrayOfNodes[r-1].value > n1 and arrayOfNodes[r-1].value > n2:
				for val in arrayOfNodes[r-1].connects:
					if val not in roots:
						chooseableNode.append(val)
				if chooseableNode[1]:
					if chooseableNode[0].value < chooseableNode[1].value:
						return lca(chooseableNode[0],n1, n2)
					else:
						return lca(chooseableNode[1],n1, n2)
				else: return lca(chooseableNode[0],n1, n2) 
			elif arrayOfNodes[r-1].value < n1 and arrayOfNodes[r-1].value < n2:
				for val in arrayOfNodes[r-1].connects:
					if val not in roots:
						chooseableNode.append(val)
				if chooseableNode[1]:
					if chooseableNode[0].value < chooseableNode[1].value:
						return lca(chooseableNode[1],n*1, n2)
					else:
						return lca(chooseableNode[0],n1, n2)
				else: return lca(chooseableNode[0],n1, n2) 
				
				# append arrayOfNodes[r-1].value to roots.append(arrayOfNodes[r-1].value)
				# for val in connects: if val not in roots, append to choosable array
				# choose min or MAX value
			else:
				return arrayOfNodes[r-1].value 

class Nodee(object):
	def __init__(self, data):
		self.data = data
		self.next = None


def question5(ll,m):
	length = 1
	root = ll
	while root.next:
		length = length+1
		root = root.next
	root = ll
	count = 0 
	while count< length-m:
		count = count+1
		root = root.next

	return root.data


def main():	

	print '\nQuestion 1:'
	q1 = [('udacity', 'ty'),('tyudacity', 'ty'),('elephant', 'cart')]
	for test in q1:
		print question1(test[0],test[1])

	print '\nQuestion 2:'
	word = ['kayakhello','kayak','notaplindrome', 'a']
	for a in word: 
		print question2(a)

	print '\nQuestion 3:'	
	s32 = {'A':[('E',5),('H',6),('F',1),('B',8),('B',8)],'B':[('F',6),('C',4)],'C':[('F',2),('G',7)],'G':[('F',9)],'F':[('H',5)],'H':[('E',3)]}
	print question3(s32),'\n-\n'
	s32 = {'A':[('E',5),('H',6),('F',1)],'B':[('F',6),('D',4)],'C':[('F',2),('A',7)],'G':[('D',9)],'F':[('A',5)],'H':[('F',3)]}
	print question3(s32),'\n-\n'
	s32 = {'A':[('B',5),('C',6),('D',1),('B',8),('B',8)],'B':[('D',6),('F',4)],'C':[('D',2),('E',7)],'G':[('C',9)],'F':[('B',5)],'H':[('A',3)]}
	print question3(s32),'\n-\n'

	print '\nQuestion 4:'	
	tree = [[0,1,0,0,0,0,0,0,0,0],
		[1,0,1,1,0,0,0,0,0,0],
		[0,1,0,0,0,0,0,0,0,0],
		[0,1,0,0,0,0,1,0,0,0],
		[0,0,0,0,0,0,0,0,0,0],
		[0,0,0,0,0,0,1,0,0,0],
		[0,0,0,1,0,1,0,0,1,0],
		[0,0,0,0,0,0,0,0,1,0],
		[0,0,0,0,0,0,1,1,0,1],
		[0,0,0,0,0,0,0,0,1,0]]
	question4(tree, 4,1,12)
	
	print '\nQuestion 5:'	
	root = Nodee(1)
	root.next = Nodee(2)
	root.next.next = Nodee(3)
	root.next.next.next = Nodee(4)
	print question5(root, 2)

	del root

	root = Nodee(5)
	root.next = Nodee(4)
	root.next.next = Nodee(2)
	root.next.next.next = Nodee(1)
	root.next.next.next.next = Nodee(3)
	root.next.next.next.next.next = Nodee(23)
	root.next.next.next.next.next.next = Nodee(31)
	print question5(root, 4)

	del root

	root = Nodee(1)
	root.next = Nodee(2)
	print question5(root, 1)

if __name__ == '__main__':
	main()