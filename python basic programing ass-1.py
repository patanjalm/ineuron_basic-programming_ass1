#!/usr/bin/env python
# coding: utf-8

# 1.	Write a Python program to print "Hello Python"?

# In[13]:


a="Hello Python"
print(a)


# 2.	Write a Python program to do arithmetical operations addition and division.?

# In[14]:


a=int(input("Enter first no. "))
b=int(input("Enter second no. "))
# Addition
print("Addition ",a+b)
#Division
print("Division ",a/b)


# 3.	Write a Python program to find the area of a triangle?

# In[15]:


a = eval(input("Enter first side of traiangle"))
b= eval(input("Enter second side of traiangle"))
c= eval(input("Enter third side of traiangle"))
s = (a+b+c)/2
if a+b ==c or b+c==a or c+a==b:
    print("Enter valid value")
else:
    Area_of_traiangle = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    print("Area_of_traiangle ",Area_of_traiangle)


# 4.	Write a Python program to swap two variables?

# In[16]:


a=10
b=20
b,a=a,b


# In[17]:


a


# In[18]:


b


# 5.	Write a Python program to generate a random number?

# In[19]:


import random
while True:
    try:
        a= int(input("Enter your starting number choice"))
        b= int(input("Enter you last number choice "))
        n = random.randint(a,b)
        print("Random number between starting and last number choice",n)
        break
    except Exception as e:
        print("Enter right choice number",e)
        


# In[ ]:




