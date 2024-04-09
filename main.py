# main.py
from expressions import *


def evaluate_expression(expression, assignment):
    """
    Evaluate a logical expression recursively considering parentheses.
    """
    stack = []
    for char in expression:
        if char in "pqrs":
            stack.append(assignment[char])
        elif char == "~":
            stack.append(negation(stack.pop()))
        elif char == "&":
            stack.append(conjunction(stack.pop(), stack.pop()))
        elif char == "|":
            stack.append(disjunction(stack.pop(), stack.pop()))
        elif char == "^":
            stack.append(xor(stack.pop(), stack.pop()))
        elif char == ">":
            stack.append(implication(stack.pop(), stack.pop()))
        elif char == "<":
            stack.append(biconditional(stack.pop(), stack.pop()))
        elif char == "(":
            stack.append(char)
        elif char == ")":
            inner_expr = []
            while stack[-1] != "(":
                inner_expr.insert(0, stack.pop())
            stack.pop()  # Remove the "("
            result = evaluate_expression("".join(inner_expr), assignment)
            stack.append(result)
    return stack.pop()


def generate_truth_table(expression):
    variables = ['p', 'q', 'r', 's']
    num_variables = len(variables)
    header = " | ".join(variables + [expression])
    print(header)
    print("-" * len(header))
    for i in range(2 ** num_variables):
        assignment = {variables[j]: bool((i >> j) & 1) for j in range(num_variables)}
        result = evaluate_expression(expression, assignment)
        assignment_str = " | ".join(str(int(assignment[var])) for var in variables)
        print(f"{assignment_str} | {int(result)}")


def main():
    print("Enter a logical expression using p, q, r, s and supported operators "
          "(negation: ~, conjunction: &, disjunction: |, exclusive OR: ^, implication: ->, biconditional: <->)")
    expression = input("Expression: ")
    generate_truth_table(expression)


if __name__ == "__main__":
    main()
