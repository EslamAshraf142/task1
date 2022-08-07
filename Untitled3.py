#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range(1500,2701):

    if i%7==0 and i%5==0:

        print("  ",i)

        


# In[2]:


celsius = float(input("Enter temperature in celsius: "))
fahrenheit = (celsius * 9/5) + 32
print('%.2f Celsius is: %0.2f Fahrenheit' %(celsius, fahrenheit))


# In[ ]:





# In[3]:


word = input("Input a word to reverse: ")
 
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
print("\n")


# In[13]:


def maximum(a, b, c): 
   list = [a, b, c] 
   return max(list) 
x = int(input("Enter First number"))
y = int(input("Enter Second number"))
z = int(input("Enter Third number"))
print("Maximum Number is ::>",maximum(x, y, z)) 


# In[17]:


def sum(numbers):
    total = 0
    for x in numbers:
        total += x
    return total
print(sum([8, 2, 3, 0, 7]))


# In[18]:


for x in range(7):

   if (x == 3 or x==6):

       continue

   print(x, end=' ')

print("\n")


# In[25]:


def fact (n) :
    if n== term +1 :
        return 1
    else :
        return n*fact(n+1)
term = int(input("Enter the term :-"))
print("Factorial =",fact(1))


# In[28]:


def unique_list(l):
  num = []
  for a in l:
    if a not in num:
      num.append(a)
  return num
print('unique elements are')
print(unique_list([1,2,4,5,4,5,6,9,10]))


# In[29]:


r = lambda a : a + 15
print(r(10))
r = lambda x, y : x * y
print(r(12, 4))


# In[ ]:




