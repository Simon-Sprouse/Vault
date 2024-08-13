#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:30:27 2024

@author: simonsprouse
"""


from collections import deque

## bungus

class Node:
    
    def __init__(self, key, page):
        self.edges = {} ## will store references to other nodes
        self.key = key
        self.page = page
        
    def printNode(self):
        print(self.key, self.page)
        
        
root = Node("", "")

node_a = Node("adam", "adam.html")
node_b = Node("benson", "benson.html")

node_a_2 = Node("adams", "adams.html")
node_a.edges = {"s": node_a_2}

root.edges = {
    "adam": node_a,
    "benson": node_b
    }






def printTree(root):
    
    visited = set()
    
    q = deque()
    q.append(root)
    
    visited.add(root)
    
    
    
    while q: 
        
        top = q.popleft()
        top.printNode()
        
        for edge, Node in top.edges.items():
            if edge not in visited:
                visited.add(Node)
                q.append(Node)
        



printTree(root)















def comparePrefix(string_1, string_2):
    
    common_prefix = "" ## adam and addition would be ad
    
    min_length = min(len(string_1), len(string_2))
    
    for char in range(min_length):
        if string_1[char] != string_2[char]:
            return common_prefix
        else:
            common_prefix += string_1[char]
            
    return common_prefix


string_1 = "bubble"
string_2 = "bubbles"

common = comparePrefix(string_1, string_2)
print()


def insertNode(root, key, page):
    
    if not key:
        return None
    
 

    for existing_key in root.edges.keys():

        match = comparePrefix(key, existing_key)
        
        if match:
            print(match) ## ad
            
            if match == key:
                
                4
                ## I need to handle this still
            


            
            
            new_parent_node = Node(match, "") ## ad
            
            old_node = root.edges[existing_key]

            
            new_parent_node.edges = { 
                existing_key[len(match):]   : old_node,
                key[len(match):]            : Node(key, page)
            }
            
            
            
            root.edges.pop(existing_key)
            root.edges[match] = new_parent_node
            
            
            return
        
        
    root.edges.add(Node(key, page))

        
insertNode(root, "addition", "add.html")





printTree(root)
    


