# dp.py

def unit_propagation(clauses, assignment):
    """
    Performs unit propagation based on an assignment of truth values.
    :param clauses: list of clauses
    :param assignment: dictionary of variable assignments
    :return: True if the formula remains satisfiable after propagation, False if a contradiction is found
    """
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
        return True
    return False


def dp(clauses, assignment):
    """
    Davis-Putnam algorithm for SAT solving.
    :param clauses: list of clauses
    :param assignment: dictionary of variable assignments
    :return: True if the formula is satisfiable, False if not
    """
    if not clauses:
        return True
    if any([len(c) == 0 for c in clauses]):
        return False

    if unit_propagation(clauses, assignment):
        return dp(clauses, assignment)

    var = next(iter(clauses[0]))  # Choose the first variable from the first clause
    return dp([clause for clause in clauses if var not in clause], assignment) or dp([clause for clause in clauses if -var not in clause], assignment)


if __name__ == "__main__":
    # Example usage
    clauses = [{1, -2}, {-1, 2}, {3, -2}]
    assignment = {}
    print("Satisfiable (Davis-Putnam):", dp(clauses, assignment))
