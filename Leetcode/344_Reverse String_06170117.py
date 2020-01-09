#!/usr/bin/env python
# coding: utf-8

# In[36]:


class Solution:
    def reverseString(self,s) :
        a = 0
        l=len(s)
        b = l - 1
        while (a < b):
            s[a], s[b] = s[b], s[a]
            a+=1
            b-=1
        return s
            


# In[ ]:




