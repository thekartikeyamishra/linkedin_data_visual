#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
from IPython.display import display,HTML


# In[6]:


LinkedInConn = pd.read_csv("LinkedInConn.csv", skiprows = 3)
LinkedInConn.shape


# In[7]:


LinkedInConn.head(0)


# In[8]:


LinkedInConn.head(1)


# In[9]:


LinkedInConn.columns


# In[10]:


LinkedInConn.columns= LinkedInConn.columns.str.replace(" ", "_").str.lower()


# In[11]:


LinkedInConn.columns


# In[13]:


LinkedInConn = LinkedInConn[["company", "position", "connected_on"]]


# In[14]:


LinkedInConn.head()


# In[15]:


LinkedInConn.info()


# In[16]:


LinkedInConn[LinkedInConn['company'].isnull()]


# In[17]:


LinkedInConn.dropna(axis="rows", inplace = True)


# In[18]:


LinkedInConn.info()


# In[19]:


LinkedInConn.groupby(by = "connected_on").count().reset_index()


# In[22]:


fig1 = px.line(LinkedInConn.groupby(by = "connected_on").count().reset_index(), x = "connected_on", y= "position", labels = {'position': 'count'},
              title = 'Numbers Of My LinkedIn Connection On Specific Date.', height = 500, width = 800, template = 'none')
fig1.show()


# In[23]:


LinkedInConn.connected_on = pd.to_datetime(LinkedInConn.connected_on)


# In[24]:


LinkedInConn.dtypes


# In[25]:


LinkedInConn['month_name'] = LinkedInConn['connected_on'].dt.month_name()


# In[26]:


LinkedInConn.head()


# In[27]:


LinkedInConn.groupby(by="month_name").count().reset_index()


# In[28]:


fig2 = px.bar(LinkedInConn.groupby(by="month_name").count().reset_index().sort_values(by="connected_on", ascending=False), x = "month_name",
             y = "position", color="month_name", labels = {'postion': 'count'}, title = 'Number Of Connections On A Specific Month',
             height = 450, width = 1000, template = "gridon", text ="company")
fig2.show()


# In[29]:


company_wise = LinkedInConn.groupby(by="company").count().reset_index().sort_values(by="position", ascending=False).reset_index(
    drop = True)


# In[30]:


company_wise.head()


# In[32]:


fig3 = px.bar(company_wise[:15], x = "company", y = "position", color="month_name", labels = {'postion': 'count'}, 
              title = 'Top Companies/ Organizations In My Network',
             height = 450, width = 1000, template = "gridon", text ="position")
fig3.show()


# In[34]:


top_company = LinkedInConn.groupby(by="company").count().reset_index().sort_values(by="position", ascending=False).reset_index(
    drop = True)
top_company.head(2)


# In[36]:


fig5 = px.treemap(top_company[:50], path = ['company', 'position'], values = 'position', template ='ggplot2')
fig5.show()


# In[37]:


top_position = LinkedInConn.groupby(by="position").count().reset_index().sort_values(by="company", ascending=False).reset_index(
    drop = True)
top_position.head()


# In[39]:


fig6 = px.treemap(top_position[:50], path = ['position', 'company'], values = 'company', template ='ggplot2', 
                   labels = {'month_name' : 'count'})
fig6.show()


# In[45]:


top_company = LinkedInConn['company'].value_counts().reset_index()


# In[41]:


top_company.head()


# In[46]:


filtered_top_company = top_company.loc[top_company['company']>=2]
filtered_top_company


# In[53]:


get_ipython().system('pip install pyvis')
import networkx as nx
from pyvis import network as net
import webbrowser


# In[61]:


g = nx.Graph()
g.add_node('root')

for _,row in filtered_top_company.iterrows():
    company = row['index']
    count = row['company']
    title = f"{company}-{count}"
    positions = set(LinkedInConn[company == LinkedInConn['company']]['position'])
    postions1 = "\n".join([i for i in positions])
    hover_info = f"{company}:{postions1}"
    g.add_node(company, size = count*2, title = hover_info, color = '#ffa500')
    g.add_edge('root', company, color = 'yellow')
    
nt = net.Network(height="750px", width="100%", bgcolor = "#222222", font_color = "white")
nt.from_nx(g)
nt.save_graph("Company_graph.html")
webbrowser.open("Company_graph.html")


# In[ ]:




