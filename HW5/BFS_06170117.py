#!/usr/bin/env python
# coding: utf-8

# In[15]:


from collections import defaultdict 

class Graph:
      
    def __init__(self): 
        self.graph = defaultdict(list) 
    
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
        
    def BFS(self, s):
        state1=[s]    #state1為暫時存放，先把頂點丟進去
        state2=[]     #state2為確定排序

        
        while len(state2)<len(self.graph):   #利用迴圈,如果state2的長度<圖的節點個數,就跑迴圈
            a=state1[0]     #a=state1的第0項
            state2.append(a)    #把a加在state2
            state1.pop(0)    #把state1的第0項刪掉
           
            for i in self.graph[a]:   #跑迴圈,找到節點後面接的節點
                if (not i in state1) and (not i in state2):  #如果已經在state1或state2裡面,就不要再加進來,以免重複
                    state1.append(i)   #將沒有重複的值,加進state1
                    
             
      
        return state2
    
    
    def DFS(self, s): 
        stack=[s]    #stack為暫時存放,先把頂點丟進去
        answer=[]     #answer為確定排序
         
       
            
        while len(stack)>0:   #利用迴圈,如果stack長度>0,表示裡面還有東西,就跑迴圈
            a=stack[-1]     #a=stack的最後一項
            answer.append(a)    #把a加在answer
            stack.pop(-1)    #把stack的最後一項刪掉
            
            for i in self.graph[a]:   #跑迴圈，找到節點後面接的節點
                if (not i in stack) and (not i in answer):  #如果已經在stack或answer裡面,就不要再加進來,以免重複
                    stack.append(i)  #將沒有重複的值,加進stack
                    
              
        return answer
    
        
    

