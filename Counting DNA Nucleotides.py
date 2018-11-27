# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Problem
A string is simply an ordered collection of symbols selected from some alphabet 
and formed into a word; the length of a string is the number of symbols that it contains.

An example of a length 21 DNA string (whose alphabet contains the symbols 
'A', 'C', 'G', and 'T') is "ATGCTTCAGAAAGGTCTTACG."

Given: A DNA string s of length at most 1000 nt.

Return: Four integers (separated by spaces) counting the respective number of times that the symbols 'A', 'C', 'G', and 'T' occur in s.

Sample Dataset
AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
"""

import re


class baseCount:
    x = 0
    y = 0
    z = -1
    prop = 0
    base = ""
    revcomp = ""
    rev = ""
    rna = ""
    def __init__(self, base1, string):
        self.base = base1
        
    def count(self):
        """
        counting number of nucleotides and their proportions in a sequence
        """
        for self.x in range(len(string)):
            if re.match(self.base, string[self.x]):
                #print(string[self.x], self.x+1)
                self.y += 1
            self.x += 1
        self.prop = self.y/len(string)
        print("\t", self.base, ": \t\t", self.y, "\t\t", round(self.prop, 3))
    
    def RNA(self):
        """
        RNA translator
        """
        for self.x in range(len(string)):
            if re.match("A|G|C", string[self.y]):
                self.rna += string[self.y]
                self.y += 1
            else:
                self.rna += "U"
                self.y +=1
            self.x += 1
        print("RNA:\n", self.rna)

    def revComp(self):
        """
        reverse complementing method
        """
        for x in range(len(string)):
            self.rev += string[self.z]
            
            if string[self.z] == "A":
                self.revcomp += "T"
                self.z -= -1
            elif string[self.z] == "G":
                self.revcomp += "C"
                self.z -= -1
            elif string[self.z] == "C":
                self.revcomp += "G"
                self.z -= -1
            elif string[self.z] == "T":
                self.revcomp += "A"
                self.z -= -1
            x += 1
        print("reverse complement:\n", "\t\t\t5' -----------------> 3'\n", self.revcomp, "\n", self.rev)

string = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

nuc = 0
sum = 0
base1 = ""

while nuc < 5:
    if nuc == 1:
        base1 = "A"
        A = baseCount(base1, string)
        A.count()
    elif nuc == 2:
        base1 = "G"
        G = baseCount(base1, string)
        G.count()
    elif nuc == 3:
        base1 = "C"
        C = baseCount(base1, string)
        C.count()
    elif nuc == 4:
        base1 = "T"
        T = baseCount(base1, string)
        T.count()

    nuc += 1

sum = A.y + G.y + C.y + T.y
print("\t\t\t", len(string), sum)

rev = rNA = baseCount(base1, string)
rNA.RNA()

rev.revComp()