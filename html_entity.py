# -*- coding: utf-8 -*-
"""
Created on Tue Feb  10 9:37:58 2017

@author: kilicm
"""


import os
import codecs
import re


def entity2char(word):
    for filenames in  os.listdir('.'):
        if filenames.endswith('.txt'):
            with codecs.open(filenames, 'w', encoding='utf-8-sig') as f:
                for line in lines:
                    
                    for word in line.split():
                        result = re.sub(r"&#(\d+);", lambda m: chr(int(m.group(1))), word)
                        #print(result)
                        f.write(result)
                        f.write(' ')

for filenames in  os.listdir('.'):
    if filenames.endswith('.txt'):
        with codecs.open(filenames, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
            
            entity2char(lines)