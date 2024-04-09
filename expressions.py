# expressions.py

# Function to evaluate negation
def negation(p):
    return not p

# Function to evaluate conjunction
def conjunction(p, q):
    return p and q

# Function to evaluate disjunction
def disjunction(p, q):
    return p or q

# Function to evaluate exclusive OR (XOR)
def xor(p, q):
    return (p or q) and not (p and q)

# Function to evaluate implication
def implication(p, q):
    return (not p) or q

# Function to evaluate biconditional
def biconditional(p, q):
    return (p and q) or (not p and not q)

def precedence(operator):
    if operator in {'~'}:
        return 3
    elif operator in {'&'}:
        return 2
    elif operator in {'|'}:
        return 1
    return 0

def shunting_yard(expression):
    output = []
    operators = []
    
    for char in expression:
        if char.isalpha():
            output.append(char)
        elif char in {'~', '&', '|', '^', '>', '<'}:
            while operators and precedence(operators[-1]) >= precedence(char):
                output.append(operators.pop())
            operators.append(char)
        elif char == '(':
            operators.append(char)
        elif char == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            operators.pop()  # Discard the '('
    
    while operators:
        output.append(operators.pop())
    
    return output

def evaluate_postfix(expression, assignment):
    stack = []
    for char in expression:
        if char.isalpha():
            stack.append(assignment[char])
        elif char == '~':
            stack.append(negation(stack.pop()))
        elif char == '&':
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(conjunction(op1, op2))
        elif char == '|':
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(disjunction(op1, op2))
        elif char == '^':
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(xor(op1, op2))
        elif char == '>':
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(implication(op1, op2))
        elif char == '<':
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(biconditional(op1, op2))
    return stack.pop()

def evaluate_expression(expression, assignment):
    postfix_expr = shunting_yard(expression)
    return evaluate_postfix(postfix_expr, assignment)
