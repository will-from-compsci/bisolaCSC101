#!/usr/bin/env python
# coding: utf-8

# In[5]:


# Python program for Compound Interest
P = int(input('Input the Principal'))
R = float(input('Input the Annual rate in decimals'))
T = int(input('Input the Time'))
n = int(input('Input the number of compounding periods'))

A = (P *(1 + (R/n)**(n*T)))
print("Amount is", A)

CI = A - P
print("Compound interest is", CI)


# In[5]:


# Python program for Annuity Plan
PMT = int(input('Input the Regular deposit'))
R = float(input('Input the Annual rate in decimals'))
t = int(input('Input the Time'))
n = int(input('Input the number of compounding periods'))

A = (PMT*((1 + (R/n))**(n*t)) - 1)/(R/n)
print ("Annuity is", A)


# In[ ]:




