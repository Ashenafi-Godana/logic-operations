# main.py
from expressions import *
from check_property import check_property
from generate_terms import generate_sop, generate_pos

def generate_truth_table(expression, variables):
    truth_table = {}
    num_variables = len(variables)
    
    for i in range(2 ** num_variables):
        assignment = {variables[j]: bool((i >> (num_variables - 1 - j)) & 1) for j in range(num_variables)}
        result = evaluate_expression(expression, assignment)
        truth_table[tuple(assignment.items())] = result
    return truth_table


def generate_truth_table_output(expression, truth_table, variables):
    header = "\t|\t".join(f"{var:^7}" for var in variables + [expression])
    line_length = len(header) + (len(variables) + 1) * 4  # Account for tabs and separators

    print(header)
    print("=" * line_length)
    for assignment, result in truth_table.items():
        assignment_str = "\t|\t".join(f"{str(value):^7}" if isinstance(value, bool) else f"{value!s:^7}" for _, value in assignment)
        # result_str = int(result)
        result_str = "True" if result else "False"
        print(f"{assignment_str} | {result_str:^7}")


def main():
    print('''
          
          This tool generates truth tables for propositional logic formulas. 
          It also checks if the formula is a tautology, contradiction, or neither.
          It also generates the minterms (SOP) and maxterms (POS) of the formula.

          You can enter logical operators using variables and supported operators 
          Supported Operators:
          negation: ~, conjunction: &, disjunction: |, exclusive OR: ^, implication: ->, biconditional: <->)
          
          ''')
    expression = input("Expression: ")
    variables = sorted(set(char for char in expression if char.isalpha()))  # Extract variables from the expression
    truth_table = generate_truth_table(expression, variables)   # A dictionary containing the truth table will be returned
    
    print("\nTruth Table:")
    print()
    generate_truth_table_output(expression, truth_table, variables)
    print()
    check_property(expression, variables)

    generate_terms = {"Minterms (SOP)": generate_sop, "Maxterms (POS)": generate_pos}
    for term_type, generate_term in generate_terms.items():
        terms = generate_term(truth_table, variables)
        print(f"\n{term_type}:")
        print(terms)


if __name__ == "__main__":
    main()
