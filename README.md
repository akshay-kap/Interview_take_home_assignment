# Interview_take_home_assignment
LRU Cache implementation in python 3.7


**Quick-Start:**
  - write'from LRU_cache import LRU' with file LRU_cache.py in your subdirectory
  - refer demo.py to look at use of LRU cache data structure using LRU class

# About

The Class LRU implements LRU cache in python using hashmaps and Doubly linked list.

# Time and Space Complexity



**Demo:**

__code__

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

__Output__

Reloaded modules: LRU_cache
The value of key 1 is [1, 3, 4]
The value of key 2 is [2, 4, 6]
lets update the value of key 2
The value of key 2 is [2, 20, 200]
Adding two more value to see if it delete the last value
The value of key 1 is None
The value of key 2 is [2, 20, 200]
The value of key 3 is 89
The value of key 4 is 33
the size of LRU cache is 3
lets reset the LRU A
the size of LRU cache is 0






