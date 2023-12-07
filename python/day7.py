#!/usr/bin/env python
# coding: utf-8

# In[41]:


# part 1
from enum import Enum
class Hand(Enum):
    FIVE_OF_KIND = 1
    FOUR_OF_KIND = 2
    FULL_HOUSE = 3
    THREE_OF_KIND = 4
    TWO_PAIR = 5
    ONE_PAIR = 6
    HIGH_CARD = 7

key = ["A", "K", "Q", "J", "T", "9", "8", "7" ,"6", "5", "4", "3", "2"]

five_of_kind = []
four_of_kind = []
full_house = []
three_of_kind = []
two_pair = []
one_pair = []
high_card = []

wins = [five_of_kind, four_of_kind, full_house, three_of_kind, two_pair, one_pair, high_card]

def determine_value(card):
    card_values = [*card[0]]
    unique = set(card_values)
    if len(unique) == 1:
        five_of_kind.append(card)
        return Hand.FIVE_OF_KIND.value
    elif len(unique) == 2:
        for i in unique:
            if card_values.count(i) == 4:
                four_of_kind.append(card)
                return Hand.FOUR_OF_KIND.value
        full_house.append(card)
        return Hand.FULL_HOUSE.value
    elif len(unique) == 3:
        for i in unique:
            if card_values.count(i) == 3:
                three_of_kind.append(card)
                return Hand.THREE_OF_KIND.value
        two_pair.append(card)
        return Hand.TWO_PAIR.value
    elif len(unique) == 4:
        one_pair.append(card)
        return Hand.ONE_PAIR.value
    else:
        high_card.append(card)
        return Hand.HIGH_CARD.value
        
def sort_card(card):
    card_values = [*card[0]]
    result = []
    for i in card_values:
        result.append(key.index(i))
    return result
    
    
f = open("day7.txt", "r")
for line in f:
    line = line.strip()
    data = tuple(line.split(" "))
    determine_value(data)

for i in range(0, len(wins)):
    wins[i] = sorted(wins[i], key=sort_card)
    
total_winnings = 0
multiplier = 1
for i in range(len(wins)-1, -1, -1):
    for j in range(len(wins[i])-1, -1, -1):
        total_winnings += int(wins[i][j][1]) * multiplier
        multiplier += 1
print(total_winnings)


# In[68]:


# part 2
key = ["A", "K", "Q", "T", "9", "8", "7" ,"6", "5", "4", "3", "2", "J"]

def determine_value_with_joker(card):
    card_values = [*card[0]]
    unique = set(card_values)
#     print(unique)
#     print(card_values)
#     print("J" in unique)
    if len(unique) == 1:
        five_of_kind.append(card)
        return
    elif len(unique) == 2:
        if "J" in unique:
#             print("Hi")
            five_of_kind.append(card)
#             print(five_of_kind)
            return
        else:
            for i in unique:
                if card_values.count(i) == 4:
                    four_of_kind.append(card)
                    return
            full_house.append(card)
            return
    elif len(unique) == 3:
        if "J" in unique:
            jcount = 0
            other = []
            for i in unique:
                if i == "J":
                    jcount = card_values.count(i)
                else:
                    other.append(card_values.count(i))
            if max(other) + jcount == 4:
                four_of_kind.append(card)
                return
            else:
                full_house.append(card)
                return
        else:
            for i in unique:
                if card_values.count(i) == 3:
                    three_of_kind.append(card)
                    return
            two_pair.append(card)
            return
    elif len(unique) == 4:
        if "J" in unique:
            three_of_kind.append(card)
            return
        else:
            one_pair.append(card)
            return
    else:
        if "J" in unique:
            one_pair.append(card)
            return
        else:
            high_card.append(card)
            return

five_of_kind = []
four_of_kind = []
full_house = []
three_of_kind = []
two_pair = []
one_pair = []
high_card = []
wins = [five_of_kind, four_of_kind, full_house, three_of_kind, two_pair, one_pair, high_card]

f = open("day7.txt", "r")
for line in f:
    line = line.strip()
    data = tuple(line.split(" "))
    determine_value_with_joker(data)

for i in range(0, len(wins)):
    wins[i] = sorted(wins[i], key=sort_card)
    
total_winnings = 0
multiplier = 1
for i in range(len(wins)-1, -1, -1):
    for j in range(len(wins[i])-1, -1, -1):
        total_winnings += int(wins[i][j][1]) * multiplier
        multiplier += 1
print(total_winnings)


# In[ ]:




