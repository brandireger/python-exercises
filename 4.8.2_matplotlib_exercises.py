#!/usr/bin/env python
# coding: utf-8

# $$
# y_i = \sum{x_i \times w_i}
# $$

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')

import matplotlib.pyplot as plt


# Use matplotlib to plot the following equation:
# 
# $$
# y = x^2  - x + 2
# $$
# 
# You'll need to write the code that generates the x and y points.
# 
# Add an annotation for the point 0, 0, the origin.

# In[27]:


x = range(10)
y = [x**2 - x + 2 for x in x]

plt.plot(x, y)

plt.text(0, 4, '(0, 0)', fontsize=10, color='blue')
plt. annotate('Origin', xy=(0,0), xytext=(0, 8))
plt.show


# Create and label 4 separate charts for the following equations (choose a range for x that makes sense):
# 
# $$
# y = \sqrt{x}
# $$

# In[40]:


x = range(100)
y = [x ** 0.5 for x in x]

plt.title('Equation: $y = \sqrt{x}$')
plt.xlabel('$x$')
plt.ylabel('$\sqrt{x}$')

plt.plot(x, y)
plt.show


# $$
# y = x^3
# $$

# In[42]:


x = range(100)
y = [x ** 3 for x in x]

plt.title('Equation: $y = x^3$')
plt.xlabel('$x$')
plt.ylabel('$x^3$')

plt.plot(x, y)
plt.show


# $$
# y = tan(x)
# $$

# In[51]:


import math

x = range(1000)
y = [math.tan(x) for x in x]

plt.title('Equation: $y = tan(x)$')
plt.xlabel('$x$')
plt.ylabel('$tan(x)$')

plt.plot(x, y)
plt.show


# $$
# y = 2^x
# $$

# In[48]:


x = range(100)
y = [2 ** x for x in x]

plt.title('Equation: $y = 2^x$')
plt.xlabel('$x$')
plt.ylabel('$2^x$')

plt.plot(x, y)
plt.show


# Combine the figures you created in the last step into one large figure with 4 subplots.

# In[55]:


x = range(100)

plt.figure(figsize=(16, 16))
plt.suptitle('One large plot')

plt.subplot(2, 2, 1)
y1 = [x ** 0.5 for x in x]
plt.title('Equation: $y = \sqrt{x}$')
plt.xlabel('$x$')
plt.ylabel('$\sqrt{x}$')
plt.plot(x, y1)

plt.subplot(2, 2, 2)
y2 = [x ** 3 for x in x]
plt.title('Equation: $y = x^3$')
plt.xlabel('$x$')
plt.ylabel('$x^3$')
plt.plot(x, y2)

plt.subplot(2, 2, 3)
y3 = [math.tan(x) for x in x]
plt.title('Equation: $y = tan(x)$')
plt.xlabel('$x$')
plt.ylabel('$tan(x)$')
plt.plot(x, y3)

plt.subplot(2, 2, 4)
y4 = [2 ** x for x in x]
plt.title('Equation: $y = 2^x$')
plt.xlabel('$x$')
plt.ylabel('$2^x$')
plt.plot(x, y4)

plt.show()


# Combine the figures you created in the last step into one figure where each of the 4 equations has a different color for the points. Be sure to include a legend.

# In[62]:


x = range(10)

y1 = [x ** 0.5 for x in x]
y2 = [x ** 3 for x in x]
y3 = [math.tan(x) for x in x]
y4 = [2 ** x for x in x]

plt.figure(figsize=(16, 16))
plt.title('All equations plot')

plt.plot(x, y1, c='orange', label='Equation: $y = \sqrt{x}$')
plt.plot(x, y2, c='red', label='Equation: $y = x^3$')
plt.plot(x, y3, c='blue', label='Equation: $y = tan(x)$')
plt.plot(x, y4, c='green', label='Equation: $y = 2^x$')

plt.legend()
plt.ylabel('$y$')
plt.xlabel('$x$')

plt.show()


# Write the code necessary to write your name on a chart. Use box letters. Bonus: use curves for letters in your name that have curves in them

# In[66]:


y = range(10)
x = 

