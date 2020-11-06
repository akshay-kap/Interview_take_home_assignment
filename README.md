# Interview_take_home_assignment
LRU Cache implementation in Python 3.7


**Quick-Start:**
  - write __from LRU_cache import LRU__ with file LRU_cache.py in your subdirectory
  - refer __demo.py__ to look at use of LRU cache data structure using LRU class

# About

The Class LRU implements LRU cache in python using hashmaps and Doubly linked list.

# Methods and attributes
- To Initialize
  - eg: To initialize a LRU Cache of size n (named as A), write the code as
    - A= LRU(n)
        - This intializes a LRU cache with a limit as n with attributes as "_size","_limit","_hash_map","_DLL".
        - "_size" can be used to know the number of elements present in the LRU
        - "_limit" is the capacity of LRU cache i.e. n from the above example
        - "_hash_map" is a python dictionary holding keys of LRU elments as its key and each key of this _hashmap points points to a node of Doubly linked list storing key, value information.
        - "_DLL" is a doubly linkedlist (DLL) storing key, value information. The head of this DLL points to recently added key value pair (via put) and tail of this DLL points to last present element in the LRU cache.
 - put(key, value)
- get(key)
- delete(key)
- reset()

# Time and Space Complexity


# Alternative Implementation appraoches Approches

# Demo

__code__

from LRU_cache import LRU
<br>
A= LRU(3)
<br>
A.put(1,[1,3,4])
<br>
A.put(2,[2,4,6])
<br>
print(f"The value of key 1 is {A.get(1)}")
<br>
print(f"The value of key 2 is {A.get(2)}")
<br>
print("lets update the value of key 2")
<br>
A.put(2,[2,20,200])
<br>
print(f"The value of key 2 is {A.get(2)}")
<br>
print("Adding two more value to see if it delete the last value")
<br>
A.put(3,89)
<br>
A.put(4,33)
<br>
print(f"The value of key 1 is {A.get(1)}")
<br>
print(f"The value of key 2 is {A.get(2)}")
<br>
print(f"The value of key 3 is {A.get(3)}")
<br>
print(f"The value of key 4 is {A.get(4)}")
<br>
print(f"the size of LRU cache is {A._size}")
<br>
print("lets reset the LRU A")
<br>
A.reset()
<br>
print(f"the size of LRU cache is {A._size}")
<br>
__Output__
<br>
Reloaded modules: LRU_cache
<br>
The value of key 1 is [1, 3, 4]
<br>
The value of key 2 is [2, 4, 6]
<br>
lets update the value of key 2
<br>
The value of key 2 is [2, 20, 200]
<br>
Adding two more value to see if it delete the last value
<br>
The value of key 1 is None
<br>
The value of key 2 is [2, 20, 200]
<br>
The value of key 3 is 89
<br>
The value of key 4 is 33
<br>
the size of LRU cache is 3
<br>
lets reset the LRU A
<br>
the size of LRU cache is 0
<br>





