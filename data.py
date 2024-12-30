from itertools import combinations

elements = ['H', 'N', 'O', 'F', 'Cl', 'He', 'Ne', 'Kr', 'Xe', 'Rn']

# توليفات لـ 2 عناصر:
for comb in combinations(elements, 2):
    print(comb)

# توليفات لـ 3 عناصر:
for comb in combinations(elements, 3):
    print(comb)
