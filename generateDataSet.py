#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 00:31:58 2024

@author: simonsprouse
"""

import csv
import random
import string
import nltk
from nltk.corpus import words

def generateData(num_entries):

    ## nltk.download('words')
    english_words = words.words()
    random.shuffle(english_words)
    
    def generate_html_filename():
        name_length = random.randint(5, 10)  # Length of the random name
        random_name = ''.join(random.choices(string.ascii_lowercase, k=name_length))
        return f"{random_name}.html"
    
    
    
    

    selected_words = english_words[:num_entries]
    
    
    data = [(word, generate_html_filename()) for word in selected_words]
    
    
    with open('augmented_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['key', 'page'])  # Write header
        writer.writerows(data)  # Write data rows
    
    









