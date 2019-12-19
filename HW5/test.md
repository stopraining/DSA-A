# BFS & DFS
## 原理
### ◆BFS(Breadth-first Search)廣度優先搜尋
* 又稱「寬度優先搜尋」or「橫向優先搜尋」，是一種圖形搜尋演算法
* 屬於盲目搜索(uninformed search)
* 使用**Queue**，通常以遞迴的方式呈現
* **Queue佇列**:           
  * 加入(Push)與刪除(Pop)在不同端
  * 先進先出(FIFO)
  * EX.排隊、排程
* 步驟：          
  1. 以某一節點為出發點，先拜訪所有相鄰的節點            
  2. 再依序拜訪與剛才被拜訪過的節點相鄰但未曾被拜訪過的節點          
  3. 直到所有相鄰的節點都已被拜訪過    

  
### ◆DFS(Depth-first Search)深度優先搜尋
* 是一種用於遍歷或搜尋樹或圖的演算法 
* 屬於盲目搜索(uninformed search)
* 利用**Stack**，通常以遞迴的方式呈現
* **Stack 堆疊**:       
  * 加入(Push)與刪除(Pop)在同一端
  * 後進先出(LIFO)
  * EX.疊盤子、走迷宮
* 步驟：           
  1. 沿著樹的深度遍歷樹的節點，儘可能深的搜尋樹的分支          
  2. 當節點v的所在邊都己被探尋過，搜尋將回溯到發現節點v的那條邊的起始節點。這一過程一直進行到已發現從源節點可達的所有節點為止          
  3. 如果還存在未被發現的節點，則選擇其中一個作為源節點並重複以上過程，整個行程反覆進行直到所有節點都被存取為止         

## 比較
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bfs11.JPG)
# 流程圖
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bfs6.JPG)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bfs10.JPG)
# 學習歷程

    做bfs時，我也是照著跟老師上課畫的流程圖去思考~也是用兩個list的概念~
    為了不要讓數字重複，我思考一下用if的方式排除~有時候只是心想這樣可以吧?~語法有沒有錯? 但竟然可行~
    
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bfs14.JPG)

    用print的方式可以清楚的看到兩個list的變化，再對照自己畫的~ 一模一樣我就放心了~

![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bfs16.JPG)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bfs12.JPG)

    再來，dfs跟bfs只是差別在取的位置而已~ bfs是第0項，dfs是最後一項~
    
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bfs15.JPG)

    同樣的~用print的方式可以清楚的看到兩個list的變化，再對照自己畫的~ 
    
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bfs17.JPG)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bfs13.JPG)

    最後我用了上面流程圖用的測資來測試看看~ 可以對照上面我畫的流程圖~
    
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bfs18.JPG)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bfs19.JPG)

    心得:
    這次作業自己覺得比較沒有花太多時間在上面 ~ 可能跟著老師上課一起畫圖和理解，再寫程式的時候就比較快~
    又或是這次作業比較簡單?? 很開心我完成了~~~~

    
★參考資料：       
老師上課ppt    
書籍《演算法圖鑑》                
https://zh.wikipedia.org/wiki/%E5%B9%BF%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2       
http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/bfs.html         
https://zh.wikipedia.org/wiki/%E6%B7%B1%E5%BA%A6%E4%BC%98%E5%85%88%E6%90%9C%E7%B4%A2          
https://www.itread01.com/content/1549064200.html                 


