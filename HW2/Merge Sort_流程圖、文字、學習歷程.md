# Merge Sort 合併排序

## ◆文字說明
### 概念:
    將數列分割成等長的2個數，直到無法再分割(每組只剩一個數)，在合併各組數列，並且由小到大排四每組數列，直到最後合併成一個數列。
### 我的想法:            
    *Step1.寫一個分割的函式
    *Step2.寫一個合併的函式
    *Step3.將兩函式做結合
    
## ◆流程圖
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/MergeSort.jpeg)

## ◆學習歷程

    *一開始，我先寫合併的函式，而我想到用append的方式，先設兩個list，再將分半的數字分別加進兩個list,就像第一次作業概念一樣。我先把概念打下來後執行看看。        
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/1.jpg)                 
    * 確定可行後再用函式方式寫出來，且在前面用print，把每一次run的結果印出來(參考別人用:print("splitting",list)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/2.jpg)                         
    * 可以發現List被分裂的過程
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/3.jpg)  
    
    



★程式碼參考資料:                      
https://stackoverflow.com/questions/18761766/mergesort-with-python                                          
https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-8.php




