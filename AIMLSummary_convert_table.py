#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas


# In[3]:


loc = "AIMLSummary_06082022_ForKunal_CSV2.csv"


# In[9]:


df1=pandas.read_csv(loc)


# In[10]:


nodes = dict() #create dictionary to store the ID of classification nodes
i = 1 #keep a counter to assign node ID


# In[11]:


cols=[list() for num in range(len(df1.columns))]


# In[12]:


col_names=df1.columns


# In[13]:


df1 = df1.reset_index()  # make sure indexes pair with number of rows
for index, row in df1.iterrows():
    if row[col_names[0]]+str(0) not in nodes.keys() and not pandas.isna(row[col_names[0]]):
        nodes[row[col_names[0]]+str(0)]=[i, [0]]
        cols[0].append(0)
        cols[1].append(i)
        cols[2].append(row[col_names[0]])
        i=i+1
    for num in range(1, len(col_names)):
        if not pandas.isna(row[col_names[num]]): 
            backstep=1
            while num-backstep>=0 and pandas.isna(row[col_names[num-backstep]]):
                backstep=backstep+1
            if num-backstep<0:
                p=0
            else:
                p=nodes[row[col_names[num-backstep]]+str(num-backstep)][0]
            if row[col_names[num]]+str(num) not in nodes.keys(): 
                nodes[row[col_names[num]]+str(num)]=[i, [p]]  
                cols[0].append(p)
                cols[1].append(i)
                cols[2].append(row[col_names[num]])
                i=i+1
            elif p not in nodes[row[col_names[num]]+str(num)][1]:
                nodes[row[col_names[num]]+str(num)][1].append(p)
                cols[0].append(p)
                cols[1].append(nodes[row[col_names[num]]+str(num)][0])
                cols[2].append(row[col_names[num]])


# In[17]:


d = {'ParentID':cols[0], 'ChildID':cols[1], 'Name':cols[2]}
df = pandas.DataFrame(data = d)
df.head(15)


# In[19]:


df.to_csv("AIMLSummary_converted.csv", index=False)


# In[18]:


df.tail(15)


# In[ ]:




