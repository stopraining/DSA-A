#!/usr/bin/env python
# coding: utf-8

# In[30]:


class Solution(object):
    def heapsort(self,data):
    
        if len(data)<=1:
            final=[]
            final.insert(0,data.pop(0))
            print("F1",final)     

        else:
            final=[]
            for i in range(len(data)):            #總共要加幾次數字到final裡
                for i in range((len(data)//2)-1,-1,-1):
                    largest=i
                    l=i*2+1
                    r=i*2+2
            
                    if len(data)%2 == 0: #表數列長度為偶數,會有out of range情況需考量
                        if data[l]==data[-1]:
                            if data[largest]<data[l]:
                                 data[largest],data[l]=data[l],data[largest]
                        else:
                            if data[largest]<data[l]:
                                if data[l]>data[r]:
                                    data[largest],data[l]=data[l],data[largest]
                                else:
                                    data[largest],data[l]=data[l],data[largest]
                                    data[largest],data[r]=data[r],data[largest]
                    
                    
                    if  len(data)%2 == 1:         #表數列長度為基數 ,正常運作
                        if data[largest]<data[l]:
                            if data[l]>data[r]:
                                data[largest],data[l]=data[l],data[largest]
                            else:
                                data[largest],data[l]=data[l],data[largest]
                                data[largest],data[r]=data[r],data[largest]
                
                final.insert(0,data.pop(0))
                
                if len(data)>0:
                    N=data[-1]
                    data.insert(0,N)
                    data.pop(-1)
                else:
                    return final       
                
            self.heapsort(data)


# In[32]:


output=Solution().heapsort([2,4,5,-13,1,22,-9])
output


# In[ ]:




