#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. Conditional Basics


# In[17]:


# a. prompt the user for a day of the week, print out whether the day is Monday or not

day_of_week = input('What day of the week is it? ')
day_of_week = day_of_week.lower()

if day_of_week == ('monday'):
    print('Today is Monday')
else:
    print('Today is not Monday')


# In[113]:


# b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_of_week = input('What day of the week is it? ')
day_of_week = day_of_week.lower()

if day_of_week in ['saturday', 'sunday']:
    print('Today is a weekend')
else:
    print('Today is a weekday')


# In[114]:


# c. create variables and make up values for: 
# the number of hours worked in one week, the hourly rate, how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours
hours_worked = 45
hourly_rate = 50
overtime_hours = hours_worked - 40

if hours_worked <= 40:
    print(hours_worked * hourly_rate)
else:
    print(((overtime_hours * 1.5) * hourly_rate) + (40 * hourly_rate))


# In[ ]:


2. Loop Basics


# In[ ]:


a. While


# In[21]:


# Create an integer variable i with a value of 5.
# Create a while loop that runs so long as i is less than or equal to 15
# Each loop iteration, output the current value of i, then increment i by one.

i = 5

while i <= 15:
    print(i)
    i += 1


# In[23]:


# Create a while loop that will count by 2's starting with 0 and ending at 100. 
# Follow each number with a new line.

loop_number = 0

while loop_number <= 100:
    print(loop_number)
    loop_number += 2


# In[24]:


# Alter your loop to count backwards by 5's from 100 to -10.
loop_number = 100

while loop_number >= -10:
    print(loop_number)
    loop_number -= 5


# In[27]:


# Create a while loop that starts at 2, 
# and displays the number squared on each line 
# while the number is less than 1,000,000.
sqd_loop_number = 2

while sqd_loop_number < 1000000:
    print(sqd_loop_number)
    sqd_loop_number *= sqd_loop_number


# In[29]:


loop_trial = 100

while loop_trial >= 5:
    print(loop_trial)
    loop_trial -= 5


# In[ ]:


b. For Loops


# In[122]:


# Write some code that prompts the user for a number, 
# then shows a multiplication table up through 10 for that number.

multiplication = input('What number would you like to multiply? ')

for n in range(1,11):
    print(f'{multiplication} x {n} =', int(multiplication) * n)


# In[ ]:


# Create a for loop that uses print to create the output shown below.

1
22
333
4444
55555
666666
7777777
88888888
999999999


# In[123]:


for n in range(1,10):
    print(f'{n}' * n)


# c. break and continue

# In[125]:


# Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# (Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
# except for the number the user entered.

odd_range = -1

number_input = input('Enter an odd number between 1 and 50 ')

while (number_input.isdigit() == False
       or int(number_input) > 50 
       or int(number_input) < 1 
       or int(number_input) % 2 == 0):
    print(f'{number_input} is invalid. Try again.')
    number_input = input('Enter an odd number between 1 and 50 ')

number_input = int(number_input)
print()
print('Number to skip is:', number_input)
print()

while odd_range < 49:
    odd_range += 2
    if odd_range == number_input:
        print('Yikes! Skipping number:', number_input)
        continue
    print('Here is an odd number: ', odd_range)


# In[107]:


# The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
# (Hints: first make sure that the value the user entered is a valid number, 
# also note that the input function returns a string, so you'll need to convert 
# this to a numeric type.)

prompt = input('Enter a positive number:')
prompt = int(prompt)
starting_point = 0
while starting_point < (prompt + 1):
    print(starting_point)
    starting_point += 1


# In[126]:


# Write a program that prompts the user for a positive integer. 
#Next write a loop that prints out the numbers from the number the user entered down to 1.

prompt = input('Enter a positive number: ')
prompt = int(prompt)

while prompt >= 1:
    print(prompt)
    prompt -= 1


# 3. Fizzbuzz
# 
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping 
# and conditional logic skills.
# 

# In[112]:


# Write a program that prints the numbers from 1 to 100.
# For multiples of three print "Fizz" instead of the number
# For the multiples of five print "Buzz".
# For numbers which are multiples of both three and five print "FizzBuzz".

for n in range(1,101):
    if n % 3 == 0 and n % 5 == 0:
        print('FizzBuzz')
    elif n % 3 == 0:
        print('Fizz')
    elif n % 5 == 0:
        print('Buzz')
    else:
        print(n)


# 4. Display a table of powers.

# In[171]:


# Prompt the user to enter an integer.
# Display a table of squares and cubes from 1 to the value entered.
# Ask if the user wants to continue.
# Assume that the user will enter valid data.
# Only continue if the user agrees to.

prompt = input('What number would you like to go up to? ')

while (prompt.isdigit() == False
       or int(prompt) > 50 
       or int(prompt) < 1):
    print(f'{prompt} is invalid. Try again.')
    prompt = input('What number would you like to go up to? ')

prompt = int(prompt)
starting_point = 1
print()
print('Here is your table!')
print()
print('number | squared | cubed')
print('------ | ------- | -----')
while starting_point <= prompt:
    print(f'{starting_point:<7}| {starting_point ** 2:<8}| {starting_point ** 3}')
    starting_point += 1
print()

choice = input('Do you want to continue? ')
choice = choice.lower()
while True:
    if choice not in ['y', 'yes']:
        break
    
    else:
        prompt = input('What number would you like to go up to? ')

        while (prompt.isdigit() == False
            or int(prompt) > 50 or int(prompt) < 1):
            print(f'{prompt} is invalid. Try again.')
            prompt = input('What number would you like to go up to? ')

        prompt = int(prompt)
        starting_point = 1
        print()
        print('Here is your table!')
        print()
        print('number | squared | cubed')
        print('------ | ------- | -----')
        while starting_point <= prompt:
            print(f'{starting_point:<7}| {starting_point ** 2:<8}| {starting_point ** 3}')
            starting_point += 1
        choice = input('Do you want to continue? ')
        choice = choice.lower()
    
        


# Convert given number grades into letter grades.
# 
# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.
# Grade Ranges:
# 
# A : 100 - 88
# B : 87 - 80
# C : 79 - 67
# D : 66 - 60
# F : 59 - 0

# In[141]:


while True:
    print('Grading application')
    user_choice = input('Input a positive number. ')
    while (user_choice.isdigit() == False
          or int(user_choice) < 0
          or int(user_choice) >= 100):
        print(f'{user_choice} is nice, but we need a positive number.')
        user_choice = input('Input a positive number. ')
    
    user_choice = int(user_choice)
    if user_choice >= 88:
        print(f'{user_choice} is an A')
    elif user_choice >= 80:
        print(f'{user_choice} is a B')
    elif user_choice >= 67:
        print(f'{user_choice} is a C')
    elif user_choice >= 60:
        print(f'{user_choice} is a D')
    else:
        print(f'{user_choice} is an F')
    
    user_choice = input('Do you want to continue? Type y or yes. ')
    wants_to_stop = user_choice.lower() not in ['y', 'yes']
    if wants_to_stop:
        break


# Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.
# 
# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.

# In[145]:


books = [
    {
        'title': 'Oathbringer',
        'author': 'Brandon Sanderson',
        'genre': 'science fiction',
    },
    {
        'title': 'Outliers',
        'author': 'Malcom Gladwell',
        'genre': 'non-fiction',
    },
    {
        'title': 'Smart Mobs',
        'author': 'Howard Rheingold',
        'genre': 'non-fiction',
    },
]

for book in books:
    print(f"'{book['title']}' by {book['author']} is about {book['genre']}")


# In[147]:


genre = input('Please enter a genre. ')

for book in books:
    if book['genre'] == genre:
        print(book['title'])

