# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:37:22 2020

@author: Akshay kapoor
"""

# There are three classes defined
# _Node class which explaines that a node consists of key and value data as well as prev and next pointers 
# _DoublyLinkedList class which can be used to implement a doubly Linklist
# LRU class that utilizes Doubly linked list, and hashmaps to mimic functionality of LRU cache 


# Implementation of _Node Class
class _Node:    
    __slots__ = "_value","_key","_next","_prev"
    

    def __init__(self, key, value, next, prev):
        """
        initializes key, value data and, next, prev pointers for a given node
        
        Returns
        ------
        None
        
        """
        
        self._value = value
        self._key = key
        self._next = next
        self._prev = prev
        
# Implementation of _DoublyLinkedList Class        
class _DoublyLinkedList:
    __slots__ = "_head","_tail","_size"      
    
    # initializes head , tail and current size of doubly Linked List
    def __init__(self):
        """
        Description
        -----------
        initializes key, value data and, next, prev pointers for a given node
        
        Returns
        -------
        None.
        """
        self._head = None
        self._tail = None
        self._size = 0
    
    
    def __len__(self):
        """
        Description
        -----------
        Tells the length of Doubly linked list
        
        Returns
        -------
        Integer
        length of Doubly Linked list (i.e. the count of number of nodes present)
        """
        return self._size
    
    def isempty(self):
        """
        Description
        -----------
        Tells if Doubly linked list is empty or not
        Returns
        -------
        Boolean
        True if Linkedlist is empty and False if Linkedlist is non empty
        """
        return self._size==0
    
    def addfirst(self, key, value):
        """
        Parameters
        ----------
        key : key of a given data
        value : value of  a given data
        
        Description
        -----------
        It adds a new node with key and values as passed argument to the begining of the Doubly LinkedList
        
        Returns
        -------
        None.
        """
        # creating new node using _Node class
        newest = _Node(key,value, None, None)
        
        # if Doubly linked List is empty
        if self.isempty():
            self._head = newest
            self._tail = newest
        
        # if Doubly linked List is non-empty           
        else:
            newest._next = self._head
            self._head._prev = newest
            self._head = newest
            
        # Incrementing the size of Doubly linked List  
        self._size += 1
        
        
    def display(self):
        """
        Description
        -----------
        It is used to display key, values stored in nodes of Doubly linked List

        Returns
        -------
        None.
        """
        p = self._head
        
        while p:
            print(p._key," - ", p._value,end=' --> ')
            p = p._next
        print()
        
        
    def removelast(self):
        """
        Description
        -----------
        It is used to remove the node corresponding to last node (tail) of Doubly linked List

        Returns
        -------
        key : key associated with last node
        value : value associated with last node
        """
        
        # return immediately if Doubly linked List is empty
        if self.isempty():
            print('List is empty')
            return
        
        # in case Doubly linked List is non empty
        key,value = self._tail._key, self._tail._value
        
        # if Doubly linked List containes just one node
        if (self._size ==1):
            self._tail = None
            self._head = None
        
        # Doubly linked List contains more than just one node    
        else:
            self._tail = self._tail._prev
            self._tail._next = None
            
        # Decreasing size of Doubly linked List    
        self._size -= 1
        
        return (key,value)
    
    
    def removespecific(self,node):
        """
        Parameters
        ----------
        node : node that needs to be deleted
        
        Description
        -----------
        Removes the specific node in the linked list
        """
        # if node is the only node present in Doubly linked List
        if self._tail== node and self._head ==node:
            self._tail = None
            self._head = None
        
        # if node is the last node in Doubly linked List
        elif self._tail==node:
                node._prev._next = node._next
                self._tail = node._prev
                
        # if node is the first node in Doubly linked List
        elif self._head==node:
                node._next._prev = node._prev
                self._head = node._next
        else:
                node._prev._next = node._next
                node._next._prev = node._prev
                
        # Decreasing size of  Doubly linked List after deletion
        self._size = self._size -1

# Implementation of LRU class, it implements LRU cache      
class LRU:
    
    # following class attributes will be used
    # _size => the present size of LRU cache
    # _limit => the capacity of LRU i.e. maximum number of key value pairs that can be stored in LRU of given limit
    # _hashmap => A dictionary that containes key value pairs, the keys are the given keys and values
    #             Point to corresponding nodes in Doubly Linked Lists
    #_DLL => A doubly linkedlist storing key, value pairs as node data and keeping track of it size, head and tail pointers
    
    __slots__ = "_size","_limit","_hash_map","_DLL"
    

    def __init__(self,max_size):
        """
        Parameters
        ----------
        max_size : Int
    
        Description
        -----------    
        Initializing max_size, size, hashmap and DoublyLinkedList for LRU class  

        Returns
        -------
        None.
        """
        self._limit = max_size
        self._size = 0
        self._hash_map = {}
        self._DLL = _DoublyLinkedList()
    
    # Defining put operation
    def put(self,key, value):
        """
        Parameters
        ----------
        key : key for a given data
        value : value for a given data
        
        Description
        -----------
        It adds key value pair in LRU cache
        It adds / overwrites the key in hashmap
        It adds the node with key value information in Doubly LinkedList
    
        Returns
        ------
        None.
        """
        
        # If the cache reached its limit (edge case when limit is zero)
        if self._limit ==0:
            return
        
        # if cache reached its limit
        if len(self._hash_map) == self._limit:
            # removing last element from hashmap and doubly linkedlist
            last_key,_ = self._DLL.removelast()
            del self._hash_map[last_key]
            # reducing the size of LRU cache
            self._size = self._size -1
        
        # checking if a duplicate element with same key is present already
        # if such element is found its value has to be  overwritten in doubly linkedlist
        try:    
            # deleting the element from hashmap as well as doubly linked list if its key already exists
            node = self._hash_map[key]
            self._DLL.removespecific(node)
            del self._hash_map[key]
            # reducing the size of LRU cache            
            self._size= self._size -1
        except:
            pass
        
        # adding new element at the beginning of Doubly LinkedList
        self._DLL.addfirst(key,value)
        # getting this element pointed by key of hashmap/python dictionary
        self._hash_map[key]=self._DLL._head
        # increasing the size of LRU cache
        self._size= self._size +1
    
    def get(self, key):
        """
        Parameters
        ----------
        key : the requested key
        
        Description
        -----------
        It finds the value associated with the request key and returns the value
        Returns
        -------
        If key is present : The value data associated with the key
        if key is not present : It does not return anything
        """        
        # checks if the key is presnt in hashmap /dictionary
        try:
            node = self._hash_map[key]
            # returns the value associated with that node
            return node._value
        # if key is not present in the dictionary it return None, as no key is a no-op
        except :
            pass
    
    def delete(self,key):
        """
        Parameters
        ----------
        key : the requested key
        
        Description
        -----------
        Deletes the key and associated value from hashmaps as well as doubly linkedlist        

        Returns
        -------
        None.
        """
        # looks for key in the hashmap 
        try:
            # if key is present in the hashmap
            node = self._hash_map[key]        
            # it removes the correponding node form the doubly linked list
            self._DLL.removespecific(node)
            # it remove the correspinding key form the hashmap
            del self._hash_map[key]
            # reduces the current size of LRU cache 
            self._size = self._size-1

        # if key is not found it returns None, as its a no-op
        except:
            pass
        
    def reset(self):
        """
        Description
        -----------
        It resets the LRU cache as an empty data structure
        It resets the hashmap back to an empty dictinary
        It resets the Doubly linked list back to an empty Linked list

        Returns
        -------
        None.
        """
        del self._hash_map
        self._hash_map ={}
        self._DLL = _DoublyLinkedList()
        self._size =0
        

    
    


