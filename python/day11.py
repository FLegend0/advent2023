#!/usr/bin/env python
# coding: utf-8

# In[37]:


# part1
f = open("day11.txt", "r")
cosmos = []
rowvoids = []
colvoids = []
currline = 0
for line in f:
    line = line.strip()
    cosmos.append(line)
    if line.count(".") == len(line):
        rowvoids.append(currline)
    currline += 1

currline = 0
coscols = len(cosmos[0])
for i in range(0, coscols):
    newcol = True
    for j in cosmos:
        if j[i] != ".":
            newcol = False
            break
    if newcol:
        colvoids.append(currline)
    currline += 1

def find_manhatten_dist(loc1, loc2):
    return abs(loc2[1] - loc1[1]) + abs(loc2[0] - loc1[0])

def calc_passed_voids(rowvoids, colvoids, loc1, loc2):
    passed = 0
    big = loc2[0]
    small = loc1[0]
    if big < small:
        big, small = small, big
    for i in rowvoids:
        if small < i < big:
            passed += 1
    big = loc2[1]
    small = loc1[1]
    if big < small:
        big, small = small, big
    for i in colvoids:
        if small < i < big:
            passed += 1
    return passed

galaxies = []
for i in range(0, len(cosmos)):
    for j in range(0, len(cosmos[i])):
        if cosmos[i][j] == "#":
            galaxies.append((i, j))

pathsum = 0
for i in range(0, len(galaxies)):
    for j in range(i+1, len(galaxies)):
        pathcount = find_manhatten_dist(galaxies[i], galaxies[j])
        pathsum += pathcount + (calc_passed_voids(rowvoids, colvoids, galaxies[i], galaxies[j]))
    
print(pathsum)


# In[38]:


# part2        
pathsum = 0
for i in range(0, len(galaxies)):
    for j in range(i+1, len(galaxies)):
        pathcount = find_manhatten_dist(galaxies[i], galaxies[j])
        pathsum += pathcount + (calc_passed_voids(rowvoids, colvoids, galaxies[i], galaxies[j]) * 999999)
    
print(pathsum)


# In[ ]:




