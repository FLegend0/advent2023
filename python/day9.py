#!/usr/bin/env python
# coding: utf-8

# In[9]:


# part1
f = open("day9.txt", "r")
result = 0

def calc_next_num_sequence(history):
    temp = int(history[-1][-1]) + int(history[-2][-1])
    for i in range(len(history)-3, -1, -1):
        temp = int(history[i][-1]) + temp
    return temp

historydata = []

for line in f:
    history = []
    data = line.strip().split(" ")
#     print(data)
    history.append(data)
    nextdata = []
    while True:
        for i in range(1, len(data)):
            nextdata.append(int(data[i]) - int(data[i-1]))
        history.append(nextdata)
        if nextdata.count(0) == len(nextdata):
            break
        
        data = nextdata
        nextdata = []
    historydata.append(history)
    result += calc_next_num_sequence(history)
print(result)


# In[15]:


# part2
def calc_prev_num_sequence(history):
    temp = int(history[-2][0])
    for i in range(len(history)-3, -1, -1):
        temp = int(history[i][0]) - temp
    return temp

result = 0

for line in historydata: 
    result += calc_prev_num_sequence(line)
    
print(result)


# In[ ]:




