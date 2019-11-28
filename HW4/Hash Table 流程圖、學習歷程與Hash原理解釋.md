# Hash 原理解釋
## ◆ Hash Table
 是資料結構的一種，利用Hash Function有效率地進行數據搜尋
  1. 先準備用來儲存數據的陣列，再將數據存進去
  2. 遇到數據儲存位置重複 → **(collision 碰撞)**                   
  3. 發生碰撞時的處理方法，例如：
     * **Chaining 鏈結法**：利用列表將數據接續在已存入數據後面    
     * **Open Addressing開放定址法**：求出第二候補位址(陣列中的位置)並儲存，如果該位置已滿，繼續找下一個候補位址，直到找到空的位址
  4. 雜湊表的陣列：              
     **規模太小**→ 導致碰撞次數增加，容易產生需要線性搜尋的情況                   
     **規模太大**→ 會產生許多未儲存數據的空箱，造成記憶體空間浪費
     
  5. **Division Method**：利用Modulus(mod)取**餘數**                   
    優點：速度快，只要做一次除法運算
     ![photo](https://github.com/stopraining/LearningNote/blob/master/pic/hash2.JPG)
     

## ◆ Hash Function (雜湊函數)
  是把輸入的數據轉換成固定長度的不規則的值的函數，輸出的不規則職稱為「雜湊碼(Hash Code)」
### Hash Function 特徵
   1. 即使輸入非常大的數據，輸出的雜湊碼的數據長度**不變**                    
   2. 輸入相同的值必定會產生**相同的**輸出值               
   3. 即使輸入的數據很相似，只要有一位元的差異，輸出值就會相差甚遠，輸入類似的數據，也不代表會產生類似的雜湊碼                         
   4. 不可逆性：雜湊碼到推倒推出原始數據是不可能                    
   5. 輸入完全不同的數據時，即使機率低，但也可能產生相同的雜湊碼，稱為「**Hash Collision雜湊碰撞 **」    
   
                       
                
   

    

# 流程圖

# 學習歷程


★參考資料:            
http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html#dm              
https://hackmd.io/@EW34LLeXTra2Oikg0WEQ5Q/HJln3jU_e?type=view                 
https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/                    
http://mail.tsu.edu.tw/~hjsin/courses/DATA/chap8.pdf                
書籍《演算法圖鑑》
