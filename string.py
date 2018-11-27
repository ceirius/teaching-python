# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 12:12:20 2018

@author: shreyas
"""

"""
Write a function that reverses a string. The header of the function is:
def reverse(s):
Write a test program that prompts the user to enter a string, invokes the 
reverse function, and displays the reversed string.
"""


def reverse(qwerty):
    
    i = -1
    j = len(qwerty)
    rev = ""
    for k in range(len(qwerty)):
        rev += qwerty[i]
        
        print(i, "\t", j, "\t", k, "\t", rev)
        i -= 1
        j -= 1
        k += 1
        
    
    
qwerty = input("enter a string:\t\t")
reverse(qwerty)


    