#!/usr/bin/env python
# coding: utf-8

# In[13]:


f = open("input.txt", "r")
result = 0
for item in f:
    numbers = [int(x) for x in list(item) if x.isnumeric()]
    value = int(str(numbers[0]) + str(numbers[-1]))
    result += value
print(result)


# In[19]:


f = open("input.txt", "r")
key = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
result = 0
for item in f:
    minind = 9999
    maxind = -1
    minval = ""
    maxval = ""
    for i in range(0, len(key)):
        ind = item.find(key[i])
        if ind != -1:
            if ind < minind:
                minind = ind
                minval = i+1
                if minval > 9:
                    minval -= 9
        ind = item.rfind(key[i])
        if ind != -1:
            if ind > maxind:
                maxind = ind
                maxval = i+1
                if maxval > 9:
                    maxval -= 9
    result += int(str(minval) + str(maxval))
print(result)


# In[ ]:




