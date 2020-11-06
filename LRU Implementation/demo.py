# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 17:41:38 2020

@author: aksha
"""
from LRU_cache import LRU

A= LRU(3)

A.put(1,[1,3,4])
A.put(2,[2,4,6])

print(f"The value of key 1 is {A.get(1)}")
print(f"The value of key 2 is {A.get(2)}")

print("lets update the value of key 2")
A.put(2,[2,20,200])
print(f"The value of key 2 is {A.get(2)}")

print("Adding two more value to see if it delete the last value")
A.put(3,89)
A.put(4,33)

print(f"The value of key 1 is {A.get(1)}")
print(f"The value of key 2 is {A.get(2)}")
print(f"The value of key 3 is {A.get(3)}")
print(f"The value of key 4 is {A.get(4)}")
print(f"the size of LRU cache is {A._size}")

print("lets reset the LRU A")
A.reset()
print(f"the size of LRU cache is {A._size}")