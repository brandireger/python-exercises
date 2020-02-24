#!/usr/bin/env python
# coding: utf-8

# In[3]:


# How many students are there?

len(students)


# In[4]:


# How many students prefer light coffee? 

len([student for student in students if student['coffee_preference'] == 'light'])


# In[8]:


# For each type of coffee roast?

len([student for student in students if student['coffee_preference'] == 'medium'])


# In[7]:


len([student for student in students if student['coffee_preference'] == 'dark'])


# In[27]:


# How many of each species of pet are there?

# This approach didn't answer the question, but it gave me an idea of how it works
sum([len([pets['species'] for pets in student['pets'] if pets['species'] == 'cat']) for student in students])


# In[28]:


sum([len([pets['species'] for pets in student['pets'] if pets['species'] == 'horse']) for student in students])


# In[29]:


sum([len([pets['species'] for pets in student['pets'] if pets['species'] == 'dog']) for student in students])


# In[38]:


# How many types of pet are there?

set(sum([[pet['species'] for pet in student['pets']] for student in students], []))


# In[9]:


# How many grades does each student have? Do they all have the same number of grades?

[len(student['grades']) for student in students]


# In[39]:


# What is each student's grade average?

# first i wanted to see the grades for each student
[student['grades'] for student in students]


# In[40]:


# then I added them together 
[sum(student['grades']) for student in students]


# In[42]:


# then I divided the sum of grades by the number of grades

[(sum(student['grades'])) / (len(student['grades'])) for student in students]


# In[45]:


# How many pets does each student have?

[len([pet for pet in student['pets']]) for student in students]


# In[52]:


# How many students are in web development? data science?

num_students_web_dev = len([student for student in students if student['course'] == 'web development'])

num_students_web_dev


# In[58]:


# What is the average number of pets for students in web development?

# first i found how many pets each student has
[len(student['pets']) for student in students if student['course'] == 'web development']


# In[57]:


# then I divided that by the number of students in web dev

[len(student['pets']) / (num_students_web_dev) for student in students if student['course'] == 'web development']


# In[61]:


# What is the average pet age for students in data science?

# first i want the age of each pet
[[pet['age'] for pet in student['pets']] for student in students if student['course'] == 'data science']


# In[72]:


# now add them all together: first flatten the list
sum([[pet['age'] for pet in student['pets']] for student in students if student['course'] == 'data science'], [])


# In[74]:


# now sum the list
summed_DS_pet_ages = sum(sum([[pet['age'] for pet in student['pets']] for student in students if student['course'] == 'data science'], []))
summed_DS_pet_ages


# In[75]:


# now find how many pets in total
num_of_pets_in_datascience = len([[pet['age'] for pet in student['pets']] for student in students if student['course'] == 'data science'])

num_of_pets_in_datascience


# In[76]:


# Now divide the summed ages by the number of pets
# this is the final answer
summed_DS_pet_ages / num_of_pets_in_datascience


# In[84]:


# What is most frequent coffee preference for data science students?
# first i want to see all coffee preferences for DS students

ds_coffee = [student['coffee_preference'] for student in students if student['course'] == 'data science']
ds_coffee


# In[87]:


max([ds_coffee.count(w) for w in ds_coffee])


# In[ ]:





# In[ ]:


# What is the least frequent coffee preference for web development students?


# In[ ]:


# What is the average grade for students with at least 2 pets?


# In[ ]:


# How many students have 3 pets?


# In[ ]:


# What is the average grade for students with 0 pets?


# In[ ]:


# What is the average grade for web development students? data science students?


# In[ ]:


# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?


# In[ ]:


# What is the average number of pets for medium coffee drinkers?


# In[ ]:


# What is the most common type of pet for web development students?


# In[ ]:


# What is the average name length?


# In[ ]:


# What is the highest pet age for light coffee drinkers?


# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:


students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]


# In[ ]:




