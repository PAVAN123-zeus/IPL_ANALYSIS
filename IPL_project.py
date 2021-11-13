#!/usr/bin/env python
# coding: utf-8

# In[1]:


#loading required librarys.
import pandas as pd
import numpy as np 
import seaborn as sns
from matplotlib import pyplot as plt


# In[2]:


#loading the ipl matches dataset
ipl=pd.read_csv("ipl data.csv")


# In[3]:


#having a glance at the first five records of the dataset
ipl.head()


# In[4]:


#Lookin at the number of rows and columns in the dataset
ipl.shape


# In[5]:


#getting information about data
ipl.info()


# In[6]:


#describing the data
ipl.describe()


# In[7]:


#Getting the frequency of most man of the match awards
ipl["player_of_match"].value_counts()


# In[8]:


#Getting the top 10 players with most man of the match awards
ipl["player_of_match"].value_counts()[0:10]


# In[9]:


#Getting the top 5 players with most man of the match awards
ipl["player_of_match"].value_counts()[0:5]


# In[10]:


list(ipl["player_of_match"].value_counts()[0:5].keys())


# In[11]:


#making a bar-plot for the top 5 players with most man of the match awards
plt.figure(figsize=(8,5))
plt.bar(list(ipl["player_of_match"].value_counts()[0:5].keys()),list(ipl["player_of_match"].value_counts()[0:5]),color="g")
plt.show()


# In[12]:


#Getting the frequency of result column
ipl["result"].value_counts()


# In[13]:


#Finding out the number of toss wins w.r.t each team
ipl["toss_winner"].value_counts()


# In[14]:


#Extracting the records where a team won batting first
batting_first=ipl[ipl["win_by_runs"]!=0]


# In[15]:


#Looking at the head
batting_first.head()


# In[16]:


#Making a histogram 
plt.figure(figsize=(5,5))
plt.hist(batting_first["win_by_runs"])
plt.title("Distribution of Runs")
plt.xlabel("Runs")
plt.show()


# In[17]:


#Finding out the number of wins w.r.t each team after batting first
batting_first["winner"].value_counts()


# In[18]:


#Making a bar-plot for top 3 teams with most wins after batting first
plt.figure(figsize=(6,6))
plt.bar(list(batting_first["winner"].value_counts()[0:3].keys()),list(batting_first["winner"].value_counts()[0:3]),color=["blue","yellow","red"])
plt.show()


# In[19]:


#Making a pie chart
plt.figure(figsize=(7,7))
plt.pie(list(batting_first['winner'].value_counts()),labels=list(batting_first['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[20]:


#extracting those records where a team has won after batting second
batting_second=ipl[ipl["win_by_wickets"]!=0]


# In[21]:


#looking at the head
batting_second.head()


# In[22]:


#Making a histogram for frequency of wins w.r.t number of wicket
plt.figure(figsize=(7,7))
plt.hist(batting_second["win_by_wickets"],bins=30)
plt.show()


# In[23]:


#Finding out the frequency of number of wins w.r.t each time after batting second
batting_second["winner"].value_counts()


# In[24]:


#Making a bar plot for top-3 teams with most wins after batting second
plt.figure(figsize=(7,7))
plt.bar(list(batting_second['winner'].value_counts()[0:3].keys()),list(batting_second['winner'].value_counts()[0:3]),color=["purple","blue","yellow"])
plt.show()


# In[25]:


#Making a pie chart for distribution of most wins after batting second
plt.figure(figsize=(7,7))
plt.pie(list(batting_second['winner'].value_counts()),labels=list(batting_second['winner'].value_counts().keys()),autopct='%0.1f%%')
plt.show()


# In[26]:


#Looking at the number of matches played each season
ipl["season"].value_counts()


# In[27]:


#Looking at the number of matches played in each city
ipl["city"].value_counts()


# In[28]:


#Finding out how many times a team has won the match after winning the toss
np.sum(ipl['toss_winner']==ipl['winner'])


# In[29]:


393/756


# In[ ]:




