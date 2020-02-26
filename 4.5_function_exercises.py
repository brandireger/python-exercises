#!/usr/bin/env python
# coding: utf-8

# Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.

# In[33]:


def is_two(num):
    if num == '2' or num == 2:
        return True
    else:
        return False


# In[34]:


is_two('2')


# In[35]:


# Solution from class:
def is_two(num):
    return x == 2 or x == '2'


# Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.

# In[3]:


def is_vowel(arg):
    if arg.lower() in 'aeiou':
        return True
    else:
        return False


# In[4]:


is_vowel('E')


# In[42]:


# Solution from class:
#def is_vowel(letter):
#    return letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u'
def is_vowel(letter):
    return letter.lower() in 'aeiou' and len(letter) == 1


# In[43]:


assert is_vowel('c') == False
assert is_vowel('z') == False
assert is_vowel('a') == True
assert is_vowel('e') == True
assert is_vowel('i') == True
assert is_vowel('o') == True
assert is_vowel('u') == True
assert is_vowel('A') == True
assert is_vowel('ae') == False


# Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.

# In[5]:


def is_consonant(arg):
    if is_vowel(arg) == False:
        return True
    else:
        return False


# In[6]:


is_consonant('e')


# In[ ]:


# Solution from class:
def is_consonant(letter):
    return len(letter) == 1 and letter.isalpha() and not is_vowel(letter)


# Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.

# In[7]:


def capitalize_consonant(arg):
    if is_consonant(arg[0]) == True:
        return arg.capitalize()
    else:
        return arg


# In[8]:


capitalize_consonant('atreyu')


# In[9]:


capitalize_consonant('beef')


# Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.

# In[10]:


def calculate_tip(tip_percent, bill_total):
    if tip_percent < 0 or tip_percent >= 1:
        return print(f'{tip_percent} is not a percentage.')
    else:
        return tip_percent * bill_total


# In[11]:


calculate_tip(0.1, 50)


# Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.

# In[12]:


def apply_discount(original_price, discount):
    if discount < 0 or discount >= 1:
        return print(f'{discount} is not a percentage.')
    else:
        return original_price - (original_price * discount)


# In[13]:


apply_discount(50, 0.3)


# Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.

# In[14]:


def handle_commas(num):
    num = num.replace(',','')
    return int(num)


# In[15]:


handle_commas('1,000,000')


# Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).

# In[16]:


def get_letter_grade(num):
    if num > 89:
        return print(f'{num} is an A')
    elif num > 79:
        return print(f'{num} is a B')
    elif num > 69:
        return print(f'{num} is a C')
    elif num > 59:
        return print(f'{num} is a D')
    else:
        return print(f'{num} is an F')


# In[17]:


get_letter_grade(95)


# Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.

# In[18]:


def remove_vowels(arg):
    for i in arg.lower():
        if i in 'aeiou':
            arg = arg.replace(i, '')
    return arg


# In[19]:


remove_vowels('Bananana')


# In[44]:


def remove_vowels(arg):
    return ''.join([c for c in arg if not is_vowel(c)])


# In[45]:


assert remove_vowels('Codeup') == 'Cdp'
assert remove_vowels('a') == ''


# Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
# - anything that is not a valid python identifier should be removed
# - leading and trailing whitespace should be removed
# - everything should be lowercase
# - spaces should be replaced with underscores
# for example:
# Name will become name
# First Name will become first_name
# % Completed will become completed

# In[20]:


def normalize_name(arg):
    arg = arg.lower()
    arg = arg.replace(" ", "_")
    for i in arg:
        if i.isdigit() == True or i.isalpha() == True or i == "_":
            continue
        else:
            arg = arg.replace(i, "")
    return arg


# In[21]:


normalize_name('Brandi Reger and I ** $#@875865')


# Write a function named cumsum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
# cumsum([1, 1, 1]) returns [1, 2, 3]
# cumsum([1, 2, 3, 4]) returns [1, 3, 6, 10]

# In[22]:


def cumsum(arg):
    argsum = 0
    newlist = []
    for i in arg:
        argsum += i
        newlist.append(argsum)
    return newlist


# In[23]:


cumsum([1, 2, 3, 4])


# # Bonus

# Create a function named twelveto24. It should accept a string in the format 10:45am or 4:30pm and return a string that is the representation of the time in a 24-hour format. Bonus write a function that does the opposite.

# In[24]:


def twelveto24(arg):
    minute = []
    hour = []
    twelve = []
    pieces = arg.split(':')
    hour.append(pieces[0])
    for i in pieces[1]:
        if i.isdigit() == True:
            minute.append(i)
        else:
            twelve.append(i)
    minute = ':' + minute[0] + minute[1]
    if twelve[0] == 'a':
        hour.append(minute)
        return hour[0] + minute
    else:
        newhour = int(hour[0]) + 12
        return str(newhour) + minute


# In[25]:


print(twelveto24('10:45pm'))
print(twelveto24('10:45am'))


# Create a function named col_index. It should accept a spreadsheet column name, and return the index number of the column.
# 
# col_index('A') returns 1
# col_index('B') returns 2
# col_index('AA') returns 27

# In[26]:


def col_index(col_name):
    num = 0
    for i in col_name:
        num = num * 26 + 1 + ord(i) - ord('A')
    return num


# In[27]:


col_index('ABA')


# In[32]:


ord('A')


# In[ ]:




