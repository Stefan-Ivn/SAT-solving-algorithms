# dpll.py

def dpll(clauses, assignment):
    """
    DPLL algorithm for SAT solving.
    :param clauses: list of clauses
    :param assignment: dictionary of variable assignments
    :return: True if the formula is satisfiable, False if not
    """
    if not clauses:
        return True
    if any([len(c) == 0 for c in clauses]):
        return False

    unit_clause = None
    for clause in clauses:
        if len(clause) == 1:
            unit_clause = next(iter(clause))
            if unit_clause not in assignment:
                assignment[unit_clause] = unit_clause > 0
            break

    if unit_clause:
        for clause in clauses:
            if unit_clause in clause:
                clauses.remove(clause)
            elif -unit_clause in clause:
                clause.remove(-unit_clause)
        return dpll(clauses, assignment)

    var = next(iter(clauses[0]))  # Choose the first variable
    return dpll([clause for clause in clauses if var not in clause], assignment) or dpll([clause for clause in clauses if -var not in clause], assignment)


if __name__ == "__main__":
    # Example usage
    clauses = [{1, -2}, {-1, 2}, {3, -2}]
    assignment = {}
    print("Satisfiable (DPLL):", dpll(clauses, assignment))
