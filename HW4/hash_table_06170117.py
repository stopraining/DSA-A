#!/usr/bin/env python
# coding: utf-8

# In[30]:


class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class MyHashSet:

    def __init__(self, capacity):
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
                cur = self.data[index]
                while (cur.next): 
                    cur = cur.next
                cur.next =  new
            
    def contains(self, key):
        index=self.md5_h(key)
        cur = self.data[index]
        if cur == None:
            return False
        if cur.data == key:
            return True
        elif cur.next != None:
            while (cur.next):
                cur=cur.next
                if cur.data==key:
                    return True
                else:
                    False
        else:
            return False   
        
    def remove(self, key):
        index=self.md5_h(key)
        cur = self.data[index]
        pre = None
        while cur and key != cur.data:
            pre=cur
            cur=cur.next
        
        if not cur:
            return
        if not pre:
            self.data[index]=self.data[index].next
        else:
            pre.next=cur.next
    
        
            


# In[ ]:




