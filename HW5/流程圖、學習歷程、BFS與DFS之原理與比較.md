# BFS & DFS
## 原理
### ◆BFS(Breadth-first Search)廣度優先搜尋
* 又稱「寬度優先搜尋」or「橫向優先搜尋」，是一種圖形搜尋演算法
* 屬於盲目搜索(uninformed search)
* 使用**Queue**，通常以遞迴的方式呈現
* 步驟：          
  1. 以某一節點為出發點，先拜訪所有相鄰的節點            
  2. 再依序拜訪與剛才被拜訪過的節點相鄰但未曾被拜訪過的節點          
  3. 直到所有相鄰的節點都已被拜訪過    
               
補充：          
* 盲目搜索:
* Queue佇列:           
  * 加入(Push)與刪除(Pop)在不同端
  * 先進先出(FIFO)
  * EX.排隊、排程
          
  
### ◆DFS(Depth-first Search)深度優先搜尋
* 是一種用於遍歷或搜尋樹或圖的演算法 
* 屬於盲目搜索(uninformed search)
* 利用**Stack**，通常以遞迴的方式呈現
* 步驟：           
  1. 沿著樹的深度遍歷樹的節點，儘可能深的搜尋樹的分支          
  2. 當節點v的所在邊都己被探尋過，搜尋將回溯到發現節點v的那條邊的起始節點。這一過程一直進行到已發現從源節點可達的所有節點為止          
  3. 如果還存在未被發現的節點，則選擇其中一個作為源節點並重複以上過程，整個行程反覆進行直到所有節點都被存取為止         
  
補充：              
* Stack 堆疊:       
  * 加入(Push)與刪除(Pop)在同一端
  * 先進先出(FILO)
  * EX.疊盤子、走迷宮
  
## 比較
# 流程圖
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bfs5.JPG)
# 學習歷程


★參考資料：       
老師上課ppt                  
https://zh.wikipedia.org/wiki/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2       
http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/bfs.html         
https://zh.wikipedia.org/wiki/%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2          
https://www.itread01.com/content/1549064200.html                 





