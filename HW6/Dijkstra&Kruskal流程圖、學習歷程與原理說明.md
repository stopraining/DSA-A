# Dijkstra & Kruskal
## 原理
### ◆戴克斯特拉 Dijkstra 
解決**最短路徑問題(shortest path problem)** 的演算法，求出從起點到終點之間，邊權重總和最小的路徑
* 作法：
  1. 以某一節點當作出發點，在與其相連且尚未被選取的節點裡，選擇加入離出發點距離最短的節點
  2. 透過新增的節點更新到達其他節點的距離
  3. 重覆加入新節點，直到所有的節點都被加入為止

### ◆克魯斯克爾 Kruskal
是一種用來尋找**最小生成樹(minimum spanning tree)** 的演算法
* 作法:
  1. 將各邊線依權值大小由小到大排列, 接著從**權值最低**的邊開始架構最小的成本擴張樹
  2. 如果加入的邊會造成迴圈則捨棄不用
  3. 直到加了 V-1 個邊為止。**E(邊)=V(點)-1**

## 流程圖
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/dij1.JPG)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/dij2.JPG)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/dij3.JPG)

## 學習歷程

     畫幾次流程圖後，知道要用"inf"的概念，但一開始寫很笨的用了字串，完全無法比較阿，後來才知道float("inf")
     首先最重要的還是要找出最短的距離和index，不要忘了要將它加入已走訪的list!
     
     最難的是距離比較的部分，一開始從無限變數字，就是因為任何數都比無限小，若取到的點可以讓距離更小，就改成該距離

![photo](https://github.com/stopraining/LearningNote/blob/master/pic/dij4.JPG)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/dij5.JPG)

     利用print看結果，可以發現跟上面自已畫的流程圖相符~

![photo](https://github.com/stopraining/LearningNote/blob/master/pic/dij6.JPG)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/dij7.JPG)


★參考資料:                                
https://zh.wikipedia.org/wiki/%E6%88%B4%E5%85%8B%E6%96%AF%E7%89%B9%E6%8B%89%E7%AE%97%E6%B3%95             
https://zh.wikipedia.org/wiki/%E5%85%8B%E9%B2%81%E6%96%AF%E5%85%8B%E5%B0%94%E6%BC%94%E7%AE%97%E6%B3%95         
http://puremonkey2010.blogspot.com/2010/10/kruskal.html            
http://nthucad.cs.nthu.edu.tw/~yyliu/personal/nou/04ds/dijkstra.html
