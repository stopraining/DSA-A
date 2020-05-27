#!/usr/bin/env python
# coding: utf-8

# In[238]:


import pandas as pd
data=pd.read_csv("D:/Ting yu 的資料/東吳大學/大三/資訊檢索/hw3_term weighting/train.csv",encoding="utf-8")
data


# In[239]:


import jieba

#斷詞
def chinese_word_cut(mytext): 
    return " ".join(jieba.cut(mytext))


# In[240]:


i=0
data["cut"]=1
while i<len(x['c_content']):
    data["cut"][i]=chinese_word_cut(data['c_content'][i])
    i+=1


# In[241]:


#訓練70%,2032筆
data_train_70=data["cut"][0:2032]
len(data_train_70)


# In[260]:


#停用字
stopword =[]
s=open("stopword.txt",encoding="utf8")
stopword=s.read()
stopword=stopword.split('\n')
stopword


# In[272]:


from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
# 初始化vectorizer, 使用的是bag-of-word 最基礎的 CountVectorizer


vectorizer = CountVectorizer(stop_words=frozenset(stopword))
# 將 text 轉換成 bow 格式
text = vectorizer.fit_transform(data_train_70)
# 實例化(Instantiate) 這個 Naive Bayes Classifier
MNB_model = MultinomialNB()
# 把資料給它，讓這個model根據貝氏定理，去算那些機率。
MNB_model.fit(text, data['i'][0:2032])


# In[273]:


from sklearn.metrics import accuracy_score


# In[274]:


#測試30%,871筆
p1 = vectorizer.transform(data['cut'][2032:])
y_pred=MNB_model.predict(p1)
y_pred


# In[275]:


y_true=data['i'][2032:]
y_true


# In[276]:


accuracy_score(y_true, y_pred)


# In[120]:


test_data=pd.read_csv("D:/Ting yu 的資料/東吳大學/大三/資訊檢索/hw3_term weighting/test.csv",encoding="utf-8")
test_data


# In[121]:


i=0
test_data["cut"]=1
while i<len(test_data['c_content']):
    test_data["cut"][i]=chinese_word_cut(test_data['c_content'][i])
    i+=1


# In[122]:


test_text = vectorizer.transform(test_data['cut'])


# In[124]:


test_pred=MNB_model.predict(test_text)


# In[128]:


test_pred


# In[131]:


pred_finai=[]
for i in test_pred:
    pred_finai.append(i)
    


# In[137]:


pred_finai
len(pred_finai)


# In[139]:


final=pd.read_csv("D:/Ting yu 的資料/東吳大學/大三/資訊檢索/hw3_term weighting/submission_example.csv",encoding="utf-8")
len(final)


# In[140]:


final['i']=pred_finai


# In[141]:


final


# In[142]:


final.to_csv('submission_K.csv')


# In[ ]:




