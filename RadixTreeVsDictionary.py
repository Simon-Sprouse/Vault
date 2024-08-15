#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 14:07:52 2024

@author: simonsprouse
"""

from RadixTree3 import RadixTree
from generateDataSet import generateData

import pandas as pd
import time





class Timer:
    
    def __init__(self):
        self.start_time = None
        self.stop_time = None
        
    def start(self):
        self.start_time = time.perf_counter()
        
    def stop(self):
        self.stop_time = time.perf_counter()
        
    def delta(self):
        return self.stop_time - self.start_time
    
    def printDeltaMs(self):
        print("Time: {:0.2f} ms".format(self.delta() * 1000))
        print()
        
    def printDelta(self):
        print("Time: {:0.2f} s".format(self.delta()))
        print()


timer = Timer()



"""
------------------------------------------
            Generate Dataset
------------------------------------------
"""
print("Generating Datset")
timer.start()


generateData(100)


timer.stop()
timer.printDelta()





"""
------------------------------------------
        Create DataFrame (timed)
------------------------------------------
"""

print("Creating DataFrame")
timer.start()

df = pd.read_csv("./augmented_data.csv")
df = df.sort_values(by="key")

timer.stop()
timer.printDelta()



"""
------------------------------------------
        Create Dictionary (timed)
------------------------------------------
"""

print("Creating Map")
timer.start()

key_page_map = df.set_index("key")["page"].to_dict()



timer.stop()
timer.printDelta()



"""
------------------------------------------
      Create Search List For Testing
------------------------------------------
"""
search_list = list(key_page_map.keys())
# print(search_list)



"""
------------------------------------------
        Create Radix Tree (timed)
------------------------------------------
"""

print("Creating Radix Tree")
timer.start()

start = time.perf_counter()
r = RadixTree()


for key, page in key_page_map.items():
    r.insert(key, page)
    
    
timer.stop()
timer.printDelta()



"""
------------------------------------------
    Search All Keys Using Map (timed)
------------------------------------------
"""

print("Searching All Keys Using Map")
timer.start()

for term in search_list:
    s = key_page_map[term]


timer.stop()
timer.printDelta()






"""
------------------------------------------
 Search All Keys Using Radix Tree (timed)
------------------------------------------
"""


print("Searching All Keys Using Radix Tree")
timer.start()

for term in search_list:
    s = r.search(term)


timer.stop()
timer.printDelta()


