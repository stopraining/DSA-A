#!/usr/bin/env python
# coding: utf-8

# In[18]:


class Solution:
    def removeElement(self, nums, val) :
        n=0
        for i in range(len(nums)):
            if(nums[i]!=val):
                nums[n]=nums[i]
                n+=1
        return n

