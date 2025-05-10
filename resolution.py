# resolution.py

def resolution(clauses):
    """
    Implements the resolution algorithm for SAT solving.
    :param clauses: list of clauses, each being a set of literals
    :return: True if the formula is satisfiable, False if not
    """
    def resolve(c1, c2):
        """Resolve two clauses."""
        resolvents = set()
        for literal in c1:
            if -literal in c2:
                new_clause = (c1 - {literal}) | (c2 - {-literal})
                resolvents.add(frozenset(new_clause))
        return resolvents

    while True:
        new_clauses = set()
        for i, c1 in enumerate(clauses):
            for c2 in clauses[i+1:]:
                new_clauses.update(resolve(c1, c2))
        
        if frozenset() in new_clauses:  # If we get an empty clause, the formula is unsatisfiable
            return False
        if new_clauses.issubset(set(clauses)):
            break
        clauses.update(new_clauses)

    return True  # The formula is satisfiable


if __name__ == "__main__":
    # Example usage
    clauses = [frozenset([1, -2]), frozenset([-1, 2]), frozenset([3, -2])]
    print("Satisfiable (Resolution):", resolution(clauses))
