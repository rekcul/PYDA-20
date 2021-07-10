#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys
import numpy as np

#list of keywords
keywords=[]
for line in sys.stdin:
    keyword = line.strip().split(',')[:-1]
    keywords.append(keyword)

flat_list_of_keywords = np.array(keywords).flatten()

#list of words
words = []
for i in flat_list_of_keywords:
        word = i.strip().split(' ')
        words.append(word)
        
# list_of_words = np.array(words).flatten()
flat_list_of_words = [word for sublist in words for word in sublist]


# stdout
for i, word in enumerate(flat_list_of_words):
    print(word, '1') 
    
    if i > 1000:
        break

