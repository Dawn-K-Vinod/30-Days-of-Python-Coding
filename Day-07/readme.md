# 🔰Day 7: Advanced List Operations and Loop Control  

Welcome to **Day 7** of the **30 Days of Coding** challenge! 🎉 Today, we will explore **advanced list operations** and **loop control mechanisms** in Python. Mastering these concepts will make your coding more efficient and structured.

---

## 👉Task 1: Advanced List Operations  

### Description:  
In this task, you will explore advanced list methods to manipulate a list step-by-step, demonstrating key Python list functionalities.

### Instructions:
[ Note: Print the current list after applying each method.]
1. Create an empty list.  
2. Perform the following operations on the list in sequence:  
   - Ask user to enter 3 numbers and append each number using `.append()`.
     <br>(use loop to ask and append )
   - Extend the current list with another list using `.extend()`.
     <br>(another list: [98,67,37,98] )
   - Insert an element at a specific position using `.insert()`.
     <br>(try inserting 13 in the 3rd index position )
   - Remove an element by value using `.remove()`.
     <br>(try removing the value 67 )
   - Pop an element from the list using `.pop()`.
     <br>(try simple pop() and also try popping the value at index 0 )
   - Count the occurrences of an element using `.count()`.
     <br>(try counting the value 98 )
   - Find the index of an element using `.index()`.
     <br>(try to find the index of 37 from the current list )
   - Sort the list in ascending order using `.sort()`.
    <br> (try to find the ascending order of list by sort() and descending order of list by sort(reverse=True) )
   - Reverse the list using `.reverse()`.  
3. Split a string into a list using `.split()`.
   (try splitting the string "python is cool" into a list)

### Examples  
#### Input:
    Enter a number:52
    Enter a number:39
    Enter a number:84
#### Output:
    The list after appending 3 numbers: [52, 39, 84]
    The list after extending [98,67,37,98] is: [52, 39, 84, 98, 67, 37, 98]
    The list after inserting 13 in the 3rd index: [52, 39, 84, 13, 98, 67, 37, 98]
    The list after removing 67: [52, 39, 84, 13, 98, 37, 98]
    The list after simply using pop(): [52, 39, 84, 13, 98, 37]
    The list after popping the value at index 0: [39, 84, 13, 98, 37] 
    Occurence of value 98: 1
    The index of 37: 4
    The list after reversing: [37, 98, 13, 84, 39]
    The list in ascending order: [13, 37, 39, 84, 98]
    The list in descending order: [98, 84, 39, 37, 13]
    Output after appliying split() to a string: ['python', 'is', 'cool']


---
---

## 👉Task 2: Using `break`, `continue`, and `pass`  

### Description:  
In this task, you will practice using `break`, `continue`, and `pass` statements to control the flow of a loop while processing a list.

### Instructions:  
1. Create a list of numbers provided by the user.<br>(use any loop to take inputs from the user and append each number to the list)  
2. Use a `for` loop to process the list and do the following:  
   - **Break**: Stop the loop when a specific condition is met (e.g., encountering the number 0).  
   - **Continue**: Skip the processing for even numbers, only displaying odd numbers.  
   - **Pass**: Use `pass` to handle items without performing any action if the number is negative.  
3. Display the processed results at each step.  

### Examples:  
#### Input:
    Enter a number:10
    Enter a number:13
    Enter a number:24
    Enter a number:35
    Enter a number:-47
    Enter a number:0
    Enter a number:68
#### Output:
    Skipping even number: 10
    Processing odd number: 13
    Skipping even number: 24
    Processing odd number: 35
    Negative number encountered, no action taken: -47
    Encountered 0, stopping the loop.

    Processed numbers: [13, 35]
---

### -Summary-
Day 7 challenges you to go deeper into Python by learning **list manipulations** and **loop control statements**. 
Practice these tasks thoroughly to build a strong foundation for more advanced programming concepts. Happy coding! 🚀  
