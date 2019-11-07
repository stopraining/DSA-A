#!/usr/bin/env python
# coding: utf-8

# In[64]:


def heapsort(data):
    final=data
    print(final)
    
    if len(data)<=1:
        num=data.pop(0)
        print("POP",num)
        print(final[0])
        
        final[0]= num
        
      
           

    else:
        for i in range((len(data)//2)-1,-1,-1):
            largest=i
            l=i*2+1
            r=i*2+2
            
            print(largest,l,r)
            
            if len(data)%2 == 0: #數列長度為偶數,會有out of range情況需考量
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
                    
                    
                
            if  len(data)%2 == 1:         #數列長度為基數 ,正常運作
                if data[largest]<data[l]:
                    if data[l]>data[r]:
                        data[largest],data[l]=data[l],data[largest]
                    else:
                        data[largest],data[l]=data[l],data[largest]
                        data[largest],data[r]=data[r],data[largest]
                
                
        
        
        num=data.pop(0)
        print("POP",num)
        
       
       
        
        N=data[-1]      #找出數列最後一個數字把 N
        data.insert(0,N)  #把 N 放在第一個(index=0)
        data.pop(-1)   #再把最後的那個刪掉，不然會重覆
        print("D2",data)
        heapsort(data)  #把調整好的數列再回去上面的函式跑
        
        
        
        
    return final
    
        


# In[66]:


ddd=[2,4,5,3,1,22,-9]
heapsort(ddd)


# In[ ]:




