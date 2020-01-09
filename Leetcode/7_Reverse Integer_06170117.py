#!/usr/bin/env python
# coding: utf-8

# In[51]:


class Solution:
    def reverse(self, x) :
        x=str(x)
        if x[0]=="-":
            x=int('-' + x[-1:0:-1])  
        else:
            x =int(x[::-1])       
                  
        return x                  


# In[ ]:




