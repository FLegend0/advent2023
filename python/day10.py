#!/usr/bin/env python
# coding: utf-8

# In[41]:


# part1
f = open("day10.txt", "r")
pipemap = []
startindex = -1
for line in f:
    line = line.strip()
    pipemap.append(line)
    if "S" in line:
        startindex = (pipemap.index(line), line.index("S"))
key = ["right", "down", "left", "up"]

def check_next(pipemap, mapindex, currdirection):
    currval = pipemap[mapindex[0]][mapindex[1]]
    direction = None
    if currval != "S":
        if currval == "|":
            if currdirection == 1:
                direction = 1
            else:
                direction = 3
        elif currval == "-":
            if currdirection == 2:
                direction = 2
            else:
                direction = 0
        elif currval == "L":
            if currdirection == 1:
                direction = 0
            else:
                direction = 3
        elif currval == "J":
            if currdirection == 1:
                direction = 2
            else:
                direction = 3
        elif currval == "7":
            if currdirection == 3:
                direction = 2
            else:
                direction = 1
        elif currval == "F":
            if currdirection == 3:
                direction = 0
            else:
                direction = 1
    newindex = None
        
    if direction == 3:
        newindex = (mapindex[0]-1, mapindex[1])
    elif direction == 1:
        newindex = (mapindex[0]+1, mapindex[1])
    elif direction == 2:
        newindex = (mapindex[0], mapindex[1]-1)
    elif direction == 0:
        newindex = (mapindex[0], mapindex[1]+1)
    return (newindex, direction)

def check_adjacent(pipemap, sindex):
    if pipemap[sindex[0]][sindex[1]+1] == "-" or pipemap[sindex[0]][sindex[1]+1] == "7" or pipemap[sindex[0]][sindex[1]+1] == "J":
        return ((sindex[0], sindex[1]+1), 0)
    elif pipemap[sindex[0]+1][sindex[1]] == "|" or pipemap[sindex[0]+1][sindex[1]] == "J" or pipemap[sindex[0]+1][sindex[1]] == "L":
        return ((sindex[0]+1, sindex[1]), 1)
    elif pipemap[sindex[0]][sindex[1]-1] == "-" or pipemap[sindex[0]][sindex[1]-1] == "L" or pipemap[sindex[0]][sindex[1]-1] == "F":
        return ((sindex[0], sindex[1]-1), 2)
    return ((sindex[0]-1, sindex[1]), 3)


pipes = [startindex]
currval = "S"
count = 1
nextindex = check_adjacent(pipemap, startindex)
mapindex = nextindex[0]
direction = nextindex[1]
initialdirection = nextindex[1]
currval = pipemap[mapindex[0]][mapindex[1]]
pipes.append(mapindex)
while currval != "S":
    tempindex = check_next(pipemap, mapindex, direction)
    direction = tempindex[1]
    mapindex = tempindex[0]
    currval = pipemap[mapindex[0]][mapindex[1]]
    if mapindex not in pipes:
        pipes.append(mapindex)
    count += 1
finaldirection = direction
print(initialdirection)
print(finaldirection) # I use these to find the value of S, so I can abuse part 2
print(int(count / 2))


# In[46]:


# part2
pipemap2 = []
for i in pipemap:
    linebelow = ""
    newstring = ""
    for j in range(0, len(i)):
        nextchar = i[j]
        if nextchar == "-" or nextchar == "L" or nextchar == "F":
            newstring += nextchar + "-"
        else:
            newstring += nextchar + "."
        if nextchar == "|" or nextchar == "F" or nextchar == "7" or nextchar == "S":
            linebelow += "|."
        else:
            linebelow += ".."
            
    pipemap2.append(newstring)
    pipemap2.append(linebelow)
    
for line in pipemap2:
    if "S" in line:
        startindex = (pipemap2.index(line), line.index("S"))
        break

pipes = [startindex]
currval = "S"
count = 1
nextindex = check_adjacent(pipemap2, startindex)
mapindex = nextindex[0]
direction = nextindex[1]
currval = pipemap2[mapindex[0]][mapindex[1]]
pipes.append(mapindex)
while currval != "S":
    tempindex = check_next(pipemap2, mapindex, direction)
    direction = tempindex[1]
    mapindex = tempindex[0]
    currval = pipemap2[mapindex[0]][mapindex[1]]
    if mapindex not in pipes:
        pipes.append(mapindex)
    count += 1

    
for i in pipes:
    pipemap2[i[0]] = pipemap2[i[0]][:i[1]] + "W" + pipemap2[i[0]][i[1]+1:]
temp = open("temp.txt", "w")
for i in pipemap2:
    temp.write(i + "\n")
temp.close()
def dfs(pipemap, pipes, startindex):
    stack = []
    visited = [startindex]
    if pipemap[startindex[0]][startindex[1]+1] != "W":
        stack.append((startindex[0], startindex[1]+1))
        visited.append((startindex[0], startindex[1]+1))
    if pipemap[startindex[0]+1][startindex[1]] != "W":
        stack.append((startindex[0]+1, startindex[1]))
        visited.append((startindex[0]+1, startindex[1]))
    while len(stack) != 0:
        nextval = stack.pop()
        if nextval[1]+1 < len(pipemap) and (nextval[0], nextval[1]+1) not in visited and pipemap[nextval[0]][nextval[1]+1] != "W":
            stack.append((nextval[0], nextval[1]+1))
            visited.append((nextval[0], nextval[1]+1))
        if nextval[1]-1 >= 0 and (nextval[0], nextval[1]-1) not in visited and pipemap[nextval[0]][nextval[1]-1] != "W":
            stack.append((nextval[0], nextval[1]-1))
            visited.append((nextval[0], nextval[1]-1))
        if nextval[0]+1 < len(pipemap) and (nextval[0]+1, nextval[1]) not in visited and pipemap[nextval[0]+1][nextval[1]] != "W":
            stack.append((nextval[0]+1, nextval[1]))
            visited.append((nextval[0]+1, nextval[1]))
        if nextval[0]-1 >= 0 and (nextval[0]-1, nextval[1]) not in visited and pipemap[nextval[0]-1][nextval[1]] != "W":
            stack.append((nextval[0]-1, nextval[1]))
            visited.append((nextval[0]-1, nextval[1]))
    return visited
outside = dfs(pipemap2, pipes, (0,0))

inside = 0
for i in range(0, len(pipemap2), 2):
    for j in range(0, len(pipemap2), 2):
        if pipemap2[i][j] != "W" and (i, j) not in outside:
            inside += 1
print(inside)


# In[ ]:




