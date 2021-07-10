#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
import numpy as np


# In[ ]:


prev_word = None
counter = 0

for line in sys.stdin:
    word, one = line.strip().split(' ') 
    one = int(one)

    if prev_word:
        if prev_word == word:
            counter += one
        else:
            print(prev_word, counter)
            prev_word = word
            counter = one
    else:
        prev_word = word
        counter = one

print(prev_word, counter)

