# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 17:58:35 2020

@author: aksha
"""
import unittest
from LRU_cache import LRU

class TestLRU(unittest.TestCase):

    
    def setUp(self):
        self.LRU1 = LRU(4)
        self.LRU2 = LRU(1)
        self.LRU3 = LRU(0)
    
    # checking for initializing LRU Cache
    def test_init_limit(self):
        self.assertEqual(self.LRU1._limit,4)
        self.assertEqual(self.LRU2._limit,1)
        self.assertEqual(self.LRU3._limit,0)
        
    def test_init_size(self):
        self.assertEqual(self.LRU1._size,0)
        self.assertEqual(self.LRU2._size,0)
        self.assertEqual(self.LRU3._size,0)

    def test_init_hashmap(self):
        self.assertEqual(len(self.LRU1._hash_map),0)
        self.assertEqual(len(self.LRU2._hash_map),0)
        self.assertEqual(len(self.LRU1._hash_map),0)
    
    def test_init_DLL(self):
        self.assertEqual(self.LRU1._DLL.isempty(),True)
        self.assertEqual(self.LRU2._DLL.isempty(),True)
        self.assertEqual(self.LRU3._DLL.isempty(),True)
    
    # Testing put, size, hashmap and DLL    
    
    # testing general cases    
    def test_put_general(self):
        
        self.LRU1.put(1,'One')
        
        self.assertEqual(self.LRU1._size,1)
        self.assertEqual(len(self.LRU1._hash_map),1)
        self.assertEqual(self.LRU1._DLL.isempty(),False)
        self.assertEqual(self.LRU1._DLL._head._key,1)
        self.assertEqual(self.LRU1._DLL._head._value,'One')
        self.assertEqual(self.LRU1._DLL._tail._key,1)
        self.assertEqual(self.LRU1._DLL._tail._value,'One')
        
        
        self.LRU1.put(2,'Two')
        
        self.assertEqual(self.LRU1._size,2)
        self.assertEqual(len(self.LRU1._hash_map),2)
        self.assertEqual(self.LRU1._DLL.isempty(),False)
        self.assertEqual(self.LRU1._DLL._head._key,2)
        self.assertEqual(self.LRU1._DLL._head._value,'Two')
        self.assertEqual(self.LRU1._DLL._tail._key,1)
        self.assertEqual(self.LRU1._DLL._tail._value,'One')
             
        self.LRU1.put(3,'Three')
        
        self.assertEqual(self.LRU1._size,3)
        self.assertEqual(len(self.LRU1._hash_map),3)
        self.assertEqual(self.LRU1._DLL.isempty(),False)
        self.assertEqual(self.LRU1._DLL._head._key,3)
        self.assertEqual(self.LRU1._DLL._head._value,'Three')
        self.assertEqual(self.LRU1._DLL._tail._key,1)
        self.assertEqual(self.LRU1._DLL._tail._value,'One')
        
    def test_put_key_update(self):
        
        self.LRU1.put(1,'One')
        
        self.assertEqual(self.LRU1._size,1)
        self.assertEqual(len(self.LRU1._hash_map),1)
        self.assertEqual(self.LRU1._DLL.isempty(),False)
        self.assertEqual(self.LRU1._DLL._head._key,1)
        self.assertEqual(self.LRU1._DLL._head._value,'One')
        self.assertEqual(self.LRU1._DLL._tail._key,1)
        self.assertEqual(self.LRU1._DLL._tail._value,'One')
        
        
        self.LRU1.put(2,'Two')
        
        self.assertEqual(self.LRU1._size,2)
        self.assertEqual(len(self.LRU1._hash_map),2)
        self.assertEqual(self.LRU1._DLL.isempty(),False)
        self.assertEqual(self.LRU1._DLL._head._key,2)
        self.assertEqual(self.LRU1._DLL._head._value,'Two')
        self.assertEqual(self.LRU1._DLL._tail._key,1)
        self.assertEqual(self.LRU1._DLL._tail._value,'One')
        
        self.LRU1.put(2,'II')
        
        self.assertEqual(self.LRU1._size,2)
        self.assertEqual(len(self.LRU1._hash_map),2)
        self.assertEqual(self.LRU1._DLL.isempty(),False)
        self.assertEqual(self.LRU1._DLL._head._key,2)
        self.assertEqual(self.LRU1._DLL._head._value,'II')
        self.assertEqual(self.LRU1._DLL._tail._key,1)
        self.assertEqual(self.LRU1._DLL._tail._value,'One')
        
                
        self.LRU1.put(3,'Three')
        
        self.assertEqual(self.LRU1._size,3)
        self.assertEqual(len(self.LRU1._hash_map),3)
        self.assertEqual(self.LRU1._DLL.isempty(),False)
        self.assertEqual(self.LRU1._DLL._head._key,3)
        self.assertEqual(self.LRU1._DLL._head._value,'Three')
        self.assertEqual(self.LRU1._DLL._tail._key,1)
        self.assertEqual(self.LRU1._DLL._tail._value,'One')
        
        
        
    # Limit exceeded
    def test_put_limit(self):
        
        self.LRU2.put(1,'I')
        
        self.assertEqual(self.LRU2._size,1)
        self.assertEqual(len(self.LRU2._hash_map),1)
        self.assertEqual(self.LRU2._DLL.isempty(),False)
        self.assertEqual(self.LRU2._DLL._head._key,1)
        self.assertEqual(self.LRU2._DLL._head._value,'I')
        self.assertEqual(self.LRU2._DLL._tail._key,1)
        self.assertEqual(self.LRU2._DLL._tail._value,'I')
        
        
        
        self.LRU2.put(2,'II')
        
        self.assertEqual(self.LRU2._size,1)
        self.assertEqual(len(self.LRU2._hash_map),1)
        self.assertEqual(self.LRU2._DLL.isempty(),False)
        self.assertEqual(self.LRU2._DLL._head._key,2)
        self.assertEqual(self.LRU2._DLL._head._value,'II')
        self.assertEqual(self.LRU2._DLL._tail._key,2)
        self.assertEqual(self.LRU2._DLL._tail._value,'II')
        

    # Edge case
    def test_put_edge(self):
        
        self.LRU3.put(0,'Zero')
        self.assertEqual(self.LRU3._size,0)
        self.assertEqual(len(self.LRU3._hash_map),0)
        self.assertEqual(self.LRU3._DLL.isempty(),True)
        self.assertEqual(self.LRU2._DLL._head,None)
        self.assertEqual(self.LRU3._DLL._tail,None)
        
        self.LRU3.put(0,'o')
        self.assertEqual(self.LRU3._size,0)
        self.assertEqual(len(self.LRU3._hash_map),0)
        self.assertEqual(self.LRU3._DLL.isempty(),True)
        self.assertEqual(self.LRU2._DLL._head,None)
        self.assertEqual(self.LRU3._DLL._tail,None)
        
    
    # testing get for all cases    
    def test_get_general(self):
        
        self.LRU1.put(1,'One')
        self.assertEqual(self.LRU1.get(1),'One')
        self.LRU1.put(2,'Two')
        self.assertEqual(self.LRU1.get(2),'Two')
        self.LRU1.put(2,'II')
        self.assertEqual(self.LRU1.get(2),'II')
        self.LRU1.put(3,'Three')
        self.assertEqual(self.LRU1.get(3),'Three')
        
        
        self.LRU2.put(1,'I')
        self.assertEqual(self.LRU2.get(1),'I')
        self.LRU2.put(2,'II')
        self.assertEqual(self.LRU2.get(2),'II')
        
        self.LRU3.put(0,'Zero')
        self.assertEqual(self.LRU3.get(0),None)
        self.LRU3.put(0,'o')
        self.assertEqual(self.LRU3.get(0),None)
    
    # testing delete
    def test_delete(self):

        self.LRU1.put(1,'One')
        self.assertEqual(self.LRU1.get(1),'One')
        self.assertEqual(self.LRU1._size,1)
        self.assertEqual(len(self.LRU1._hash_map),1)
        self.assertEqual(self.LRU1._DLL.isempty(),False)
        self.assertEqual(self.LRU1._DLL._head._key,1)
        self.assertEqual(self.LRU1._DLL._head._value,'One')
        self.assertEqual(self.LRU1._DLL._tail._key,1)
        self.assertEqual(self.LRU1._DLL._tail._value,'One')
        
        #duplicating the key
        self.LRU1.put(1,'One')
        self.LRU1.delete(1)
        
        self.assertEqual(self.LRU1._size,0)
        self.assertEqual(len(self.LRU1._hash_map),0)
        self.assertEqual(self.LRU1._DLL.isempty(),True)
        self.assertEqual(self.LRU1._DLL._head, None)
        self.assertEqual(self.LRU1._DLL._tail,None)
        
        # deleting duplicate key
        self.LRU1.put(1,'One')
        self.LRU1.put(2,'Two')
        self.LRU1.put(2,'II')
        self.LRU1.delete(2)
        
        self.assertEqual(self.LRU1._size,1)
        self.assertEqual(len(self.LRU1._hash_map),1)
        self.assertEqual(self.LRU1._DLL.isempty(),False)
        self.assertEqual(self.LRU1._DLL._head._key,1)
        self.assertEqual(self.LRU1._DLL._head._value,'One')
        self.assertEqual(self.LRU1._DLL._tail._key,1)
        self.assertEqual(self.LRU1._DLL._tail._value,'One')
        
        self.LRU2.put(1,'I')
        self.LRU2.put(2,'II')
        self.LRU2.delete(1)
        self.assertEqual(self.LRU2._size,1)
        self.assertEqual(len(self.LRU2._hash_map),1)
        self.assertEqual(self.LRU2._DLL.isempty(),False)
        self.assertEqual(self.LRU2._DLL._head._key,2)
        self.assertEqual(self.LRU2._DLL._head._value,'II')
        self.assertEqual(self.LRU2._DLL._tail._key,2)
        self.assertEqual(self.LRU2._DLL._tail._value,'II')
        self.LRU2.delete(2)
        self.assertEqual(self.LRU2._size,0)
        self.assertEqual(len(self.LRU2._hash_map),0)
        self.assertEqual(self.LRU2._DLL.isempty(),True)
        self.assertEqual(self.LRU2._DLL._head,None)
        self.assertEqual(self.LRU2._DLL._tail,None)
        
        
        self.LRU3.put(0,"zero")
        self.LRU3.delete(0)
        self.assertEqual(self.LRU3._size,0)
        self.assertEqual(len(self.LRU3._hash_map),0)
        self.assertEqual(self.LRU3._DLL.isempty(),True)
        self.assertEqual(self.LRU2._DLL._head,None)
        self.assertEqual(self.LRU3._DLL._tail,None)

    def test_reset(self):
        
        self.LRU1.put(1,'One')
        self.LRU1.put(2,'Two')
        self.LRU1.reset()
        self.assertEqual(self.LRU1._limit,4)
        self.assertEqual(self.LRU1._size,0)        
        self.assertEqual(len(self.LRU1._hash_map),0)
        self.assertEqual(self.LRU1._DLL.isempty(),True)
        
        
    def test_all(self):
        
        self.LRU1.put(1,'One')
        self.assertEqual(self.LRU1.get(1),'One')
        self.assertEqual(self.LRU1._size,1)
        self.assertEqual(len(self.LRU1._hash_map),1)
        self.assertEqual(self.LRU1._DLL.isempty(),False)
        self.assertEqual(self.LRU1._DLL._head._key,1)
        self.assertEqual(self.LRU1._DLL._head._value,'One')
        self.assertEqual(self.LRU1._DLL._tail._key,1)
        self.assertEqual(self.LRU1._DLL._tail._value,'One')
        
        self.LRU1.put(2,'Two')
        self.assertEqual(self.LRU1.get(2),'Two')
        self.assertEqual(len(self.LRU1._hash_map),2)
        self.assertEqual(self.LRU1._DLL.isempty(),False)
        self.assertEqual(self.LRU1._DLL._head._key,2)
        self.assertEqual(self.LRU1._DLL._head._value,'Two')
        self.assertEqual(self.LRU1._DLL._tail._key,1)
        self.assertEqual(self.LRU1._DLL._tail._value,'One') 
        
        self.LRU1.put(2,'II')
        self.assertEqual(self.LRU1.get(2),'II')
        self.assertEqual(len(self.LRU1._hash_map),2)
        self.assertEqual(self.LRU1._DLL.isempty(),False)
        self.assertEqual(self.LRU1._DLL._head._key,2)
        self.assertEqual(self.LRU1._DLL._head._value,'II')
        self.assertEqual(self.LRU1._DLL._tail._key,1)
        self.assertEqual(self.LRU1._DLL._tail._value,'One') 
        
        self.LRU1.put(3,'Three')
        self.assertEqual(self.LRU1.get(3),'Three')
        self.assertEqual(self.LRU1._size,3)
        self.assertEqual(len(self.LRU1._hash_map),3)
        self.assertEqual(self.LRU1._DLL.isempty(),False)
        self.assertEqual(self.LRU1._DLL._head._key,3)
        self.assertEqual(self.LRU1._DLL._head._value,'Three')
        self.assertEqual(self.LRU1._DLL._tail._key,1)
        self.assertEqual(self.LRU1._DLL._tail._value,'One')
        
        self.LRU1.put(4,'Four')
        self.LRU1.put(5,'Five')
        self.assertEqual(self.LRU1.get(4),'Four')
        self.assertEqual(self.LRU1.get(5),'Five')
        self.assertEqual(self.LRU1._size,4)
        self.assertEqual(len(self.LRU1._hash_map),4)
        self.assertEqual(self.LRU1._DLL.isempty(),False)
        self.assertEqual(self.LRU1._DLL._head._key,5)
        self.assertEqual(self.LRU1._DLL._head._value,'Five')
        self.assertEqual(self.LRU1._DLL._tail._key,2)
        self.assertEqual(self.LRU1._DLL._tail._value,'II')
        
        self.LRU1.reset()
        self.assertEqual(self.LRU1._limit,4)
        self.assertEqual(self.LRU1._size,0)        
        self.assertEqual(len(self.LRU1._hash_map),0)
        self.assertEqual(self.LRU1._DLL.isempty(),True)
        
        
if __name__=="__main__":
    unittest.main()
