#!/usr/bin/env python
# coding: utf-8

# In[19]:


from Crypto.Hash import MD5

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class MyHashSet:

    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity
        
        
    def md5_h(self,x):       
        h=MD5.new()
        h.update(x.encode("utf-8"))
        j=h.hexdigest()
        j=int(h.hexdigest(), 16)
        index=j % self.capacity
        return index
        
    def add(self, key):
        new=ListNode(key)
        index=self.md5_h(key)
        if self.contains(key)==True: 
            return
        else:
            if self.data[index]== None:   
                self.data[index]=new
            else:
                now = self.data[index]   
                while (now.next): 
                    now = now.next
                now.next =  new
            
    def contains(self, key):
        index=self.md5_h(key)
        now = self.data[index] 
        if now == None:      
            return False
        if now.data == key:
            return True
        elif now.next != None:
            while (now.next):
                now=now.next
                if now.data==key:
                    return True
                else:
                    False
        else:
            return False   
        
    def remove(self, key):
        index=self.md5_h(key)
        now = self.data[index]
        ed = None
        
        if self.contains(key)==None:  
            return
        
        while now and key != now.data:
            ed=now
            now=now.next
        
        if not now:
            return
        if not ed:
            self.data[index]=self.data[index].next
        else:
            ed.next=now.next
    
        
            

