# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 14:30:54 2018

@author: shreyas
"""

"""
Question1:
Write a program that prompts the user to enter a Social Security number 
in the format ddd-dd-dddd, where d is a digit. The program displays Valid
SSN for a correct Social Security number or Invalid SSN otherwise.
"""


SSNinp = input("enter your SSN as XXX-XX-XXXX:  ")

if len(SSNinp) == 11:
    try:                                                                        # testing if user entered numbers
        diff = int(SSNinp[0:3]) + int(SSNinp[4:6]) + int(SSNinp[7:11])          
        if SSNinp[4] == SSNinp[7] :                                             # testing if hyphenation is correct
            #print("correct format")
            ssnstr = SSNinp[0:3] + SSNinp[4:6] + SSNinp[7:11]
            ssn = int(ssnstr)
            print("SSN without hyphen: ",ssn, type(ssn), "\n", SSNinp)                        # validating 
        else:
            print("incorrect hyphenation")
            
        #print(SSNinp[0:3], "\n", SSNinp[4:6], "\n", SSNinp[7:11])
    except: 
        print("invalid entry 1")
        
elif len(SSNinp) == 9:
    try: 
        int(SSNinp)
        print("follow the hyphenation instructions to enter SSN")
    except:
        print("invalid entry 2")
else: 
    print("invalid entry 3")