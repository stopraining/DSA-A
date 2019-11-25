# Hash 原理解釋
## ◆ Hash Table
   是hash function的一個主要應用，使用hash table能夠快速的按照關鍵字尋找資料記錄。                          
   若將**bucket想像成是桌子**，而**slot就是抽屜**，為了要能更快速找到物品，透過Hash Function找到對應的抽屜(Hash Function的功能是指出「第幾個」抽屜，也就是抽屜的index)，就能保證是該Key所要找的物品。反之，如果同一個抽屜裡有兩個以上的物品時，便有可能找錯物品。
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/hash_1.JPG)
   
   

## ◆ Hash Function 
   是一種從任何一種資料中建立小的數字「指紋」的方法。雜湊函式把訊息或資料壓縮成摘要，使得資料量變小，將資料的格式固定下來。該函式將資料打亂混合，重新建立一個叫做雜湊值（hash values，hash codes，hash sums，或hashes）的指紋。雜湊值通常用一個短的隨機字母和數字組成的字串來代表。
### Hash function性質
   * 運算速度快
   * 不可逆性： 無法從雜湊值推回原本的資料是什麼
   * 如果兩個雜湊值是不相同的（根據同一函式），那麼這兩個雜湊值的原始輸入也是不相同的
   * 如果兩個雜湊值是**相同**的（根據同一函式），那麼這兩個雜湊值的原始輸入 **不一定**是相同的 → **Collisions 雜湊衝突**      
   * `Collisions 雜湊衝突`：兩筆資料存進同一個**table**之**slot** → 查詢資料失敗               
      解決方法:                        
           1. Chaining：使用Linked list把「Hashing到同一個slot」的資料串起來。                
           2.Open Addressing：使用Probing Method來尋找Table中「空的slot」存放資料。

    

# 流程圖

# 學習歷程


★參考資料:            
http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html#dm              
https://hackmd.io/@EW34LLeXTra2Oikg0WEQ5Q/HJln3jU_e?type=view                 
https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/                    
http://mail.tsu.edu.tw/~hjsin/courses/DATA/chap8.pdf
