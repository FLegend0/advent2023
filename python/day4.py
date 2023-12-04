#!/usr/bin/env python
# coding: utf-8

# In[23]:


# part1
f = open("day4.txt", "r")
data = []
for line in f:
    line = line.strip()
    cardinput = line.split(":")[1:]
    carddata = cardinput[0].split("|")

    carddata[0] = carddata[0].split(" ")
    carddata[1] = carddata[1].split(" ")
    data.append(carddata)
    
score = 0
    
for winner, card in data:
    matches = 0
    for num in winner:
        if num != "" and num in card:
            matches += 1
    if matches > 0:
        score += 2 ** (matches - 1)
        
print(score)


# In[28]:


# part2

totalcards = [1] * len(data)
currindex = 0
for winner, card in data:
    matches = 0
    for num in winner:
        if num != "" and num in card:
            matches += 1
    if matches > 0:
        for i in range(currindex+1, currindex+matches+1):
            totalcards[i] += totalcards[currindex]
    currindex += 1

print(sum(totalcards))


# In[ ]:




