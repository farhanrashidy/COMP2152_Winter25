# COMMENTS
# Sample Coding Questions 01 Week 01
"""
Name: Sheikh Mohammad Farhan Rashidy
Student Id: 101512659
"""

# DEFINING VARIABLE
number = [1, 4, 7, 9]

# ORDER OF OPERATIONS
a = 1
b = 2
c = 3
d = 4

e = a - b ** c // d + a % c
print(e)
e = ((a - ((b ** c) // d)) + (a % c))
print(e)

# FORMATTING
temperature = 32.6
rounded_temp = f"{temperature:.3f}"
print(rounded_temp)

# COMMON FUNCTIONS
userAge = int(input("Please enter your age: "))
print(f"Now showing the shop items filtered by age: {userAge}")
