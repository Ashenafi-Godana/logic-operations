# check_property.py
from expressions import evaluate_expression

def check_property(expression, variables):
    num_variables = len(variables)
    is_tautology = True
    is_contradiction = True

    for i in range(2 ** num_variables):
        assignment = {variables[j]: bool((i >> (num_variables - 1 - j)) & 1) for j in range(num_variables)}
        result = evaluate_expression(expression, assignment)
        is_tautology = is_tautology and result
        is_contradiction = is_contradiction and not result

    if is_tautology:
        print(f"The expression '{expression}' is a tautology.")
    elif is_contradiction:
        print(f"The expression '{expression}' is a contradiction.")
    else:
        print(f"The expression '{expression}' is neither a tautology nor a contradiction.")

def main():
    print("Enter a logical expression using variables and supported operators "
          "(negation: ~ or not, conjunction: &, disjunction: |, exclusive OR: ^, implication: ->, biconditional: <->)")
    expression = input("Expression: ")
    variables = sorted(set(char for char in expression if char.isalpha()))  # Extract variables from the expression
    check_property(expression, variables)


if __name__ == "__main__":
    main()
