#!/usr/bin/env python
# coding: utf-8

# In[1]:


# part1
f = open("day8.txt", "r")
sequence = ""
paths = dict()
for line in f:
    if "=" not in line:
        sequence += line
    else:
        line = line.split(" = ")
        key = line[0].strip().rstrip()
        data = line[1].strip("()\n")
        data = tuple(data.split(", "))
        paths[key] = data

sequence = sequence.strip()
seq = []
for i in sequence:
    if i == "L":
        seq.append(0)
    elif i == "R":
        seq.append(1)
steps = 0
currpath = "AAA"
currindex = 0
seqlen = len(seq)
while currpath != "ZZZ":
    if currindex >= seqlen:
        currindex = 0
    currpath = paths[currpath][seq[currindex]]
    currindex += 1
    steps += 1
print(steps)


# In[2]:


# part2
currpaths = []
zpaths = []
for i in paths.keys():
    if i[2] == "A":
        currpaths.append(i)
    if i[2] == "Z":
        zpaths.append(i)
steps = 0
check = 0
fullcheck = len(currpaths)
currindex = 0
pathdata = []
for i in range(0, len(currpaths)):
    steps = 0
    currindex = 0
    while True:
        if currindex >= seqlen:
            currindex = 0
        currpaths[i] = paths[currpaths[i]][seq[currindex]]
        steps += 1
        currindex += 1
        if currpaths[i][2] == "Z":
            zindex = zpaths.index(currpaths[i])
            pathdata.append((zindex, steps))
            if pathdata.count((zindex, steps)) >= 4:
                break
            steps = 0
import math
pathnums = []
result = 1
for i in range(0, len(pathdata), 4):
    pathnums.append(pathdata[i][1])
    result *= int(pathdata[i][1])
# print(math.lcm(pathnums))  # I'm not using python 3.9 so I can't use this function
print(pathnums)  # I got the numbers here and put them in an online LCM calculator
# I hate numpy, numpy lcm gave me the wrong answer, numpy is bad


# In[ ]:




