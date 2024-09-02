weight = float(input('Weight: '))
unit = input("(L)bs or (K)g: ")

if unit.lower() == 'k' :
    converted_weight = weight / 0.45
    unit = 'kilos'
else:
    converted_weight = weight * 0.45
    unit = 'pounds'

print(f"you are {converted_weight} {unit}")