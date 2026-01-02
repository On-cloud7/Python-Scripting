# Variables in Python

A **variable** in Python is used to store data in memory.  
It acts as a container that holds a value which can be used and modified during program execution.

---

## What is a Variable?
- A variable is created when you assign a value to it.
- Python does not require explicit type declaration.
- The type of a variable is determined at runtime.

---

## Variable Assignment
- Variables are assigned using the `=` operator.
- Python supports single and multiple assignments.

---

## Rules for Naming Variables
- Must start with a letter (a–z, A–Z) or underscore (`_`)
- Cannot start with a number
- Can contain letters, numbers, and underscores
- Case-sensitive (`name` and `Name` are different)
- Cannot be a Python keyword

---

## Valid Variable Names
- `name`
- `age`
- `_count`
- `total_marks`
- `userName`

---

## Invalid Variable Names
- `1name`
- `total-marks`
- `class`
- `user name`

---

## Types of Variables in Python

### 1. Local Variables
- Defined inside a function
- Accessible only within that function

### 2. Global Variables
- Defined outside all functions
- Accessible throughout the program

### 3. Instance Variables
- Associated with an object
- Defined inside a class constructor

### 4. Class Variables
- Shared by all instances of a class

---

## Dynamic Typing
- Python allows changing the type of a variable during execution.
- The same variable can store different data types at different times.

---

## Multiple Assignment
- Python allows assigning multiple variables in one line.
- Values are assigned based on position.

---

## Variable Reassignment
- Variables can be reassigned to new values at any time.
- The old value is replaced by the new one.

---

## Constants in Python
- Python does not have true constants.
- Variables written in uppercase are treated as constants by convention.

---

## Checking Variable Type
- The `type()` function is used to identify the data type of a variable.

---

## Deleting Variables
- The `del` keyword is used to remove a variable from memory.

---

## Best Practices
- Use meaningful variable names
- Follow snake_case naming convention
- Avoid using Python keywords as variable names
- Keep variable names short but descriptive

---

## Summary
Variables are fundamental to Python programming and are used to store, update, and manipulate data efficiently.

---
# Naming Conventions in Programming (Python Focus)

Naming conventions define **how variable, function, class, and constant names are written**.  
They improve code readability and maintainability.

---


## 1. camelCase
- First word starts with a lowercase letter  
- Each new word starts with an uppercase letter  
- No spaces or underscores  

### Usage
- Common in Java, JavaScript  
- Sometimes used for variables and functions  

### Example
- userName  
- totalMarks  
- getUserData  

---

## 2. snake_case
- All letters are lowercase  
- Words are separated using underscores (`_`)  

### Usage
- **Most commonly used in Python**  
- Recommended by PEP 8 for variables and functions  

### Example
- user_name  
- total_marks  
- get_user_data  

---

## 3. PascalCase
- First letter of every word is uppercase  
- No underscores or spaces  

### Usage
- Used for **class names** in Python  
- Common in Java, C#, Python (OOP)  

### Example
- UserName  
- TotalMarks  
- GetUserData  

---