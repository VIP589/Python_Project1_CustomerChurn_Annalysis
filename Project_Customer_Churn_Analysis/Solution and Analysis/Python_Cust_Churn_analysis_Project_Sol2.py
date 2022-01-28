#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[2]:


cd G:\ANTWALK\Python Project\Python Project Solution
    pwd


# In[3]:


cd G:\ANTWALK\Python Project\Python Project Solution


# In[4]:


pwd


# In[5]:


import pandas as pd
df =pd.read_csv('G:\ANTWALK\Python Project\Python Project Solution\Given_Dataset\Customer Attrition Status.csv')
df


# In[6]:


df.shape

df.describe
# In[7]:


df.describe


# In[8]:


df.head(7)


# In[9]:


df.tail(7)


# In[10]:


df.isnull().sum()


# In[11]:


df


# In[12]:


df2 = df[df.isnull().any(axis=1)]
df2


# In[13]:


df2 = df[df.isnull().any(axis=1)]
df2


# In[14]:


df2.dropna(inplace= True)


# In[15]:


df2 = df[df.isnull().any(axis=1)].copy((deep=True)
df2


# In[16]:


import warnings
warnings.filterwarnings('ignore')


# In[17]:


df.isnull().sum()


# In[18]:


df2 = df[df.isnull().any(axis=1)]
df2


# In[19]:


df2.dropna(inplace= True)


# In[20]:


df.isnull().sum()


# In[21]:


df2 = df[df.isnull().any(axis=1)]
df2


# In[22]:


df2.dropna(inplace= True)


# In[23]:


df2 = df[df.isnull().any(axis=1)]
df2


# In[24]:


df3 = df[df.isnull().any(axis=1)]
df3


# In[25]:


df.tail(20)


# In[26]:


df2.dropna
df2


# In[27]:


df = df.dropna(axis=0)
print(df)


# In[28]:


df.describe


# In[29]:


df.tail(20)


# In[30]:


df.isnull().sum()


# In[31]:


df.head(6)


# In[32]:


df


# In[33]:


dfdemog =pd.read_csv('G:\ANTWALK\Python Project\Python Project Solution\Given_Dataset\Customer Demographics.csv')
dfdemog


# In[34]:


dfdemog.tail(20)


# In[35]:


dfdemog.describe


# In[36]:


dfdemog.isnull().sum()


# In[37]:


dfdemog.dropna


# In[38]:


dfdemog.isnull().sum()


# In[39]:


df3 = dfdemog.dropna(axis=0)
print(df3)


# In[40]:


dfdemog


# In[41]:


dfdemog = df3


# In[42]:


df3 =pd.merge(df,dfdemog,on='CustomerId')
df3


# In[43]:


df


# In[44]:


df3


# In[45]:


df3 =pd.merge(df,dfdemog,on='CustomerId',how='left')
df3


# In[46]:


df4= df3.drop(['RowNumber_y'],axis = 1)


# In[47]:


df4


# In[48]:


dfInv1 =pd.read_csv('G:\ANTWALK\Python Project\Python Project Solution\Given_Dataset\Customer Investment Snapshot.csv')


# In[49]:


dfInv1


# In[50]:


dfInv1.describe


# In[51]:


dfInv1.isnull().sum()


# In[52]:


df6 = dfInv1.dropna(CustomerId = 'null')


# In[53]:


df5 = dfInv.dropna(['CustomerId'],axis = 1)


# In[54]:


df5= dfInv1["CreditScore"].fillna(method ='ffill', inplace = True)


# In[55]:


dfInv1.isnull().sum()


# In[56]:


df5= dfInv1["Balance"].fillna(method ='ffill', inplace = True)


# In[57]:


df5= dfInv1["EstimatedSalary"].fillna(method ='ffill', inplace = True)


# In[58]:


df5= dfInv1["Tenure"].fillna(method ='ffill', inplace = True)


# In[59]:


df


# In[60]:


dfInv1.describe


# In[61]:


dfInv1.describe


# In[62]:


dfInv1.isnull().sum()


# In[63]:


df6 = dfInv1.dropna(axis=0)   
print(df6)


# In[64]:


df6.isnull().sum()


# In[65]:


df7 =pd.merge(df4,df6,on='CustomerId',how='inner')


# In[66]:


df7


# In[67]:


df8= df7.drop(['RowNumber'],axis = 1)


# In[68]:


df8


# In[69]:


df8.isnull().sum()


# In[70]:


df8.describe()


# In[71]:


df8.head()


# In[72]:


df8.tail()


# In[73]:


dfPort =pd.read_csv('G:\ANTWALK\Python Project\Python Project Solution\Given_Dataset\Customer Portfolio Snapshot.csv')
dfPort


# In[74]:


dfPort.isnull().sum()


# In[75]:


df9= dfPort["NumOfProducts"].fillna(method ='ffill', inplace = True)


# In[76]:


dfPort.isnull().sum()


# In[77]:


df9= dfPort["HasChckng"].fillna(method ='ffill', inplace = True)


# In[78]:


df9= dfPort["IsActiveMember"].fillna(method ='ffill', inplace = True)


# In[79]:


df10 =pd.merge(df8,dfPort,on='CustomerId',how='inner')


# In[80]:


df10.isnull().sum()


# In[81]:


df10.describe


# In[82]:


df.tail()


# In[83]:


df.head()


# In[84]:


df10


# In[85]:


df11= df10.drop(['RowNumber'],axis = 1)


# In[86]:


df11


# In[87]:


df12 = df11(['CustomerId'].astype(int))


# In[88]:


df12


# In[89]:


df13 = df11.astype({"CustomerId":'int', "EstimatedSalary":'int',"Age":'int',"Tenure":'int',"CreditScore":'int',"Exited":'int'})


# In[90]:


df14 = df13.astype({"HasChckng":'int'})


# In[91]:


df14


# In[92]:


display.df13.dtypes()


# In[94]:


display(df14.dtypes)


# In[96]:


df15 = df14.astype({"EstimatedSalary":'float'})
df15


# In[97]:


display(df15.dtypes)


# In[98]:


df16 = df14.astype({"IsActiveMember":'int'})


# In[99]:


display(df16.dtypes)


# In[100]:


df17 = df14.astype({"NumOfProducts":'int',"EstimatedSalary":'float' })


# In[101]:


df17


# In[102]:


import seaborn as sns


# In[104]:


df17.head()


# In[105]:


df17.rename({("RowNumber_x","RowNumber")})


# In[106]:


df17.corr()


# In[107]:


sns.heatmap(df17.corr())


# In[108]:


sns.jointplot(x='Balance',y='NumOfProducts',data=df17,kind='hex')


# In[109]:


sns.jointplot(x='Balance',y='NumOfProducts',data=df17,kind='reg')


# In[111]:


sns.jointplot(x='IsActiveMember',y='Exited',data=df17,kind='reg')


# In[114]:


sns.pairplot(df17)


# In[116]:


sns.pairplot(df17,hue='Exited')


# In[120]:


sns.distplot(df17['Exited'],kde=False,)


# In[122]:


sns.distplot(df17['IsActiveMember'],kde=False)


# In[124]:


sns.countplot('IsActiveMember',data=df17)


# In[125]:


sns.countplot('Exited',data=df17)


# In[126]:


sns.countplot('CreditScore',data=df17)


# In[127]:


sns.countplot('Tenure',data=df17)


# In[128]:


sns.countplot(y='IsActiveMember',data=df17)


# In[131]:


sns.boxplot(x='Exited',y='IsActiveMember',data=df17)


# In[133]:


sns.boxplot(y='Age',x='IsActiveMember',data=df17)


# In[134]:


sns.boxplot(y='Age',x='NumOfProducts',data=df17)


# In[136]:


sns.boxplot(y='EstimatedSalary',x='NumOfProducts',data=df17)


# In[138]:


sns.violinplot(y='EstimatedSalary',x='NumOfProducts',data=df17)


# In[ ]:




