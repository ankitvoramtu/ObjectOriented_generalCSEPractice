# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 00:56:34 2016

@author: jobin
"""

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
        
        
def question4(T, r, n1, n2):
    builtTree = Tree()
    builtTree.table(r)

question4(tree,4,8,10)