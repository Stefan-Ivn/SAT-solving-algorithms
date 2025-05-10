def resolution(clauses):
    new_clauses = set()  # Set to store new clauses generated during resolution
    stop_condition_met = False  # Control variable to stop the function if necessary

    # Convert the set of clauses into a list so that we can use indices for comparison
    clauses_list = list(clauses) 

    # Iterate over each pair of clauses
    for i, c1 in enumerate(clauses_list):
        for c2 in clauses_list[i + 1:]:
            new_clauses.update(resolve(c1, c2))  # Add resolved clauses to the new_clauses set

    # Check if an empty clause is found, meaning the formula is unsatisfiable
    if frozenset() in new_clauses:  
        stop_condition_met = True

    # If the new clauses are a subset of the original clauses, we stop the resolution process
    if new_clauses.issubset(clauses):  
        stop_condition_met = True

    if stop_condition_met:  # If stopping condition is met, return False (unsatisfiable)
        return False

    clauses.update(new_clauses)  # Add the new clauses to the original set of clauses

    return True  # Formula is satisfiable

def resolve(c1, c2):
    # This function returns the resolvent of two clauses
    resolvent = set()
    for literal in c1:
        if -literal not in c2:  # Add literal if its negation is not in the second clause
            resolvent.add(literal)
    for literal in c2:
        if -literal not in c1:  # Add literal if its negation is not in the first clause
            resolvent.add(literal)
    return resolvent

if __name__ == "__main__":
    # Example of usage: clauses to test the resolution algorithm
    clauses = [frozenset([1, -2]), frozenset([3, -2])]
    print("Satisfiable (Resolution):", resolution(set(clauses)))  # Output the result of the resolution
