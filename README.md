# Code Optimizer and Stack Machine Code Generator

This project is a Python implementation of two core compiler design concepts: code optimization and code generation. It was created as a solution for the "GitHub Assignment" for the course **CSE23CT302 - Theory of Computation and Compiler Design** at **Sri Ramachandra Faculty of Engineering and Technology**.

---
## Project Description

The script is divided into two main parts:
1.  **Code Optimizer**: This part of the program takes a sequence of simple arithmetic assignments and applies several optimization techniques:
    * **Constant Folding**: Evaluates expressions with constant values (e.g., `2 * 8` becomes `16`).
    * **Strength Reduction**: Replaces expensive operations with cheaper ones (e.g., `x * 1` becomes `x`).
    * **Dead Code Elimination**: Removes code that does not affect the program's result.

2.  **Stack Machine Code Generator**: This part translates a given arithmetic expression into a sequence of assembly instructions for a simple stack-based machine.
---
## 🛠️ How to Run
### **Requirements**
* Python 3.x

### **Execution**
No external libraries are needed. Save the code as a Python file (e.g., `compiler_tasks.py`) and run it from your terminal:
python compiler_tasks.py

### **Assignment Problems & Output**
This script directly solves the two problems outlined in the assignment.

**Problem 1: Code Optimization**
**Task:** Implement a program that detects redundant computations, dead code, and strength reduction.
**Input:**
x = 2 * 8 <br>
y = x * 1 <br>
z = y + 0 <br>
**Expected Output:**
x = 16 <br>
Z = X <br>

**Problem 2: Stack Machine Code Generation**
**Task:** Implement a simple code generator that translates arithmetic expressions into target assembly for a stack machine.
**Input:** (a+b)*c
**Expected Output:**
PUSH a <br>
PUSH b <br>
ADD <br>
PUSH c <br>
MUL <br>
