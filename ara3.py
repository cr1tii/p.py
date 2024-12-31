import arabic_reshaper
from rich.console import Console 

text = "مرحبا، ارجوك اكتب 1: "
rt = arabic_reshaper.reshape(text)
rv = rt[::-1]
s1 = input(rv)

if s1 == str(1) :
    text1 = "تهاني! إن الكود يعمل بنجاح"
    rt1 = arabic_reshaper.reshape(text1)
    rv1 = rt1[::-1]
    c1 = Console()
    c1.print(f"\n{rv1}",style="bold underline yellow")
else:
    c2 = Console()
    c2.print(f"error, please type an arabic word",style="red")
