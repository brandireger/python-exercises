#!/usr/bin/env python
# coding: utf-8

# Use the following code for the questions below:

import numpy as np

a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# 1. How many negative numbers are there?

negatives = a < 0
print(negatives)
negatives.sum()


# 2. How many positive numbers are there?

positives = a > 0
print(positives)
positives.sum()


# 3. How many even positive numbers are there?

positive_evens = (a > 0) & (a % 2 == 0)
positive_evens.sum()


# 4. If you were to add 3 to each data point, how many positive numbers would there be?

array_plus_three = a + 3
print(array_plus_three)
array_plus_three = array_plus_three > 0
print(array_plus_three)
array_plus_three.sum()


# 5. If you squared each number, what would the new mean and standard deviation be?

squared_array = a ** 2
print(squared_array)
print(squared_array.mean())
print(squared_array.std())


# 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the center of the data is at 0. This is done by subtracting the mean from each data point. Center the data set.

mean = a.mean()
print(mean)
mean_array = a - mean
print(mean_array)


# 7. Calculate the z-score for each data point. Recall that the z-score is given by:
# 
# $Z = \begin{array}{cc} \underline{x - \mu}  \\  \sigma \end{array}$
# 

sigma = a.std()
print(sigma)

z_score = mean_array / sigma
print(z_score)


# 8. Copy the setup and exercise directions from More Numpy Practice into your 4.8.3_numpy_exercises.py and add your solutions.

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list

a = np.array(a)
sum_of_a = a.sum()
print(sum_of_a)


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list

min_of_a = a.min()
print(min_of_a)


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list

max_of_a = a.max()
print(max_of_a)


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list

mean_of_a = a.mean()
print(mean_of_a)


# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together

product_of_a = a.prod()
print(product_of_a)


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]

squares_of_a = a * a
print(squares_of_a)


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers

odds_in_a = a[a % 2 != 0]
print(odds_in_a)


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.

evens_in_a = a[a % 2 == 0]
print(evens_in_a)


# Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.

b = [
    [3, 4, 5],
    [6, 7, 8]
]

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**

b = np.array(b)
sum_of_b = b.sum()
print(sum_of_b)


# Exercise 2 - refactor the following to use numpy. 

min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  

min_of_b = b.min()
print(min_of_b)


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.

max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])

max_of_b = b.max()
print(max_of_b)


# Exercise 4 - refactor the following using numpy to find the mean of b

mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))

mean_of_b = b.mean()
print(mean_of_b)


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.

product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number

product_of_b = b.prod()
print(product_of_b)


# Exercise 6 - refactor the following to use numpy to find the list of squares

squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)

squares_of_b = b.flatten() ** 2
print(squares_of_b)


# Exercise 7 - refactor using numpy to determine the odds_in_b

odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)

odds_in_b = b[b % 2 != 0]
print(odds_in_b)


# Exercise 8 - refactor the following to use numpy to filter only the even numbers

evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)

evens_in_b = b[b % 2 == 0]
print(evens_in_b)


# Exercise 9 - print out the shape of the array b.

np.shape(b)


# Exercise 10 - transpose the array b.

np.transpose(b)


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)

b.flatten()


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)

b.reshape(6,1)

c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


# Exercise 1 - Find the min, max, sum, and product of c.

c = np.array(c)
print('min of c: {}'.format(c.min()))
print('max of c: {}'.format(c.max()))
print('sum of c: {}'.format(c.sum()))
print('product of c: {}'.format(c.prod()))


# Exercise 2 - Determine the standard deviation of c.

print('standard deviation of c: {}'.format(c.std()))


# Exercise 3 - Determine the variance of c.

print('variance of c: {}'.format(c.var()))


# Exercise 4 - Print out the shape of the array c

print('shape of c: {}'.format(np.shape(c)))


# Exercise 5 - Transpose c and print out transposed result.

print('transpose of c: {}'.format(np.transpose(c)))


# Exercise 6 - Get the dot product of the array c with c. 

print('dot product of c: {}'.format(np.dot(c, c)))


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

print('sum of c * c transposed: {}'.format((c * np.transpose(c)).sum()))


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.

print('product of c * c transposed: {}'.format((c * np.transpose(c)).prod().sum()))

d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]


# Exercise 1 - Find the sine of all the numbers in d

d = np.array(d)
np.sin(d)


# Exercise 2 - Find the cosine of all the numbers in d

np.cos(d)


# Exercise 3 - Find the tangent of all the numbers in d

np.tan(d)


# Exercise 4 - Find all the negative numbers in d

d[d < 0]


# Exercise 5 - Find all the positive numbers in d

d[d > 0]


# Exercise 6 - Return an array of only the unique numbers in d

np.unique(d)


# Exercise 7 - Determine how many unique numbers there are in d

np.size(np.unique(d))


# Exercise 8 - Print out the shape of d.

np.shape(d)


# Exercise 9 - Transpose and then print out the shape of d

np.shape(d.transpose())


# Exercise 10 - Reshape d into an array of 9 x 2

d.reshape(9, 2)


