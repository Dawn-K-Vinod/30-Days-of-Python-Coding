"""
Author: Dawn K Vinod
Date: 17-11-2024
"""
# Declaring strings
greeting = "Hello"
name = "Dawn"

# String Concatenation
full_greeting = greeting + ", " + name + "!"
print(full_greeting)

# String Slicing
message = "Welcome to Python"
print(message[0:7]) #using positive indexing
print(message[:-10]) #using negative indexing

# Using String Methods
sentence = "python is awesome"
print(sentence.lower())
print(sentence.upper())
print(sentence.split())
print(sentence.replace("awesome", "great"))

# Escape Characters
quote = "He said, \"Python is amazing!\""
print(quote)