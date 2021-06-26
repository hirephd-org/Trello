#!/usr/bin/env python
# coding: utf-8

# In[1]:


from trello import TrelloClient #load package


# In[2]:


import pandas as pd


# In[3]:


client = TrelloClient(
  api_key= "",     #your trello key
     token= "" ,             #your api token
) #access my trello account


# In[4]:


all_boards = client.list_boards()


# In[5]:


events_board=all_boards[1] #get events board


# In[6]:


events_board #check to see if events_board variable shows the events board on trello


# In[7]:


for lists in events_board.list_lists():
    print(lists) #see the list from the events board


# In[8]:


wrapup_list = events_board.list_lists()[-4]#get the "wrap up" list


# In[9]:


for card in wrapup_list.list_cards():
    print(card) #see all the cards in the


# In[10]:


patent_card=wrapup_list.list_cards()[1] #check the patent card


# In[11]:


for cl in patent_card.fetch_checklists():
    print(cl.name) #see all the names of the checklists in the patent card


# In[12]:


a=[]
for cl in patent_card.fetch_checklists():
    df1=pd.DataFrame(cl.items)
    a.append(df1[['name']])
    #print(df1[['name']]) #print name of checklist and items
a


# In[13]:


d=[]
for cl in patent_card.fetch_checklists():
    d.append(cl.name)
    df2=pd.DataFrame(d, columns=['Checklist']) #get names of checklist
df2 #view all names of checklists 


# In[14]:


conceptual=a[0] #view checklist for "Conceptual" checklist
conceptual


# In[15]:


wrap_up=a[11] #view checklist for "Event wrap up" checklist
wrap_up


# In[ ]:





# In[ ]:




