#!/usr/bin/env python
# coding: utf-8

# In[22]:


# part 1
f = open("day2.txt", "r")
result = 0
for game in f:
    valid = True
    gameid = int(game.split(":")[0][4:])
    data = game.split(":")[1]
    data = data.split(";")
    for i in data:
        gameset = i.split(",")
        for i in gameset:
            i = i.split(" ")
            if "red" in i[2] and int(i[1]) > 12:
                valid = False
                break
            elif "green" in i[2] and int(i[1]) > 13:
                valid = False
                break
            elif "blue" in i[2] and int(i[1]) > 14:
                valid = False
                break
    if valid:
        result += gameid
    
print(result)


# In[21]:


# part 2
f = open("day2.txt", "r")
result = 0
for game in f:
    red = 0
    green = 0
    blue = 0
    data = game.split(":")[1]
    data = data.split(";")
    for i in data:
        gameset = i.split(",")
        for i in gameset:
            i = i.split(" ")
            if "red" in i[2] and int(i[1]) > red:
                red = int(i[1])
            elif "green" in i[2] and int(i[1]) > green:
                green = int(i[1])
            elif "blue" in i[2] and int(i[1]) > blue:
                blue = int(i[1])
    power = red * green * blue
    result += power
    
print(result)


# In[ ]:




