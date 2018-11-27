# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 12:09:45 2018

@author: shreyas
"""

"""
Some Web sites impose certain rules for passwords. Write a function that checks 
whether a string is a valid password.

Suppose the password rules are as follows:
A password must have at least eight characters.
A password must consist of only letters and digits.
A password must contain at least two digits.

Write a program that prompts the user to enter a password and displays valid 
password if the rules are followed or invalid password otherwise

"""



import re
import time

# using regular expressions

def pwdcheck(password):
    if len(password) <= 9 and re.search("[a-z|0-9]", password) and re.search("[0-9]{2}",password):  #searches only for two consecqutive numbers
        s.stop()
        s.getElapsedTime()
        print("valid password")
    else:
        print("\n\n \t wrong \n\n")





#not using regular expressions

def pwd(password):
    y = 0
    
    # this condition tests if the string is alpha-numeric, and not only alphabetical, 
    # and 8 characters or less
    
    if password.isalnum()==True and password.isalpha()==False and len(password) <=9:
    
        # this loop traverses the string
        for x in range (len(password)):
            
            # this condition evaluates that each 
            
            if password[x].isalpha() == False:
                #print(password[x], x, y, "test 1")
                y += 1
                        
            #print(password[x], x,y, "test 2")

            x += 1
            
        if y >= 2:
            print("You have successfully entered a password with at least two numbers.")
            s.stop()
            s.getElapsedTime()
        else:
            print("You have successfully entered a password with at least one number.")
            
    else: 
        print("Invalid password. Reenter.")


class StopWatch:
	"""
	this class is to measure the difference in computation time between different approaches.
	"""
	
    startTime = 0
    endTime = 0
    elapsed = 0
    
    
    def start(self):
        self.startTime = time.time()
    
    def stop(self):
        self.endTime = time.time()
    
    def getElapsedTime(self):
        elapsed = self.endTime - self.startTime
        print(elapsed, "ms")
        
s = StopWatch()

password = input("Enter a password string \t : \t ")
    
choose = input("do you want to use regular expressions (type R) or not (type N) \t\t:")

s.start()

    
if choose == "R":
    pwdcheck(password)
elif choose == "N":
    pwd(password)
else:
    print("enter R or N (case sensitive; start over)")
