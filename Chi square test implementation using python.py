#!/usr/bin/env python
# coding: utf-8

# In[14]:


import seaborn as sns
import numpy as np
import pandas as pd
dataset=sns.load_dataset('tips')


# In[15]:


dataset.head()


# In[16]:


dataset_table=pd.crosstab(dataset['sex'],dataset['smoker'])


# In[17]:


dataset_table


# In[18]:


dataset_table.values


# In[19]:


Observed_Values = dataset_table.values
print("Observed Values :-\n",Observed_Values)


# In[ ]:




