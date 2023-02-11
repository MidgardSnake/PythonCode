#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 15:30:51 2022

@author: lui

Gruppe 10 
HA 05 
"""


#Aufgabe 5.1 

#mix = [51, "Q", {"hallo" : "hello", "Welt" : "world"}, -1, 1, False, "apfel"]
mix = [51, 0, "Q", "LISTE", 4.3, {"null" : 0, "eins" : 1, "zwei" : 2}, -1, "Tupel", 1, "False", 3 > 5, "hell", 666, "dictionaries", True, 42.42]
res = []

# START TODO ###################
ints, double, string, dicts = [], [], [], [] 

for val in  mix :
    if type(val) == int: 
        ints.append(val)
    elif type(val) == float: 
        double.append(val)
    elif type(val) == str:
        string.append(val)
    elif type(val) == dict: 
        dicts.append(val)
    elif type(val) == bool: 
        break;
    
res = sum(ints + double)
# END TODO #####################

print("Sortierte Listen: ")
print(ints)
print(double)
print(string)
print(dicts)
print(res)

