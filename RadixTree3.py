#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 23:44:17 2024

@author: simonsprouse
"""


def comparePrefix(str_1, str_2):
    
    string_1 = str(str_1)
    string_2 = str(str_2)
    
    
    
    
    common_prefix = ""  ## adam and addition would be "ad"
    min_length = min(len(str(string_1)), len(str(string_2)))
    
    
    
    for char in range(min_length):
        if string_1[char] != string_2[char]:
            return common_prefix
        else:
            common_prefix += string_1[char]
            
    return common_prefix





class Node:
    def __init__(self, key, page):
        self.edges = {}  # will store references to other nodes
        self.key = key
        self.page = page
        self.number_of_children = 0

    def printNode(self, depth=0):
        print("\t" * depth + f"'{self.key}' ({self.page})")




class RadixTree:
    


    
    def __init__(self):
        self.root = Node("", "")
        
    
    ### PUBLIC METHODS ###
    
    
    def printTree(self):
       self. _printTree(self.root)
        
    def insert(self, key, page):
         self._insertNode(self.root, key, page)
            
    def search(self, key):
        return self._search(self.root, key)
                            


    ### PRIVATE METHODS ###

    def _printTree(self, root, depth=0):
        if not root:
            return
        
        root.printNode(depth)
        
        for edge, node in root.edges.items():
            self._printTree(node, depth + 1)
    
    



    
    def _insertNode(self, root, key, page):
        
        if not key:
            return None
        
        ## loop through existing paths to find a prefix match 
        
        for existing_key in list(root.edges.keys()):
            
            match = comparePrefix(key, existing_key)
            
            if match:
                
                if match == existing_key:
                    ## existing key is prefix of new key, reccur to add rest of new key
                    self._insertNode(root.edges[existing_key], key[len(match):], page)
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
        
        
   
      
    
    
    def _search(self, root, key):
        
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
            
            
            

    

        
        
    

# r = RadixTree()



# r.insert("adam", "adam.html")
# r.insert("adamant", "adamant.html")


# r.printTree()


# s = r.search("adam")
# print(s)






