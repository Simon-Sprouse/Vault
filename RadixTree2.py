#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 13:17:40 2024

@author: simonsprouse
"""



class Node:
    def __init__(self, key, page):
        self.edges = {}  # will store references to other nodes
        self.key = key
        self.page = page

    def printNode(self, depth=0):
        print("\t" * depth + f"'{self.key}' ({self.page})")



def printTree(root, depth=0):
    if not root:
        return
    
    root.printNode(depth)
    
    for edge, node in root.edges.items():
        printTree(node, depth + 1)





def comparePrefix(string_1, string_2):
    common_prefix = ""  ## adam and addition would be "ad"
    min_length = min(len(string_1), len(string_2))
    
    for char in range(min_length):
        if string_1[char] != string_2[char]:
            return common_prefix
        else:
            common_prefix += string_1[char]
            
    return common_prefix


def insertNode(root, key, page):
    
    if not key:
        return None
    
    ## loop through existing paths to find a prefix match 
    
    for existing_key in list(root.edges.keys()):
        
        match = comparePrefix(key, existing_key)
        
        if match:
            
            if match == existing_key:
                ## existing key is prefix of new key, reccur to add rest of new key
                insertNode(root.edges[existing_key], key[len(match):], page)
                return
            
            else:

                
                ## trim common prefix off of old node
                old_node = root.edges.pop(existing_key)
                old_node.key = existing_key[len(match):]
                
                
                ## trim common prefix off new key and create new node
                new_node = Node(key[len(match):], page)
               
                
                ## common prefix becommes a parent node connecting new and old nodes
                parent_node = Node(match, "")
                parent_node.edges = {
                    old_node.key : old_node,
                    new_node.key : new_node
                }
                root.edges[match] = parent_node
                
                return
    
    ## If no prefix match, add as a direct descendant
    root.edges[key] = Node(key, page)
    
    
    
    
    
    
def search(root, key):
    
    if not key: 
        return None
    
    while key: 
        
        found = False
        
        for existing_key, child_node in root.edges.items():

            match = comparePrefix(existing_key, key)
            
            if match:
                
                if match == key:
                    
                    return child_node.page
                
                else: 
                    
                    key = key[len(match):]
                    root = child_node
                    found = True
                    break
                
                
        if not found:
            
            return None
                    
    
def deletePage(root, key):
    
    if not key: 
        return False
    
    while key: 
        
        found = False
        
        for existing_key, child_node in root.edges.items():

            match = comparePrefix(existing_key, key)
            
            if match:
                
                if match == key:
                    
                    child_node.page = ""
                    return True
                
                else: 
                    
                    key = key[len(match):]
                    root = child_node
                    found = True
                    break
                
                
        if not found:
            
            return False
    
    
    
    


root = Node("", "")


insertNode(root, "adam", "adam.html")
insertNode(root, "adams", "adams.html")

insertNode(root, "addition", "add.html")
insertNode(root, "adamant", "adamant.html")

insertNode(root, "benson", "benson.html")
insertNode(root, "bent", "bent.html")

printTree(root)



