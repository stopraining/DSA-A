#!/usr/bin/env python
# coding: utf-8

# In[12]:


from collections import defaultdict 

class Graph(): 
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = []  
        
    def Dijkstra(self,s):

        dist = [float("inf")]*len(self.graph)    #距離都先設無限大
        dist[s] = 0     #起點自己到自己的距離為0
        visited = []   #走訪list

        while True:     #一直循環,直到return

            s_d = float("inf")   #設最短距離是無限
            s_i = -1      #設最短index為-1,方便之後判斷是否已結束
            
            for i in range(len(self.graph)):
             
                if dist[i] < s_d and i not in visited:  #當小於無限並且未走訪過
                    s_i= i        #找出最小Index
                    s_d = dist[i]        #找出最小距離
                    
            if s_i == -1:       #最後return dictionary
                ans= {}         
                num=0
                for i in dist:       #把dist裡的數一一印出來
                    ans[str(num)]=i    #加上節點之數字
                    i+=1     
                    num+=1
                return ans
            
            visited.append(s_i)     #已經走訪過的加入visited裡面

            for i in range(len(self.graph[s_i])):
               
                if self.graph[s_i][i] != 0 and self.graph[s_i][i]+dist[s_i]<dist[i]:  #如果此點到各個鄰點的距離有比現在的小
                    dist[i] = self.graph[s_i][i]+dist[s_i]   #就要改成最短距離
        
    def addEdge(self,u,v,w): 
        return None
        
    def Kruskal(self):
        return None
        


# In[ ]:




