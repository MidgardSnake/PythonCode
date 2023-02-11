#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 13:21:31 2022

@author: lui
"""




class Point: 
    count = 0

    def __init__ (self, x, y ):
        
        self.x = x
        self.y = y
        type(self).count += 1 
        
    def __del__(self): 
        type(self).counter -=1 
        
        
#bewegt den alten Wert von x;y um die entsprechenden Übergabewerte
    def move (self, x, y ): 
        self.x = self.x + x 
        self.y = self.y + y 
        
    def coincide(self, Point): 
        if (self.x == Point.x and self.y == Point.y) : 
            return True
        else: 
            return False 
        
    def __str__(self): 
        return (f"Punkt bei ({self.x},{self.y}) ")
        
class Circle (Point): 
    
    def __init__ (self, x ,y ,radi): 
        super().__init__(x,y) 
        self.radi = radi 
        
        
    def coincide(self, Point ): 
        if (self.x + self.radi <= self.x or self.x - self.radi <=self.x)and (self.y+self.radi <= self.y or self.y-self.radi <= self.y) : 
            return True 
        else: 
            return False 
        
    def __str__(self): 
        return (f"Kreis bei ({self.x},{self.y},{self.radi}) ")
    
class LineSeg: 
    
    def __init__ (self, Point1, Point2 ): 
        self.Point1 = Point1 
        self.Point2 = Point2 
        
    def p_on_line(self, PointCheck): 
        deltaY = self.Point2.y  - self.Point1.y
        deltaX = self.Point2.x - self.Point1.x
        
        m = deltaY /deltaX 
        
        b = self.Point1.y - (m * self.Point1.x )
        
        if (PointCheck.y == (m*PointCheck.x)+ b) : 
            return True 
        else: 
            return False 
        
    def __str__(self): 
        return (f"Anfangspunkt bei ({self.Point1.x},{self.Point1.y}) und Endpunkt bei ({self.Point2.x},{self.Point2.y}) ")
        
    
        
        
        
    
        
    
      
        
   
        
    