#!/usr/bin/env python
# coding: utf-8

# In[1]:


# part 1
f = open("day5.txt", "r")

seedlist = []
seedToSoil = dict()
soilToFertilizer = dict()
fertilizerToWater = dict()
waterToLight = dict()
lightToTemp = dict()
tempToHumid = dict()
humidToLocation = dict()

almanac = [seedlist, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemp, tempToHumid, humidToLocation]

currJob = 0
for line in f:
    line = line.strip()
    if "map" in line:
        currJob += 1
        continue
    if currJob == 0:
        data = line.split(" ")
        for value in data:
            if value.isnumeric():
                seedlist.append(value)
    if currJob >= 1:
        data = line.split(" ")
        if len(data) == 3:
            almanac[currJob][data[1]] = (int(data[0]), int(data[2])-1)

def getAlmanacValue(almanac, index, value):
    almdata = list(almanac[index].keys())
    almdata = [int(i) for i in almdata]
    almdata.sort()
    maxAlmVal = 0
    for i in range(len(almdata)-1, -1, -1):
        if int(almdata[i]) <= value:
            maxAlmVal = int(almdata[i])
            break
    if str(maxAlmVal) in almanac[index]:
        maxDataVal = maxAlmVal + almanac[index][str(maxAlmVal)][1]
        if maxDataVal >= value:
            seedAdder = value - maxAlmVal
            return almanac[index][str(maxAlmVal)][0] + seedAdder
    return value
    
locationresults = []

for seed in seedlist:
    index = 1
    currval = int(seed)
    while index < len(almanac):
        currval = getAlmanacValue(almanac, index, currval)
        index += 1
    locationresults.append(currval)
    
print(min(locationresults))


# In[2]:


# part 2
def getRangedAlmanacData(almanac, index, value):
    almdata = list(almanac[index].keys())
    almdata = [int(i) for i in almdata]
    almdata.sort(reverse=True)
    maxAlmVal = 0
    maxAlmInd = -1
    for i in range(0, len(almdata)):
        if int(almdata[i]) <= value:
            maxAlmVal = int(almdata[i])
            maxAlmInd = i
            break
    if str(maxAlmVal) in almanac[index]:
        maxDataVal = maxAlmVal + almanac[index][str(maxAlmVal)][1]
        if maxDataVal >= value:
            seedAdder = value - maxAlmVal
            result = almanac[index][str(maxAlmVal)][0] + seedAdder
            seedsleft = almanac[index][str(maxAlmVal)][1] - seedAdder
            if maxAlmInd - 1 >= 0:
                return (result, maxAlmVal, seedsleft, almdata[maxAlmInd-1])
            else:
                return (result, maxAlmVal, seedsleft, maxDataVal+1)
        else:
            return (value, None, None, None)
    return (value, None, None, almdata[-1]) # (value, maxAlmVal, maxSteps, nextMaxAlmVal)

def compileRangedAlmData(almanac, minrange, maxrange, resultslist):
    rangeAlmData = []
    
    index = 1
    currval = (minrange,)
    while index < len(almanac):
        currval = getRangedAlmanacData(almanac, index, currval[0])
        rangeAlmData.append(currval)
        index += 1
    resultslist.append(currval[0])
    nextchange = min([i[2] for i in rangeAlmData if i[2] != None])
    return nextchange

rangeSeedLocationResults = []

for i in range(0, len(seedlist), 2):
    minrange = int(seedlist[i])
    maxrange = int(seedlist[i])+int(seedlist[i+1])
    
    nextchange = compileRangedAlmData(almanac, minrange, maxrange, rangeSeedLocationResults) + minrange + 1
    while maxrange - nextchange > 0:
        nextchange = compileRangedAlmData(almanac, nextchange, maxrange, rangeSeedLocationResults) + nextchange + 1
        
print(min(rangeSeedLocationResults))


# In[ ]:




