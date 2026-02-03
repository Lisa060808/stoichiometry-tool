# Reaction Stoichiometry Tool
# Example: C3H8 + O2 -> CO2 + H2O


# This function gives off the dictionary takes no input
def parse_reaction():
    # For now, hardcode a reaction (later you can make it user input)
    reaction = {
        "reactants": {"C3H8": 5, "O2": 20},   # moles available
        "stoichiometry": {"C3H8": 1, "O2": 5, "CO2": 3, "H2O": 4}  # balanced equation
    }
    return reaction

#This function takes a dictionary as a function 

def limiting_reactant(reaction):
    ratios = {}
    for reactant, available in reaction["reactants"].items():
        needed = reaction["stoichiometry"][reactant]
        ratios[reactant] = available / needed
    return min(ratios, key=ratios.get)  # reactant with smallest ratio

'''def calculate_products(reaction):
    lr = limiting_reactant(reaction)
    factor = reaction["reactants"][lr] / reaction["stoichiometry"][lr]
    products = {}
    for species, coeff in reaction["stoichiometry"].items():
        if species not in reaction["reactants"]:  # only products
            products[species] = coeff * factor
    return products

reaction = parse_reaction()
print("Limiting reactant:", limiting_reactant(reaction))
print("Products formed:", calculate_products(reaction))'''