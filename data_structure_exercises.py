# The following questions reference the students data structure below. Write the python code to answer the following questions:

# How many students are there?

len(students)

= 14

# How many students prefer light coffee? For each type of coffee roast?

len([student for student in students if student['coffee_preference'] == 'light'])

= 3

len([student for student in students if student['coffee_preference'] == 'medium'])               

= 6

len([student for student in students if student['coffee_preference'] == 'dark'])

= 5

# How many types of each pet are there?

# this answer isn't right = 18
sum([len(student['pets']) for student in students]) 

# How many grades does each student have? Do they all have the same number of grades?

[len(student['grades']) for student in students]

= Yes, they each have 4 grades

# What is each student's grade average?
# How many pets does each student have?
# How many students are in web development? data science?
# What is the average number of pets for students in web development?
# What is the average pet age for students in data science?
# What is most frequent coffee preference for data science students?
# What is the least frequent coffee preference for web development students?
# What is the average grade for students with at least 2 pets?
# How many students have 3 pets?
# What is the average grade for students with 0 pets?
# What is the average grade for web development students? data science students?
# What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
# What is the average number of pets for medium coffee drinkers?
What is the most common type of pet for web development students?
What is the average name length?
What is the highest pet age for light coffee drinkers?