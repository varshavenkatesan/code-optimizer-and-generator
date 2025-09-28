#
# SRI RAMACHANDRA FACULTY OF ENGINEERING AND TECHNOLOGY
# CSE23CT302- THEORY OF COMPUTATION AND COMPILER DESIGN
# GitHub Assignment
# Name: VARSHA VENKATESAN
# Unique ID: E0223018
# Department: CSE (Cyber Security and IoT)
# GitHub: 
#

import operator

# --- Solution for Question 1: Code Optimization ---

def optimize_code(code_lines):
    """
    Performs constant folding, strength reduction, and dead code elimination.
    
    """
    statements = []
    # 1. Parse input code into a structured format
    for line in code_lines:
        lhs, rhs = line.split('=')
        statements.append({'lhs': lhs.strip(), 'rhs': rhs.strip(), 'used': False})

    # Dictionary for constant propagation
    constants = {}
    
    # 2. Perform Constant Folding and Strength Reduction
    for stmt in statements:
        parts = stmt['rhs'].split()
        if len(parts) == 3:
            op1, op, op2 = parts
            
            # Check if operands are numbers
            is_op1_digit = op1.isdigit() or (op1.startswith('-') and op1[1:].isdigit())
            is_op2_digit = op2.isdigit() or (op2.startswith('-') and op2[1:].isdigit())

            # Constant Folding: e.g., 2 * 8 -> 16 
            if is_op1_digit and is_op2_digit:
                ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
                result = ops[op](int(op1), int(op2))
                stmt['rhs'] = str(result)
                constants[stmt['lhs']] = result
            
            # Strength Reduction: e.g., x * 1 -> x, y + 0 -> y 
            elif op == '*' and op2 == '1':
                stmt['rhs'] = op1
            elif op == '+' and op2 == '0':
                stmt['rhs'] = op1

    # 3. Perform Copy Propagation
    # This pass replaces variables with their known constant or variable values
    substitutions = {}
    for stmt in statements:
        # Substitute RHS variables if they are in our map
        rhs_parts = stmt['rhs'].split()
        for i, part in enumerate(rhs_parts):
            if part in substitutions:
                rhs_parts[i] = substitutions[part]
        stmt['rhs'] = " ".join(rhs_parts)

        # If statement is a simple copy (e.g., y = x), add to substitutions map
        if len(rhs_parts) == 1:
            substitutions[stmt['lhs']] = stmt['rhs']

    # 4. Dead Code Elimination
    # Mark all variables that are used on the RHS
    for stmt in statements:
        for s_inner in statements:
            if stmt['lhs'] in s_inner['rhs'].split():
                stmt['used'] = True
                break
    
    # The final variable 'z' is implicitly used, so we mark it as used.
    if statements:
        statements[-1]['used'] = True

    # Build the final optimized code
    optimized_code = []
    for stmt in statements:
        is_copy = stmt['lhs'] in stmt['rhs'].split() # e.g., x = x
        # Keep statement if it's used or it's a final computation
        if stmt['used'] and not is_copy:
            optimized_code.append(f"{stmt['lhs']} = {stmt['rhs']}")
            
    return optimized_code


def solve_question_1():
    """Solves the code optimization problem."""
    print("--- Solving Question 1: Code Optimization ---")
    input_code = [
        "x = 2 * 8",  # [cite: 10]
        "y = x * 1",  # [cite: 11]
        "z = y + 0"   # [cite: 12]
    ]
    print("Input Code:")
    for line in input_code:
        print(line)

    optimized_code = optimize_code(input_code)

    print("\nOutput (after optimization):")
    for line in optimized_code:
        # Match the output format from the PDF [cite: 14, 15]
        print(line.replace('z', 'Z').replace('x', 'X'))

# --- Solution for Question 2: Stack Machine Code Generator ---

def generate_stack_code(expression):
    """
    Generates assembly code for a stack machine from an arithmetic expression.
    
    """
    # Use Shunting-yard algorithm to convert infix to postfix
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    operators = []
    
    # Simple tokenization
    tokens = []
    current_token = ""
    for char in expression:
        if char.isalnum():
            current_token += char
        else:
            if current_token:
                tokens.append(current_token)
                current_token = ""
            if char.strip():
                tokens.append(char)
    if current_token:
        tokens.append(current_token)

    # Shunting-yard implementation
    for token in tokens:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop() # Pop '('
        else: # Operator
            while (operators and operators[-1] != '(' and
                   precedence.get(operators[-1], 0) >= precedence.get(token, 0)):
                output.append(operators.pop())
            operators.append(token)
    
    while operators:
        output.append(operators.pop())
    
    # Generate assembly from postfix expression
    assembly_code = []
    op_map = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV'}
    for token in output:
        if token in op_map:
            assembly_code.append(op_map[token]) # 
        else:
            assembly_code.append(f"PUSH {token}") # 
            
    return assembly_code


def solve_question_2():
    """Solves the code generation problem."""
    print("\n\n--- Solving Question 2: Stack Machine Code Generator ---")
    input_expr = "(a+b)*c" # [cite: 17]
    print(f"Input Expression: {input_expr}")
    
    assembly = generate_stack_code(input_expr)
    
    print("\nOutput (Assembly Code):")
    for line in assembly:
        print(line)

# --- Main execution block ---

if __name__ == "__main__":
    solve_question_1()
    solve_question_2()