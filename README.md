# Interview_take_home_assignment
LRU Cache implementation in Python 3.7

## Table of Contents

* [About the Project](#About)
  * [Quick-start](#Quick-Start)
* [Necessary Files](#File-Checks)
* [Performance](#Performance-of-LRU-cache-implementation)
* [Methods and Attributes](#Methods-and-attributes)
* [Demo](#Demo)


# About
A Least Recently Used (LRU) Cache organizes items in order of use, allowing you to quickly identify which item hasn't been used for the longest amount of time.
The Class LRU implements LRU cache in python using hashmaps and Doubly linked list.
## Quick-Start:
  - write __from LRU_cache import LRU__ with file LRU_cache.py in your subdirectory
  - refer __demo.py__ to look at use of LRU cache data structure using LRU class

# File-checks
- [x] LRU_cache.py featuring basic LRU_cache implementation.
- [x] demo.py featuring typical use of LRU_chache.
- [x] test_LRUcache.py featuring 12 unittests for LRU cahce implementation.
- [x] Updated readme.md

# Performance-of-LRU-cache-implementation

- Strengths:
  - *Fast access:* LRU caches store items in order from most-recently used to least-recently used. That means both can be accessed in O(1)O(1) time.
  - Super fast updates: Each time an item is accessed, updating the cache takes O(1)O(1) time.

- Weaknesses:
  - *Space heavy:* An LRU cache tracking nn items requires a linked list of length nn (key, value in each node), and a hash map holding nn items. That's O(n)O(n) space, but it's still two data structures (as opposed to one).


# Methods-and-attributes

- To Initialize
  - eg: To initialize a LRU Cache of size n (named as A), write the code as
    - A= LRU(n)
  - This intializes a LRU cache with a limit as __n__ with attributes as "_size","_limit","_hash_map","_DLL".
  - "_size" can be used to know the number of elements present in the LRU
  - "_limit" is the capacity of LRU cache i.e. n from the above example
  - "_hash_map" is a python dictionary holding keys of LRU elments as its key and each key of this _hashmap points points to a node of Doubly linked list storing key, value information.
  - "_DLL" is a doubly linkedlist (DLL) storing key, value information. The head of this DLL points to recently added key value pair (via put) and tail of this DLL points to last present element in the LRU cache.

- put(key, value)
  - To put a key, value pair in LRU cache, write code as:
   - A.put(1,[1,3,4]) // here key is 1 and value is  [1,3,4]
   
- get(key)
  - To get value of a key, write code as
   - A.get(1) // it will return value as [1,3,4]
   
- delete(key)
  - to delete a key, write code as,
  - A.delete(1) // it will delete the key and assciated value from LRU cache()
  
- reset()
  - to reset a LRU cache, write code as,
  - A.reset() // this will reset the LRU cache

# Alternative Implementation appraoches Approches

# Demo

__Code__ and __Output__
<br> The code and the output shown here
 
<code> from LRU_cache import LRU
</code> 
<br>
<br>
<code> A= LRU(3)
</code> 
<br>
<code> A.put(1,[1,3,4])
</code> 
<br>
<code> A.put(2,[2,4,6])
</code>
<br>
<br>
<code> print(f"The value of key 1 is {A.get(1)}")
</code> 
<br>
*output*: The value of key 1 is [1, 3, 4]
<br> 
<code> print(f"The value of key 2 is {A.get(2)}")
</code>
<br>
*output:* The value of key 2 is [2, 4, 6]
<br>
<br>
// lets update the value of key 2 //
<br>
<code> A.put(2,[2,20,200])
</code>
<br>
<br>
<code> print(f"The value of key 2 is {A.get(2)}")
</code>  
*output:* The value of key 2 is [2, 20, 200]
<br>
<br>
//Adding two more value to see if it delete the last value//
<br>
<code> A.put(3,89)
</code>
<br>
<code> A.put(4,33)
</code>
<br>
<br>
<code> print(f"The value of key 1 is {A.get(1)}")
</code>
<br>
*output*: The value of key 1 is None
<br> 
<code> print(f"The value of key 2 is {A.get(2)}")
</code> 
<br> 
*output*: The value of key 2 is [2, 20, 200]
<br> 
<code> print(f"The value of key 3 is {A.get(3)}")
</code>
<br>
*output*: The value of key 3 is 89
<code> print(f"The value of key 4 is {A.get(4)}")
</code>
<br>
*output*: The value of key 4 is 33
<br>  
<code> print(f"the size of LRU cache is {A._size}")
</code> 
<br>
*output* the size of LRU cache is 3
<br> 
<br>
// lets reset the LRU A //
<br>
<code> A.reset()
</code>
<br>
<br>
<code> print(f"the size of LRU cache is {A._size}")
</code>
<br>
<br>
*output:* the size of LRU cache is 0






