# Hash 原理解釋
## ◆ Hash Table
 是資料結構的一種，利用Hash Function有效率地進行數據搜尋
  1. 先準備用來儲存數據的陣列，再將數據存進去
  2. 遇到數據儲存位置重複 → **Collision 碰撞**                   
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
  5. 輸入完全不同的數據時，即使機率低，但也可能產生相同的雜湊碼，稱為「**Hash Collision雜湊碰撞**」  
     ![photo](https://github.com/stopraining/LearningNote/blob/master/pic/hash3.JPG)
   
# 流程圖
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/hash18.jpg)

# 學習歷程

    先import並測試看看md5~再將他寫成一個function方便之後使用，bucket可以任意輸入想要的大小，也就是capacity

![photo](https://github.com/stopraining/LearningNote/blob/master/pic/hash4.jpg)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/hash6.jpg)

    contains 很重要，就是search的功能，也是檢測data是否存在的function，但我寫得有點亂....但可以work

![photo](https://github.com/stopraining/LearningNote/blob/master/pic/hash8.jpg)
    
    add的部分，我在最前面先寫了一個，如果欲新增的字串已經在裡面的，就不再加入! 如果add的那格是空的可以直接加進去，
    但是如果已經有data的話，就必須往下串所以在測試的時候我找了兩個會被放在同一格的字串("tiffany","wbefbiw"都放在1)，
    再用contain看看"wbefbiw"是否被加入，也順便檢查前面的"tiffany"會不會不小心被覆蓋掉
  
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/hash7.jpg)
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/hash11.jpg)

    刪除的部分，找到欲刪除的值，需全部刪除，但我add的部分已經寫了，重複的data不需再輸入

![photo](https://github.com/stopraining/LearningNote/blob/master/pic/hash9.jpg)

    用助教給的範例測資~
    
![photo](https://github.com/stopraining/LearningNote/blob/master/pic/hash12.jpg)


      





★原理參考資料:          
書籍《演算法圖鑑》                   
http://alrightchiu.github.io/SecondRound/hash-tableintrojian-jie.html#dm              
https://hackmd.io/@EW34LLeXTra2Oikg0WEQ5Q/HJln3jU_e?type=view                 
https://blog.techbridge.cc/2017/01/21/simple-hash-table-intro/                                                                          
https://codereview.stackexchange.com/questions/185638/find-and-delete-an-item-from-a-singly-linked-list-in-python           
https://tbc-python.fossee.in/convert-notebook/Sams_Teach_Yourself_Data_Structures_and_Algorithms_Analysis_in_24_Hours/chapter23_1.ipynb
