#!/usr/bin/env python
# coding: utf-8

# In[58]:


import scipy.stats as stats


# In[59]:


import seaborn as sns
import numpy as np
import pandas as pd
dataset=sns.load_dataset('tips')


# In[60]:


dataset.head()


# In[61]:


dataset_table=pd.crosstab(dataset['sex'],dataset['smoker'])


# In[62]:


dataset_table


# In[63]:


dataset_table.values


# In[64]:


Observed_Values = dataset_table.values
print("Observed Values :-\n",Observed_Values)


# In[65]:


val=stats.chi2_contingency(dataset_table)


# In[66]:


val


# In[67]:


Expected_Values=val[3]


# In[68]:


Observed_Values=val[3]


# In[69]:


no_of_rows=len(dataset_table.iloc[0:2,0])


# In[70]:


no_of_rows=len(dataset_table.iloc[0:2,0])


# In[71]:


no_of_columns=len(dataset_table.iloc[0,0:2])


# In[72]:


ddof=(no_of_rows-1)*(no_of_columns-1)
print("Degree of Freedom:-",ddof)
alpha=0.05


# In[73]:


from scipy.stats import chi2
chi_square=sum([(o-e)**2./e for o,e in zip(Observed_Values,Expected_Values)])
chi_square_statistic=chi_square[0]+chi_square[1]


# In[74]:


print("chi_square_statistic:-",chi_square_statistic)


# In[75]:


critical_value=chi2.ppf(q=1-alpha,df=ddof)
print('critical_value:',critical_value)


# In[76]:


if chi_square_statistic>=critical_value:
    print("Reject H0,There is a relationship between two catagorical variable")
else:
    print("Retain H0,There is not a relationship between two catagorical variable")


# In[ ]:




