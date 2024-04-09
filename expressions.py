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
