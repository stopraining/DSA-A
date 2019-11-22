# Binary Search Tree
### 預設:
  * 搜尋方式：pre- order 
  * 修改(刪除)數字 → 全修改(刪除)
  * <= root：放左邊(left child) / > root：放右邊(right child)
  
  
# 流程圖


![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bst10.JPG)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bst9.JPG)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bst7.JPG)

# 學習歷程

    按照助教給的範例程式碼來寫~ 我有參考老師上課教的~ 畫圖邊想邊打code! 
    利用助教在ppt的Q&A裡面提供的測試方法~來檢驗自己有沒有對~
    
    
### ▼Insert
    
    一開始，我先寫insert函式，我覺得比較好去想...
    一步一步畫圖思考
    
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bst1.jpg)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bst4.jpg)    
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bst3.jpg)

    
### ▼Search
    
    原本把return放錯位置，結果一值回傳原本的root給我
    想了很久才放對...

![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bst5.jpg)    
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bst6.jpg)

### ▼Delete

     刪除比較複雜一點，自己寫的時候一直錯，所以參考了網路上的.... 
     當目標刪除節點有兩個子節點時，我選擇從左邊最大的補上來，這樣結構才不會被破壞
     我利用preorder將root印出來，發現我並沒有將兩個3都刪除，只刪到了一個.....
     這個delete失敗:(
   
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bst11.JPG)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bst13.JPG)

### ▼Modify
    
     先利用delete函式將目標刪除，再呼叫insert函式，將欲修改成的值加進來
     但是我delete函式是錯的....所以這個修改函式也不會是正確的...

     
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bst12.JPG)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/bst14.JPG)



    ☆ 心得: 
       delete部分實在太難了...希望有空時，能將delete函式再重新寫過，將各種狀況考慮進去
       這次寫tree也遇到很多困難，但每解決一個都要想很久...
       
   


★程式碼參考資料:                            
https://cppsecrets.com/users/859710057545452565764103109971051084699111109/Python-program-to-delete-an-element-into-AVL-Tree.php        
https://www.itread01.com/content/1542339850.html              
https://www.geeksforgeeks.org/how-to-handle-duplicates-in-binary-search-tree/              
老師上課程式碼                

