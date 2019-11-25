## Hash 原理解釋
### ◆ Hash Function
1. 什麼是Hash Function?  

        是一種從任何一種資料中建立小的數字「指紋」的方法。雜湊函式 把訊息或資料 (key) 壓縮成摘要，使得資料量變小，將資料的格式固定下來。
    該函式將資料打亂混合，重新建立一個叫做 雜湊值（hash values，hash codes，hash sums，或hashes） 的指紋。這個雜湊值就當作是陣列的索引，
    資料就儲存在這個索引的位置中。雜湊值通常用一個短的隨機字母和數字組成的字串來代表。
    
2.優秀的Hash Function(h())應具備以下特徵：             

        定義h()的定義域(domain)為整個Key的宇集合U，值域(range)應小於Table的大小m：h:U→{0,1,...,m−1},where|U|≫m                       
    盡可能讓Key在經過Hash Function後，在值域(也就是Table的index)能夠平均分佈(uniform distributed)，如此才不會有
    「兩筆資料存進同一個Table空格(稱為slot)」的情況。
    

### ◆ Hash Table

## 流程圖

## 學習歷程


★參考資料:            
http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html#dm              
https://hackmd.io/@EW34LLeXTra2Oikg0WEQ5Q/HJln3jU_e?type=view
