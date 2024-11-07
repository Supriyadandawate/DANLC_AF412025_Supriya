#!/usr/bin/env python
# coding: utf-8

# ## 1. Write a Python program to find the number of times 4 appears in the tuple.
# Input:
# tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 )
# Output: 3

# In[ ]:


# Given tuple
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7)

# Counting the occurrences of 4 in the tuple
count_of_fours = tuplex.count(4)

# Displaying the result
print("The number 4 appears", count_of_fours, "times in the tuple.")


# ## 2.Write a Python program to convert a list to a tuple.
# 
# Input: listx = [5, 10, 7, 4, 15, 3]
# Output: (5, 10, 7, 4, 15, 3)

# In[2]:


# Given list
listx = [5, 10, 7, 4, 15, 3]

# Converting the list to a tuple
tuplex = tuple(listx)

# Displaying the result
print(tuplex)


# ## 3. Write a Python program to calculate the sum of the numbers in a given tuple.
# Input: tuples_list = [(1, 2), (3, 4), (5, 6)]
# Output:sum of values in the tuples:21

# In[3]:


# Given list of tuples
tuples_list = [(1, 2), (3, 4), (5, 6)]

# Calculating the sum of values in the tuples
total_sum = sum(sum(tup) for tup in tuples_list)

# Displaying the result
print("Sum of values in the tuples:", total_sum)


# ## 4.Write a python program and iterate the given tuples
# Input:
# employee1 = ("John Doe", 101, "Human Resources", 60000)
# employee2 = ("Alice Smith", 102, "Marketing", 55000)
# employee3 = ("Bob Johnson", 103, "Engineering", 75000)
# Output:Employee Records:
# Name: John Doe,
# EmployeeID: 101,
# Department: Human Resources,
# Salary: $60000
# 
# Name: Alice Smith,
# EmployeeID: 102,
# Department: Marketing,
# Salary: $55000
# 
# Name: Bob Johnson,
# EmployeeID: 103,
# Department: Engineering,
# Salary: $75000

# In[4]:


# Given employee tuples
employee1 = ("John Doe", 101, "Human Resources", 60000)
employee2 = ("Alice Smith", 102, "Marketing", 55000)
employee3 = ("Bob Johnson", 103, "Engineering", 75000)

# List of employees
employees = [employee1, employee2, employee3]

# Displaying Employee Records
print("Employee Records:")
for employee in employees:
    print(f"Name: {employee[0]},")
    print(f"EmployeeID: {employee[1]},")
    print(f"Department: {employee[2]},")
    print(f"Salary: ${employee[3]}\n")


# In[ ]:




