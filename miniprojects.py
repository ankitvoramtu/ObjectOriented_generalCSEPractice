import json
import random

def question1(s, t):
	return True if (t[::-1] in s or t in s) else False
	# for val in range(len(t)):
	# 	found = True
	# 	if t[val] not in s:
	# 		found= False
	# 		break
	# 	else:
	# 		count = 0
	# 		ss = list(s)
	# 		for l in ss:
	# 			count+=1 
	# 			if l==t[val]:
	# 				del ss[count]
	# 				break
	# return found

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
	#chosenVertex.append('A')
	#print chosenVertex
	weightTable = []
	for key in s32:
	    for val in s32[key]:
	        v = sorted([key, val[0]])
	        if [val[1],v[0],v[1]] not in weightTable:
	            weightTable.append([val[1],v[0],v[1]]) 
	weightTable =  sorted(weightTable)
	#print weightTable
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
	print 'chosenVertex = {},\nchosenEdges = {}'.format(chosenVertex,chosenEdges)
	answer = {}
	for val in chosenVertex:
		print val
		for edge in chosenEdges:
			if val in edge:
				if val in answer:
					answer[val].append((edge[2] if val!= edge[2] else edge[1],edge[0]))
				else:
					answer[val] = [(edge[2] if val!= edge[2] else edge[1],edge[0])]
	return answer    


def question4(T, r, n1, n2): # question4(tree, 4,1,12)
	class Node:
	    def __init__(self,val):
	        self.value = val
	        self.leftChild = None
	        self.rightChild = None
	    def insert(self, data):
	        if self.value == data:
	            return False	
	        elif self.value > data:
	            if self.leftChild: 
	                return self.leftChild.insert(data)
	            else:
	                self.leftChild = Node(data)
	                return True
	        else: 
	            if self.rightChild:
	                return self.rightChild.insert(data)
	            else:
	                self.rightChild = Node(data)
	                return True
	        
	class Tree: 
	    def __init__(self):
	        self.root = None
	    def insert(self, data):
	        if self.root:
	            return self.root.insert(data)
	        else:
	            self.root = Node(data)
	            return True
	    def table(self, r):
	        self.insert(r)
	        for i,val in enumerate(tree[r-1]):
	            if val == 1: 
	                return self.table(i)

	# def getChildren(Tree, node):
	#     # read the row in the Tree that belongs to the node, checking each spot for a child
	#     for position in Tree[node]:
	#         if position == 1:
	#             # you found a child node, now insert it!
	
	# def getChildren(T,r):
	# 	tree = Tree(r)
	# 	# read the row in the Tree that belongs to the node, checking each spot for a child
	# 	for row in T:
	# 		for i, position in enumerate(row):
	# 			if position == 1:
	# 				tree.insert(i)
	#getChildren(T,r)

	theTree = Tree()
	theTree.table(r)

	def lca(root, n1, n2):
		if( root > n1 and root > n2):
			return lca(root.left, n1, n2)
		elif(root < n1 and root < n2):
			return lca(root.right, n1, n2)
		else:
			return root
def question5(ll,m): 
	class Node(object):

	    def __init__(self, data=None, count = None, next_node=None):
	        self.data = data
	        self.c = count
	        self.next_node = next_node

	    def get_data(self):
	        return self.data
	    
	    def get_i(self):
	        return self.c

	    def get_next(self):
	        return self.next_node

	    def set_next(self, new_next):
	        self.next_node = new_next

	class LinkedList(object):
	    def __init__(self, head=None):
	        self.head = head
	        self.c =0
	    def insert(self, data):
	        self.c+=1
	        new_node = Node(data,self.c)
	        new_node.set_next(self.head)
	        self.head = new_node
	    def size(self):
	        current = self.head
	        count = 0
	        while current:
	            count += 1
	            current = current.get_next()
	        return count
	    def search(self, data):
	        current = self.head
	        found = False
	        while current and found is False:
	            if current.get_i() == data:
	                found = True
	            else:
	                current = current.get_next()
	        if current is None:
	            raise ValueError("Data not in list")
	        return current
	    def printer(self):
	        current = self.head
	        while current:
	            print current.get_i()
	            current = current.get_next()
	    def makeLinked(self, array):
	        for val in array:
	            self.insert(val)
	    def getMth(self, m):
	        m = m-1
	        newIndex = self.size()-m
	        found = self.search(newIndex)
	        return found.get_data()

	linked = LinkedList()
	linked.makeLinked(ll)
	return linked.getMth(m)

def main():
	## Functions
	#print question1(s,t)
	#print question2(word)
	#print question3(s32)
	question4(tree, 4,1,12)
	# makeLinked = LinkedList()
	# headNode = makeLinked.getHeadNode()
	#print question5(ll,m) # ll (first node is 3), m mth num from end




## Variables 
# for # 1
s = 'udacityy'
t = 'ty'
# for # 2
#word = 'kayakhello'
word = 'kayak'
word = 'notaplindrome'
word = 'a'
# for # 3 
s32 = {'A':[('E',5),('H',6),('F',1),('B',8),('B',8)],'B':[('F',6),('C',4)],'C':[('F',2),('G',7)],'G':[('F',9)],'F':[('H',5)],'H':[('E',3)]}
# for # 4
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
# for # 5 
ll = [3,5,4,2,1]; m = 2
if __name__ == '__main__':
	main()