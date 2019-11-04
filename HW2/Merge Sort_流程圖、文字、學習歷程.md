# Merge Sort 合併排序

## ◆文字說明
### 概念:
    將數列分割成等長的2個數，直到無法再分割(每組只剩一個數)，在合併各組數列，並且由小到大排四每組數列，直到最後合併成一個數列
### 我的想法:            
    *Step1.寫一個分割的函式          
    *Step2.寫一個合併的函式
    *Step3.將兩函式做結合
    
## ◆流程圖
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/MergeSort.jpeg)

## ◆學習歷程

    一開始，我先寫合併的函式，而我想到用append的方式，先設兩個list，再將分半的數字分別加進兩個list(left和right)，
    就像第一次作業概念一樣。我先把概念打下來後執行看看     
    
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/1.jpg)             
 
    確定可行後再用函式方式寫出來，且在前面用print，把每一次run的結果印出來，就可以發現List被分裂的過程。
    註:參考別人用:print("splitting",list)           

![photo](https://github.com/stopraining/LearningNote/blob/master/pic/2.jpg)                         
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/3.jpg)  

    再來，我用老師上課交的概念，假設p、q分別為left和right的index，利用while迴圈，使數字排序至新的List→ N，
    並且將分割的函式與此函式做結合
    
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/7.jpg)  
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/4.jpg)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/8.jpg)

    oops，跑出來的結果是錯的！和前面一樣再用print的方式，看看是哪個環節出了問題！

![photo](https://github.com/stopraining/LearningNote/blob/master/pic/9.jpg)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/10.jpg)

    發現問題，雖然有比較數字，將小的放前面，但只是改數字，並非交換，導致數列呈現有重複數字的情形。
    於是，參考了網路上的人寫的(最下方有放參考資料連結)，多加了下面兩段程式碼，以達成交換效果！
    
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/11.jpg)

    成功了！ 結果顯示可以看到交換過程(螢光筆處)
    雖然排序成功了，但要怎麼用class寫呢?? 查了一些網路上的資料還是不太懂，必須請教老師和同學了！

![photo](https://github.com/stopraining/LearningNote/blob/master/pic/12.jpg)
    
    



★程式碼參考資料:                      
https://stackoverflow.com/questions/18761766/mergesort-with-python                                          
https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-8.php




