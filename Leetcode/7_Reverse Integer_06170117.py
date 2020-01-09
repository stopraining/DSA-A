#!/usr/bin/env python
# coding: utf-8

# In[52]:


class Solution:
    def reverse(self, x) :
        if x < -2147483648 or x > 2147483648:
            return 0
        else:
            x=str(x)
            if x[0]=="-":
                x=int('-' + x[-1:0:-1])  
                if x < -2147483648 or x > 2147483648:
                    return 0
                else:
                    return x 
            else:
                x =int(x[::-1]) 
                if x < -2147483648 or x > 2147483648:
                    return 0
                else:
                    return x 
        
                   

