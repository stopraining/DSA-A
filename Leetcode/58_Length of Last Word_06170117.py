#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def lengthOfLastWord(self, s) :
        a=s.split()
        if len(a) !=0:
            return len(a[-1])
        else:
            return 0

