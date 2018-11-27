#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
write a program to compute area of a rectangle
"""


class Rectangle:
    length = 0
    breadth = 0
        
    def __init__(self, length, breadth):
        self.breadth = breadth
        self.length = length
        
       # print(self.length, self.breadth)
    
    def getArea(self):
        area = self.length * self.breadth
        print("the area of the rectangle is:  ", area)
        
    def getPerimeter(self):
        perimeter = 2 * (self.length + self.breadth)
        print ("the perimeter of the rectangle is:  :", perimeter)
        
s = Rectangle(1,3)
s.getArea()
s.getPerimeter()


t = Rectangle(3.5, 35.7)
t.getArea()
t.getPerimeter()