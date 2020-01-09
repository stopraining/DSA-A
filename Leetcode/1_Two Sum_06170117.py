#!/usr/bin/env python
# coding: utf-8

# In[27]:


class Solution:
    def twoSum(self, nums, target) :
        ans=[]
        k = 0
        for i in nums:
            n=k+1
            while n<len(nums):
                if nums[k]+nums[n]==target:
                    ans.append(k)
                    ans.append(n)
                
                n+=1
            k+=1
        
        
        return ans

