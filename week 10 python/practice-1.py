#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Numeric Data Types in Python

# integer number
num = 100
print(num)
print ("Data Type of variable num is", type(num))

# float number
fnum = 34.45
print(fnum)
print("Data Type of variable fnum is", type(fnum))

# complex number
cnum = 3 + 4j
print(cnum)
print("Data Type of variable cnum is", type(cnum))


# In[2]:


#Python Data Type - String

# Python program to print strings and type
str1 = "Hi my name is Matthew. I am a String"
str2 = 'Hi my name is Precious. I am also a String'

#displaying string str1 and its type
print(str1)
print(type(str1))

#displaying string str2 and its type
print(str2)
print(type(str2))


# In[6]:


# Python Data Type - Tuple

# tuple of integers
t1 = (1, 2, 3, 4, 5)

# prints entire tuple
print(t1)

# tuple of strings
t2 = ("Nifemi", "Gina", "Marho")

# loop through tuple elememts
for s in t2:
    print (s)

# tuple of mixed type elements
t3 = (2, "Ebube", 45, "Jeffery")

print (t3[2])


# In[7]:


# Python Data Type - List

#list of integers
lis1 = [1, 2, 3, 4, 5]

#prints entire list
print(lis1)

# list of strings
lis2 = ["Mouse", "Keyboard", "Monitor"]

# loop through list elements
for x in lis2:
    print (x)
    
# list of mixed type elememts
lis3 = [20, "CSC101", 15, "Python Programming"]

print ("Element at index 3 is:", lis3[3])


# In[8]:


# Python Data Type - Dictionary

# Dictionary example
dict = {1:"Maryam","lastname":"Shefiu","age":25}

# prints the value where key value is 1
print(dict[1])

# prints the value where key value is "lastname"
print(dict["lastname"])

# prints the value where key value is "age"
print(dict["age"])


# In[9]:


# Python Data Type - Set

# Set Example
myset = {"Joseph", "Adaobi", "Kamara", "Ugochi"}

# Loop through set
for a in myset:
    print (a)
    
# checking whether 2 exists in myset
print(2 in myset)

# adding new element 
myset.add (99)
print(myset)


# In[11]:


# Simple Interest Problem

P = 1000
R = 1
T = 2

#simple interest
A = (P * (1 + ((R / 100.0 * T))))
print ("Amount is", A)
SI = A - P
print ("Simple Interest is", SI)


# In[12]:


# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

#find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solutions are', sol1, sol2)


# In[13]:


# Python Program to find the area of a triangle

# Take inputs from the user
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))

# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print ('The area of the triangle is %0.2f' %area)

