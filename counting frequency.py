# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 22:20:22 2018

@author: shreyas
"""

x = 0

numbers = []

count = input("how many numbers do you want to enter?\t\t")

while x < int(count):
    userinp = input(" enter a number:\t\t")
    numbers.append(int(userinp))
    x += 1

unique = set(numbers)       		

for num in unique:                  
    y = count = 0
    for y in range(len(numbers)):
        if numbers[y] == num:
            count += 1
    print(num, "::", count)

print(numbers, "\n", unique, x, y)
