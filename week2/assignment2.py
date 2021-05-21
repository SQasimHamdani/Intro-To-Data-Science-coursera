#!/usr/bin/env python
# coding: utf-8

# # Assignment 2
# For this assignment you'll be looking at 2017 data on immunizations from the CDC. Your datafile for this assignment is in [assets/NISPUF17.csv](assets/NISPUF17.csv). A data users guide for this, which you'll need to map the variables in the data to the questions being asked, is available at [assets/NIS-PUF17-DUG.pdf](assets/NIS-PUF17-DUG.pdf). **Note: you may have to go to your Jupyter tree (click on the Coursera image) and navigate to the assignment 2 assets folder to see this PDF file).**

# # Submitted by Syed Qasim

# ## Question 1
# Write a function called `proportion_of_education` which returns the proportion of children in the dataset who had a mother with the education levels equal to less than high school (<12), high school (12), more than high school but not a college graduate (>12) and college degree.
# 
# *This function should return a dictionary in the form of (use the correct numbers, do not round numbers):* 
# ```
#     {"less than high school":0.2,
#     "high school":0.4,
#     "more than high school but not college":0.2,
#     "college":0.2}
# ```
# 

# In[21]:


def proportion_of_education():
    # your code goes here
    # YOUR CODE HERE
    
    import pandas as pd
    df = pd.read_csv('assets/NISPUF17.csv')
    df.head(5)
    
    count = [0,0,0,0]
    for num,value in df['EDUC1'].iteritems():
        count[value-1] += 1
#     print(count)
    total_count = sum(count)

#     print(total_count)

    res = { "less than high school":count[0]/total_count,
            "high school":count[1]/total_count,
            "more than high school but not college":count[2]/total_count,
            "college":count[3]/total_count
          }
    return res
    
#     raise NotImplementedError()


# In[22]:


assert type(proportion_of_education())==type({}), "You must return a dictionary."
assert len(proportion_of_education()) == 4, "You have not returned a dictionary with four items in it."
assert "less than high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "high school" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "more than high school but not college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."
assert "college" in proportion_of_education().keys(), "You have not returned a dictionary with the correct keys."


# ## Question 2
# 
# Let's explore the relationship between being fed breastmilk as a child and getting a seasonal influenza vaccine from a healthcare provider. Return a tuple of the average number of influenza vaccines for those children we know received breastmilk as a child and those who know did not.
# 
# *This function should return a tuple in the form (use the correct numbers:*
# ```
# (2.5, 0.1)
# ```

# In[30]:


def average_influenza_doses():
    df = pd.read_csv('assets/NISPUF17.csv')
    df.head(5)
    df = df[['CBF_01','P_NUMFLU']]
    df.head(5)
    df.isna().sum()
    df= df[df['P_NUMFLU'].notna()]
    df
    tot1 = len(df[df['CBF_01']==1])
    tot2 = len(df[df['CBF_01']==2])

    mi = df[df['CBF_01']==1]['P_NUMFLU'].sum()
    notmi = df[df['CBF_01']==2]['P_NUMFLU'].sum()
    return (mi/tot1,notmi/tot2)
    # YOUR CODE HERE
    raise NotImplementedError()


# In[31]:


assert len(average_influenza_doses())==2, "Return two values in a tuple, the first for yes and the second for no."


# ## Question 3
# It would be interesting to see if there is any evidence of a link between vaccine effectiveness and sex of the child. Calculate the ratio of the number of children who contracted chickenpox but were vaccinated against it (at least one varicella dose) versus those who were vaccinated but did not contract chicken pox. Return results by sex. 
# 
# *This function should return a dictionary in the form of (use the correct numbers):* 
# ```
#     {"male":0.2,
#     "female":0.4}
# ```
# 
# Note: To aid in verification, the `chickenpox_by_sex()['female']` value the autograder is looking for starts with the digits `0.0077`.

# In[35]:


def chickenpox_by_sex():
    # YOUR CODE HERE
    df = pd.read_csv('assets/NISPUF17.csv')
    df = df[df['P_NUMVRC']>=1]
    x = df[df['HAD_CPOX']==1]
    y = df[df['HAD_CPOX']==2]
    dic = {}
    male_infected = len(x[x['SEX']==1])
    male_notinfected = len(y[y['SEX']==1])
    female_infected = len(x[x['SEX']==2])
    female_notinfected = len(y[y['SEX']==2])

    dic['male'] = male_infected/male_notinfected
    dic['female'] = female_infected/female_notinfected
    return dic

    raise NotImplementedError()


# In[36]:


assert len(chickenpox_by_sex())==2, "Return a dictionary with two items, the first for males and the second for females."


# ## Question 4
# A correlation is a statistical relationship between two variables. If we wanted to know if vaccines work, we might look at the correlation between the use of the vaccine and whether it results in prevention of the infection or disease [1]. In this question, you are to see if there is a correlation between having had the chicken pox and the number of chickenpox vaccine doses given (varicella).
# 
# Some notes on interpreting the answer. If the `had_chickenpox_column` is either `1` (for yes) or `2` for no, and that the `num_chickenpox_vaccine_column` is the number of doses a child has been given of the varicella vaccine, then a positive correlation (e.g. `corr > 0`) would mean that an increase in `had_chickenpox_column` (which means more no's) would mean an increase in the `num_chickenpox_vaccine_column` (which means more doses of vaccine). If `corr < 0` then there is a negative correlation, indicating that having had chickenpox is related to an increase in the number of vaccine doses. Also, `pval` refers to the probability the relationship observed is significant. In this case `pval` should be very very small (will end in `e-18` indicating a very small number), which means the result unlikely to be by chance.
# 
# [1] This isn't really the full picture, since we are not looking at when the dose was given. It's possible that children had chickenpox and then their parents went to get them the vaccine. Does this dataset have the data we would need to investigate the timing of the dose?

# In[38]:


def corr_chickenpox():
    import scipy.stats as stats
    import numpy as np
    import pandas as pd
    
    # this is just an example dataframe
    df=pd.DataFrame({"had_chickenpox_column":np.random.randint(1,3,size=(100)),
                   "num_chickenpox_vaccine_column":np.random.randint(0,6,size=(100))})

    # here is some stub code to actually run the correlation
    corr, pval=stats.pearsonr(df["had_chickenpox_column"],df["num_chickenpox_vaccine_column"])
    
    # just return the correlation
    #return corr

    # YOUR CODE HERE
    df = pd.read_csv('assets/NISPUF17.csv')
    df = df[['HAD_CPOX','P_NUMVRC']]
    df = df[df['HAD_CPOX']<=3]
    df = df[df['P_NUMVRC'].notna()]
    
    corr,pval = stats.pearsonr(df['HAD_CPOX'],df['P_NUMVRC'])
    return corr
    
    
    raise NotImplementedError()


# In[39]:


assert -1<=corr_chickenpox()<=1, "You must return a float number between -1.0 and 1.0."


# In[ ]:




