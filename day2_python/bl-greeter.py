# day2_python exercise solution: bl-greeter.py

# request the user's name
name = input("What's your name? ")

# request the user's DOB
dob = input("What year were you born? ")

# compute the user's age
age = 2026 - int(dob)

# print out the results
print(f"Hello, {name}! You are {age} years old.")