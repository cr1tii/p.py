import time 
import arabic_reshaper
from rich.console import Console

text1 = "اكتب 1 لعرض بيت من ابيات المتنبي"
rt = arabic_reshaper.reshape(text1)
rv = rt[::-1]
while True:
    class poem:
        def __init__(self,poem1,poem2):
            self.poem1 = poem1
            self.poem2 = poem2
        def show_poem(self):
            console = Console()
            t1 = ".1 اكتب واحد لعرض بيت المتنبي"
            rtt = arabic_reshaper.reshape(t1)
            rvv = rtt[::-1]
            t2 = ".2 اكتب اثنين لعرض قصيدة المتنبي"
            rttt = arabic_reshaper.reshape(t2)
            rvvv = rttt[::-1]
            console.print(f"\n",rvv,"\n",style="underline yellow")
            console.print(rvvv,"\n",style="underline yellow")
            print("or type c to close")
            s2 = input(f"\n      : ")
            if s2 == str(1):
                self.poem1()
            elif s2 == str(2):
                self.poem2()
            else:
                c1 = Console()
                c1.print(f"error.",style="bold red")
                c1.print(f"please choose one from the list\n",style="bold red")
                print("—"*30)
        def runpoem1():
            c2 = Console()
            text2 = "على قدرِ أهلِ العزمِ تأتي العزائمُ"
            rt1 = arabic_reshaper.reshape(text2)
            rv1 = rt1[::-1]
            c2.print(f"\n",rv1, end='', style="underline pink1")
            time.sleep(0.01)
            text3 = "وتأتي على قدرِ الكرامِ المكارمُ"
            rt3 = arabic_reshaper.reshape(text3)
            rv3 = rt3[::-1]
            c2.print(f"\n",rv3,"\n",end='',style="underline pink1")
            time.sleep(0.01)
            print("—"*30)
        def runpoem2():
            print("\nthis place is empty.\n")
            print("—"*30)
    
    finish = poem(poem.runpoem1,poem.runpoem2)
    finish.show_poem()
