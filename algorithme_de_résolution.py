import re

def parse_formula_input(input_string):
    
    clauses_match = re.findall(r'\{(.*?)\}', input_string)
    if not clauses_match:
        raise ValueError("Invalid input format. Please use the format {¬P v ¬Q v R, ¬R, P, ¬T v Q, T}")

    
    clauses = [re.split(r'\s*v\s*', clause) for clause in clauses_match[0].split(',')]

    
    processed_clauses = []
    for clause in clauses:
        processed_clause = []
        for literal in clause:
            literal = literal.strip()
            if literal.startswith("¬"):
                processed_clause.append(-ord(literal[1]) + ord("A") + 1)
            else:
                processed_clause.append(ord(literal) - ord("A") + 1)
        processed_clauses.append(processed_clause)

    return processed_clauses

def negation(F):
    if isinstance(F[0], list):
        return [[-literal for literal in clause] for clause in F]
    else:
        return [-F]

def mettre_sous_forme_de_clauses(F):
    return [F] if isinstance(F[0], int) else F

def chercher_clauses_resolvantes(clauses):
    result = []
    for i in range(len(clauses)):
        for j in range(i+1, len(clauses)):
            for literal_i in clauses[i]:
                for literal_j in clauses[j]:
                    if abs(literal_i) == abs(literal_j):  
                        resolvant = [literal for literal in clauses[i] if literal != literal_i] + \
                                    [literal for literal in clauses[j] if literal != literal_j]
                        if resolvant not in result: 
                            result.append(resolvant)
    return result

def resolution(F):
    neg_F = negation(F)
    clauses = mettre_sous_forme_de_clauses(neg_F)
    while True:
        new_resolvantes = chercher_clauses_resolvantes(clauses)
        if not new_resolvantes:
            return "F est valide"

        
        for resolvant in new_resolvantes:
            if all(lit not in clauses for lit in resolvant):  
                clauses.append(resolvant)

        
        if [] in clauses:
            return "F est invalide"

def test_resolution():
   
    formula_input = input("Enter the formula (e.g., {¬P v ¬Q v R, ¬R, P, ¬T v Q, T}): ")

    try:
        formula = parse_formula_input(formula_input)
    except ValueError as e:
        print(e)
        return

    print("Formula:", formula)
    print("Result:", resolution(formula))
    print()


test_resolution()












