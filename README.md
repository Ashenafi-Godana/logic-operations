# Truth Table Generator

This Python script generates a truth table for a given logical expression using up to four variables (p, q, r, and s). It evaluates the expression for all possible combinations of truth values for the variables and displays the truth table along with minterms and maxterms.

## Logical Operators

The following logical operators are implemented:

- Negation (NOT)
- Conjunction (AND)
- Disjunction (OR)
- Exclusive OR (XOR)
- Implication (→)
- Biconditional (↔)

## Usage

To generate truth tables for logical operators, you can use the `truth_table()` function provided in `logical_operators.py`. Additionally, the `minterms_maxterms()` function can be used to extract Minterms (SOP) and Maxterms (POS) from the truth tables.

Example usage:

````python
from logical_operators import truth_table, minterms_maxterms


## Usage

1. Run the script using Python 3.
2. Input the logical expression using variables p, q, r, and/or s. For example:
    ```
    Enter expression using variables (e.g., 'p and q'): p and q or (not r) -> s
    ```
3. The script will generate the truth table for the expression and display it.
4. It will also calculate and print the minterms (SOP) and maxterms (POS) for the expression.

## Features

- Supports logical operators: and, or, not, -> (implication), <-> (biconditional)
- Generates truth tables for expressions using up to four variables
- Calculates minterms (SOP) and maxterms (POS)

## Requirements

- Python 3.x

## Example

````
