def react_with_chlorine(element):
    reactions = {
        "H": "H₂ + Cl₂ → 2 HCl",
        "N": "N₂ + 3 Cl₂ → 2 NCl₃",
        "O": "O₂ + 2 Cl₂ → 2 OCl₂",
        "F": "F₂ + Cl₂ → 2 ClF",
        "Cl": "Cl₂ + Cl₂ → 2 Cl₂",
        "He": "No reaction",
        "Ne": "No reaction",
        "Kr": "Kr + Cl₂ → KrCl₂",
        "Xe": "Xe + Cl₂ → XeCl₂",
        "Rn": "Rn + Cl₂ → RnCl₂"
    }
    
    return reactions.get(element, "Element not found")

# طلب الإدخال من المستخدم
element = input("Enter the element symbol (e.g., H, N, O, F, Cl, He, Ne, Kr, Xe, Rn): ")

# عرض التفاعل
print(react_with_chlorine(element))
