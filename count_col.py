# -*- coding: utf-8 -*-
"""
Spyder Editor

@author  shan
"""
import numpy as np
import pandas as pd


def count_col(pdframe1,pdframe2,feature1 = "word",feature2 = "char",feature3 = "charFreq"):
    word_array = pdframe1[feature1]
    char_array = pdframe2[feature2]
    np_array_word_set = np.array([])
    
    for w in word_array:
        np_array_word_set = np.append(np_array_word_set,set(w))
    
    collocation = {}
    for c in char_array:
        collocation[c] = 0
        for word_set in np_array_word_set:
            if c in word_set:
                collocation[c] += (len(word_set) - 1)

    char_num_collocations_array = np.array([],dtype = 'int16' )
    
    for i in range(len(pdframe2)):
        char_num_collocations_array  =  np.append(char_num_collocations_array ,collocation[char_array[i]])
    
    pdframe2['#collocations'] = char_num_collocations_array

    return None
