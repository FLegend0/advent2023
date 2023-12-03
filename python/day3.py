#!/usr/bin/env python
# coding: utf-8

# In[15]:


# part1
f = open("day3.txt", "r")
array = []
for line in f:
    linecontent = []
    for char in line:
        if char != "\n":
            linecontent.append(char)
    array.append(linecontent)
    
def checkAround(array, x, y):
    key = []
    for i in range(x-1, x+1+1):
        row = []
        for j in range(y-1, y+1+1):
            row.append((i, j))
        key.append(row)
    maxArray = len(array)
    maxLine = len(array[x])
    for row in key:
        for item in row:
            if item[0] < 0 or item[1] < 0 or item[0] >= maxArray or item[1] >= maxLine:
                continue
            if array[item[0]][item[1]].isnumeric() or array[item[0]][item[1]] == ".":
                continue
            else:
                return True
    return False    

sum = 0

for line in range(0, len(array)):
    currnum = ""
    checking = False
    valid = False
    for char in range(0, len(array[line])):
        if array[line][char].isnumeric():
            if not checking:
                checking = True
                currnum = array[line][char]
            else:
                currnum += str(array[line][char])
            
            if not valid and checkAround(array, line, char):
                valid = True
        elif checking:
            if valid:
                sum += int(currnum)
            currnum = ""
            checking = False
            valid = False
    if checking:
        if valid:
            sum += int(currnum)
            
print(sum)


# In[24]:


# part2     
def checkForNumbers(array, x, y):
    key = []
    for i in range(x-1, x+1+1):
        row = []
        for j in range(y-1, y+1+1):
            row.append((i, j))
        key.append(row)
    maxArray = len(array)
    maxLine = len(array[x])
    numbers = []
    gearcheck = 0
    for row in key:     
        indexIsNum = False
        currnum = ""
        startIndex = ""
        endIndex = ""
        for item in row:
            if item[0] < 0 or item[1] < 0 or item[0] >= maxArray or item[1] >= maxLine:
                continue
            if array[item[0]][item[1]].isnumeric():
                if not indexIsNum:
                    indexIsNum = True
                    gearcheck += 1
                    currnum = array[item[0]][item[1]]
                    startIndex = item[1]
                else:
                    currnum += str(array[item[0]][item[1]])
            elif indexIsNum:
                startIndex -= 1
                while startIndex >= 0 and array[item[0]][startIndex].isnumeric():
                    currnum = str(array[item[0]][startIndex]) + currnum
                    startIndex -= 1
                numbers.append(currnum)
                indexIsNum = False
                currnum = ""
                startIndex = ""
            
        if indexIsNum:
            startIndex -= 1     
            while startIndex >= 0 and array[item[0]][startIndex].isnumeric():
                currnum = str(array[item[0]][startIndex]) + currnum
                startIndex -= 1
            endIndex = int(item[1]) + 1
            while endIndex < maxLine and array[item[0]][endIndex].isnumeric():
                currnum = currnum + str(array[item[0]][endIndex])
                endIndex += 1
            numbers.append(currnum)
            indexIsNum = False
            currnum = ""
            startIndex = ""
            
    if gearcheck == 2:
        return numbers
    else:
        return []

result = 0    
    
for line in range(0, len(array)):
    for char in range(0, len(array[line])):
        if array[line][char] == "*":
            gear = checkForNumbers(array, line, char)
            if len(gear) == 2:
                result += (int(gear[0]) * int(gear[1]))
                
print(result)


# In[ ]:




