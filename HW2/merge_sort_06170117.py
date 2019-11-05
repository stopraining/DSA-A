#!/usr/bin/env python
# coding: utf-8

# In[275]:


class Solution(object):
    def merge_sort(self,data):
        
        if len(data) <= 1:
            return data
        else:
            left=[]
            right=[]
            n=0
            for i in data:
                data[n]=i
                if n < (len(data)/2):
                    left.append(i)
                    n+=1
                    left=self.merge_sort(left)
                elif n >= (len(data)/2):
                    right.append(i)
                    n+=1
                    right=self.merge_sort(right)
         
            return self.merge(data,left,right)

    def merge(self,data,left,right):
   
        j=0
        p=0
        q=0
        
        while p <len(left) and q<len(right):
            if left[p] < right[q]:
                data[j] =left[p]
                p+=1
               
            elif left[p] >= right[q]:
                data[j] =right[q]
                q+=1
            j+=1
            
        while p < len(left):
            data[j] =left[p]
            p+=1
            j+=1
        while q< len(right):
            data[j] =right[q]
            q+=1
            j+=1     

        return data


# In[274]:


output=Solution().merge_sort([4,2,8,9,-12,-5])
output


# In[ ]:




