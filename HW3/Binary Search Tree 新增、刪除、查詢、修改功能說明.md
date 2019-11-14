# Binary Search Tree 功能說明
### 什麼是binary search tree??
   * 又稱 有序二元樹 或 排序二元樹
   * 樹狀結構，將數據儲存於各個節點
   * 若任意節點的左、右子樹不空，左子樹所有節點的值會小於等於其根節點，右子樹所有節點的值會大於其根節點 (**以遇到同樣的數放左邊為例**)
   * 有新增、刪除、查詢、修改之功能

![photo](https://github.com/stopraining/LearningNote/blob/master/pic/a.jpg)                           
(圖片來源:https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9)

## 查詢
   * 可透過下列查詢方式，遇到比目標數字大的節點時，繼續往下找                     
   * 查詢方式：           
       **pre-order**前序 ：順序是：根、左子樹、右子樹，根排在前面                              
       **In-order**中序 ：順序是：左子樹、根、右子樹，根排在中間                                      
       **Post-order**後序：順序是：左子樹、右子樹、根，根排在後面                         
       
       ![photo](https://github.com/stopraining/LearningNote/blob/master/pic/c.JPG)
     
    補充：以上三種遍歷，使用的是「depth-first search 深度優先查詢」，其目的是從起點抵達指定頂點(目標頂點)，在搜尋頂點時，
         先探查單一路徑，直到無法繼續前進，在折返探查下一個選項路徑
       
## 新增
   * 若要新增節點N到樹T中:                           
     * 當樹T是空值，則直接將節點N新增至樹T                    
     * 若不是：                           
       i.當節點N <= 樹T之根節點 →將節點N插入 *左* 子樹之葉子節點                       
       2.當節點N  > 樹T之根節點 →將節點N插入 *右* 子樹之葉子節點
   
## 刪除


## 修改



參考資料:              
https://zh.wikipedia.org/wiki/%E4%BA%8C%E5%85%83%E6%90%9C%E5%B0%8B%E6%A8%B9                                  
http://www.csie.ntnu.edu.tw/~u91029/BinaryTree.html  
https://algorithm.yuanbin.me/zh-tw/basics_data_structure/binary_tree.html#python                        
書籍 《演算法圖鑑》    

