# 🔰Day 4: Python Tasks  
Welcome to **Day 4** of the **30 Days of Coding** challenge! Today, we will tackle two exciting tasks:  
1. Using `if-elif-else` statements to determine the type of a triangle.  
2. Exploring string manipulation and built-in string methods.  

By the end of today, you’ll strengthen your problem-solving skills and enhance your understanding of Python’s string and logic operations.

---

## 👉Task 1: Determine the Type of Triangle

### Description:
Write a Python program that uses **conditional statements** to classify a triangle based on its three sides. 
The program will validate the input to ensure the sides form a valid triangle and then determine whether it is **Equilateral**, **Isosceles**, or **Scalene**.

---

### Instructions:  
1. Prompt the user to input three positive numbers representing the sides of a triangle.  
2. Use the **triangle inequality theorem** to validate whether the input forms a triangle:
   - The sum of any two sides must be greater than the third side.  
   - If the condition is not satisfied, output: `"Not a triangle"`.  
3. If the sides form a valid triangle:
   - Use **if-elif-else** statements to classify it:
     - `"Equilateral"`: All three sides are equal.  
     - `"Isosceles"`: Exactly two sides are equal.  
     - `"Scalene"`: All three sides are different.
---

### 🔹Example-1:
#### Input:
    Enter the length of the first side: 5
    Enter the length of the second side: 5
    Enter the length of the third side: 5  
#### Expected Output:
    Equilateral

### 🔹Example-2:
#### Input:
    Enter the length of the first side: 10
    Enter the length of the second side: 10
    Enter the length of the third side: 5
#### Expected Output:
    Isosceles

### 🔹Example-3:
#### Input:
    Enter the length of the first side: 5
    Enter the length of the second side: 10
    Enter the length of the third side: 7
#### Expected Output:
    Scalene
    
### 🔹Example-4:
#### Input:
    Enter the length of the first side: 10
    Enter the length of the second side: 20
    Enter the length of the third side: 30 
#### Expected Output:
    Not a triangle
    
---
---

## 👉Task-2: Explore String Manipulation and Methods  

### Description:  
Strings allow you to store and manipulate text data in Python. In this task, you’ll:  
- Learn to declare strings using quotes.  
- Combine strings using **concatenation**.  
- Extract parts of a string using **slicing notation**.  
- Use Python's **string methods** for operations like changing case, splitting, and replacing text.  
- Handle special characters with **escaping techniques**.

---

### Key Concepts:  
1. **String Declaration**: Declare strings using single (`'`) or double (`"`) quotes.  
2. **String Concatenation**: Combine strings using the `+` operator.  
3. **String Slicing**: Extract portions of a string using slicing `[start:end]` notation.  
4. **String Methods**: Use Python’s built-in methods such as:
   - `lower()` and `upper()` to change case.  
   - `split()` to break a string into a list of words.  
   - `replace()` to replace a substring with another.  
5. **Escaping Characters**: Use backslashes (`\`) to handle special characters within strings.

---

### Instructions: 
1. Declare a string with a greeting and a name.  
2. Combine the two strings using concatenation to create a full greeting.  
3. Practice string slicing to extract a part of the string.  
4. Use at least three string methods `lower()`, `upper()`, `split()`, `replace()` or others.  
5. Handle a special character in a string using an escape sequence.  
6. Print the results of all the above operations with explanations.

---

### Example:
#### Code:
```python
# Declaring strings
greeting = "Hello"
name = "Alice"

# String Concatenation
full_greeting = greeting + ", " + name + "!"
print(full_greeting)  # Output: Hello, Alice!

# String Slicing
message = "Welcome to Python"
print(message[0:7]) # using positive indexing
print(message[:-10]) # using negative indexing
# Same Output for both: Welcome

# Using String Methods
sentence = "python is awesome"
print(sentence.lower())  # Output: python is awesome
print(sentence.upper())  # Output: PYTHON IS AWESOME
print(sentence.split())  # Output: ['python', 'is', 'awesome']
print(sentence.replace("awesome", "great"))  # Output: python is great

# Escape Characters
quote = "He said, \"Python is amazing!\""
print(quote)  # Output: He said, "Python is amazing!"

