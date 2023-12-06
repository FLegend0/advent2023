#!/usr/bin/env python
# coding: utf-8

# In[11]:


# part1
f = open("day6.txt", "r")
times = f.readline().split(":")
times[1] = times[1].strip().rstrip()
times = times[1].split("     ")
distances = f.readline().split(":")
distances[1] = distances[1].strip().rstrip()
distances = distances[1].split("   ")

result = 1
for i in range(0, len(times)):
    time = int(times[i])
    distance = int(distances[i])
    maxtime = time // 2
    dist = maxtime * (time - maxtime)
    distsbeat = 0
    while dist > distance and maxtime >= 0:
        distsbeat += 1
        maxtime -= 1
        dist = maxtime * (time - maxtime)
    if time % 2 == 0:
        distsbeat = distsbeat * 2 - 1
    else:
        distsbeat *= 2
    result *= distsbeat
    
print(result)


# In[17]:


# part2
totaltime = int("".join(i for i in times))
totaldist = int("".join(i for i in distances))

maxtime = totaltime // 2
dist = maxtime * (totaltime - maxtime)
distsbeat = 0
while dist > totaldist and maxtime >= 0:
    distsbeat += 1
    maxtime -= 1
    dist = maxtime * (totaltime - maxtime)
if time % 2 == 0:
    distsbeat = distsbeat * 2 - 1
else:
    distsbeat *= 2
    
print(distsbeat)


# In[ ]:




