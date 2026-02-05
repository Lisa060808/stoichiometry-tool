

# Create a set of questions 
# Ask for a hydrocarbon as I know that the rest are O2, H20, CO2 
# Store those answers into a dictionary 
# aCXHx + bO2 => cH2O + dCO2 

hydrocarbon = input('Enter the hydrocarbon: ').upper()
initial_moles_hydrocarbon = float(input(f'Enter {hydrocarbon} moles: '))
initial_mole_oxygen = float(input('Enter O2 moles: '))
stoic_hydrocarbon = float(input(f'Enter the stoichiometry coefficient of {hydrocarbon}: '))
stoic_oxygen = float(input('Enter the stoichiometry coefficient of O2: '))
stoic_water = float(input('Enter the stoichiometry coefficient of H2O: '))
stoic_carbon_dioxide = float(input('Enter the stoichiometry coefficient of CO2: '))

# Answer storage 
reaction = {
'reactants': {
    hydrocarbon : initial_moles_hydrocarbon, 
    'O2' : initial_mole_oxygen
    },
'stoichiometry' : {
    hydrocarbon : stoic_hydrocarbon, 
    'O2' : stoic_oxygen, 
    'H2O' : stoic_water, 
    'CO2' : stoic_carbon_dioxide
    }

}

# Calculating limiting reagent 

mole_ratio = {}

for species, initial_moles in reaction['reactants'].items(): 
    required_moles = reaction['stoichiometry'][species]
    mole_ratio[species] = initial_moles / required_moles

Limiting_reagent = min(mole_ratio, key=mole_ratio.get)

# Calculating how much is being formed or used 
# LR is know we can find extent of reaction assumiing 100% efficiency 
# form a dictionary of formed and used 

extent_of_reaction = reaction['reactants'][Limiting_reagent] / reaction['stoichiometry'][Limiting_reagent]


moles_reacted_or_formed = {}

for species, coefficient in reaction['stoichiometry'].items():
    moles_reacted_or_formed[species] = extent_of_reaction * coefficient

# Unpack the dictionary to reacted and product

reacted_moles = {}

for species, moles in moles_reacted_or_formed.items():
    if species in reaction['reactants']:
        reacted_moles[species] = moles

product_moles = {}

for species, moles in moles_reacted_or_formed.items():
    if species not in reaction['reactants']:
        product_moles[species] = moles


# Calculate how much is left 
remaing_moles = {}

for species, reacted in reacted_moles.items():
    if species == Limiting_reagent: 
        print(f'{species} is the limiting reagent')
    else: 
        remaing_moles[species] = reaction['reactants'][species] - reacted


# Print what is left 
for species, moles_left in remaing_moles.items():
    print(f'{moles_left} moles of {species} left')

# Print what is formed 
for species, moles_formed in product_moles.items():
    print(f'{moles_formed} moles of {species} formed')