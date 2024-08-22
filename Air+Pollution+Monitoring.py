
# coding: utf-8

# In[33]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import seaborn as sns
import datetime 
import matplotlib.dates as md


# In[71]:


df=pd.read_csv('/home/user/Air-Pollution-Monitoring-using-IoT-Data-Viz.-ML/pollution.csv')
df.head()


# In[72]:


df.drop("entry_id",axis=1,inplace=True)
df.head()


# In[73]:


#finding out the time when max. pollution occurs at Ghadi Chowk
df[df['Ghadi Chowk']==3.0235897439999997].drop(['Pandri','Mowa'],axis=1)


# In[74]:


#finding out the time when max. pollution occurs at Pandri
df[df['Pandri']==3.0235897439999997].drop(['Ghadi Chowk','Mowa'],axis=1)


# In[75]:


#finding out the time when max. pollution occurs at Mowa
df[df['Mowa']==3.0235897439999997].drop(['Ghadi Chowk','Pandri'],axis=1)


# In[96]:


#finding out pollution level at Ghadi Chowk by hourly update
plt.figure(figsize=(12,8))
plt.rcParams.update({'font.size':15})
x =pd.to_datetime(df['created_at'])
y=df['Ghadi Chowk']
plt.plot_date(x, y)
plt.xlabel("Data & Hour")
plt.ylabel("Pollution Level")
plt.title("Hourly Pollution Level at Ghadi Chowk")


# In[97]:


#finding out pollution level at Pandri by hourly update
plt.figure(figsize=(12,8))
plt.rcParams.update({'font.size':15})
x =pd.to_datetime(df['created_at'])
y=df['Pandri']
plt.plot_date(x, y,color='green')
plt.xlabel("Data & Hour")
plt.ylabel("Pollution Level")
plt.title("Hourly Pollution Level at Pandri")


# In[98]:


#finding out pollution level at Mowa by hourly update
plt.figure(figsize=(12,8))
plt.rcParams.update({'font.size':15})
x =pd.to_datetime(df['created_at'])
y=df['Mowa']
plt.plot_date(x, y,color='red')
plt.xlabel("Data & Hour")
plt.ylabel("Pollution Level")
plt.title("Hourly Pollution Level at Mowa")


# In[95]:


#pairplotting
sns.set(font_scale=1.5)
g=sns.pairplot(df,hue="Ghadi Chowk")
g.fig.set_size_inches(15,15)


# In[108]:


sns.jointplot(x="Ghadi Chowk",y="Pandri",data=df,color='green')


# In[109]:


sns.jointplot(x="Ghadi Chowk",y="Mowa",data=df,color='red')


# In[113]:


sns.jointplot(x="Mowa",y="Pandri",data=df,color='k')

