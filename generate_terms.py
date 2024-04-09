# generate_terms.py

def generate_sop(truth_table, variables):
    sop_terms = []
    for assignment, result in truth_table.items():
        if result:  # If the result is true
            term = []
            for var, value in assignment:
                if value:
                    term.append(var)
                else:
                    term.append(f"~{var}")
            sop_terms.append(" & ".join(term))
    return " | ".join(sop_terms)


def generate_pos(truth_table, variables):
    pos_terms = []
    for assignment, result in truth_table.items():
        if not result:  # If the result is false
            term = []
            for var, value in assignment:
                if value:
                    term.append(f"~{var}")
                else:
                    term.append(var)
            pos_terms.append(" | ".join(term))
    return " & ".join(pos_terms)
