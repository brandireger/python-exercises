#!/usr/bin/env python
# coding: utf-8

# 1. Import and test 3 of the functions from your functions exercise file.
# 
# -- Your functions exercise are not currently in a file with a name that can be easily imported. Copy your functions exercise file and name the copy functions_exercises.py.
# 
# -- Import each function in a different way:
# 
# -- import the module and refer to the function with the . syntax

# In[1]:


import function_exercises


# In[2]:


function_exercises.calculate_tip(0.2, 50)


# -- use from to import the function directly

# In[3]:


from function_exercises import apply_discount


# In[4]:


apply_discount(4697, 0.3)


# -- use from and give the function a different name

# In[5]:


from function_exercises import handle_commas as commas_are_bad


# In[6]:


commas_are_bad('2,935,023')


# For the following exercises, read about and use the itertools module from the standard library to help you solve the problem.
# 
# 1. How many different ways can you combine the letters from "abc" with the numbers 1, 2, and 3?

# In[12]:


from itertools import product

list(product('abc', '123'))


# In[13]:


len(list(product('abc', '123')))


# 2. How many different ways can you combine two of the letters from "abcd"?

# In[169]:


from itertools import combinations

list(combinations('abcd', 2))


# In[170]:


len(list(combinations('abcd', 2)))


# Save this file as profiles.json inside of your exercises directory. Use the load function from the json module to open this file, it will produce a list of dictionaries. 

# In[173]:


from json import load


# In[25]:


profiles = load(open("profiles.json"))


# In[27]:


profiles


# In[178]:


profiles[0]


# In[177]:


profiles[0].keys()


# In[180]:


# shows the first 4 values with 'in profiles[:4]'
[profile['balance'] for profile in profiles[:4]]


# In[181]:


from pprint import pprint

pprint(profiles)


# Using this data, write some code that calculates and outputs the following information:
# 
# Total number of users

# In[28]:


len(profiles)


# Number of active users

# In[182]:


len([profile for profile in profiles if profile['isActive']])


# Number of inactive users

# In[183]:


len([profile for profile in profiles if not profile['isActive']])


# Grand total of balances for all users

# In[63]:


profile_balances = [profile['balance'] for profile in profiles]

profile_balances


# In[185]:


def dollars_to_float(num):
    return float(num.replace(',','').replace('$',''))


# In[186]:


dollars_to_float('$2,940.24')


# In[188]:


# Solution from class
[dollars_to_float(profile['balance']) for profile in profiles]


# In[168]:


newlist = []

for profile in profile_balances:
    newlist.append(dollars_to_float(profile))
    
newlist


# In[70]:


sum(newlist)


# In[ ]:


Average balance per user


# In[74]:


sum(newlist) / len(newlist)


# User with the lowest balance

# In[89]:


min(newlist)


# In[104]:


[x for x in range(len(newlist)) if newlist[x] == min(newlist)]


# In[108]:


profiles[6]['name'], profiles[6]['balance']


# User with the highest balance

# In[109]:


max(newlist)


# In[110]:


[x for x in range(len(newlist)) if newlist[x] == max(newlist)]


# In[111]:


profiles[3]['name'], profiles[3]['balance']


# Most common favorite fruit

# In[122]:


fruitlist = [profile['favoriteFruit'] for profile in profiles]

fruitlist


# In[134]:


fruitcount = [fruitlist.count(x) for x in fruitlist]
fruitcount


# In[143]:


max(list(zip(fruitcount, fruitlist)))


# Least most common favorite fruit

# In[144]:


min(list(zip(fruitcount, fruitlist)))


# Total number of unread messages for all users

# In[148]:


greetinglist = [profile['greeting'] for profile in profiles]

greetinglist


# In[161]:


def get_digits(string):
    new_string = ''
    for s in string:
        if s.isdigit():
            new_string += s
    return new_string


# In[162]:


num_messages = []

for x in message_list:
    num_messages.append(int(get_digits(x)))

num_messages


# In[163]:


sum(num_messages)


# In[193]:


# Solutions from class:

def get_n_unread_messages(profile):
        greeting = profile['greeting']
        start_index = greeting.index('have ') + 5
        end_index = greeting.index(' unread')
        return int(greeting[start_index:end_index])


# In[195]:


sum([get_n_unread_messages(profile) for profile in profiles])


# In[200]:


profile = profiles[0]
greeting = profile['greeting']

int(''.join([c for c in greeting if c. isdigit()]))


# In[ ]:




