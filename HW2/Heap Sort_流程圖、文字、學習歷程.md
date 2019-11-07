# Heap Sort 堆積排序
## ◆文字說明
* 二元數的一種
### 概念:
    將數列以樹狀結構呈現，每一個節點有兩個子節點，若子節點的數比該節點大，則交換位子，直到不用在變動時，將最上層的數抽出來，
    再把最後一個節點的數補上去最上層，重複比較，直到將所有的數字抽出，完成排序
    
### 我的想法：
    step1.先把數列變成heap的結構
    step2.比較後，用pop的方式把最大的數字抽出來，再用insert和pop把最後的一個放到數列第一個，然後刪掉最後一個，再丟回函是裡面跑
    step3.把抽出來的數字放在一個新的list，並且將每次抽出來的數字放進來時，都放在第一個(因為我是先抽出大的數字 MAX HEAP)

## ◆流程圖
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/HeapSort.jpeg)

## ◆學習歷程
    
    因為時間上來不及，就不附上我前幾次修改的過程了!我一樣是用print的方式來看看程式碼跑得是不是我要的邏輯，
    
    ● 原本依照老師上課說的，是要從上面比到下面，但其實那樣有要再「重複比較」的可能，為了省去不必要的麻煩，
    我讓它從下面比上來，這樣每run一次，我就能確保最大的在最上面了!
    
    其中像是要考慮會跑出out of range的情況，讓我思考了一下，的確是我一開始沒想到的問題！
    
    現在遇到的難題是，雖然數字都抓對了，但是沒辦法把他們同時放在新list裡面.......
   
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/17.jpg)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/18.jpg)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/20.jpg)

    Finally!!!!!!!!!!                 
    我少加一個迴圈! 要抽幾個數字到新的list就要跑幾次~
    原本有out of range的問題，是因為到最後data裡面沒有數字了，是個空的List~跑data[-1]的動作就會出現錯誤，
    所以我讓data長度大於0時，繼續動作，否則直接回傳結果final
    假使一開始data的長度只有1的話，代表不需比較，加入final後，直接回傳final
    

![photo](https://github.com/stopraining/LearningNote/blob/master/pic/22.jpg)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/23.jpg)

    △寫heap sort真是個艱辛的過程啊~!!!每寫一點，就會遇到一點難關卡住，不過一次又一次地解決了! 終於完成了~ 真的是絞盡腦汁啊!
      使用迴圈上有時候還是會讓我當機，不過階段式print能幫助我理解~
      感謝助教耐心批改!排版有點亂請見諒><


程式碼參考資料:                            
https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-17.php
