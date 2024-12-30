import time
import random
from rich.console import Console

class att:
  def __init__(self, at1):
    self.at1 = at1
  def as1(self):
    self.at1()
  @staticmethod
  def as1dorun():
    c1 = Console()
    c1.print(f"attention",style="bold italic underline black on white")
    time.sleep(1)
    c1.print(f"this is a simple code to simulate",style="bold red")
    time.sleep(0.5)
    c1.print(f"a chemical environment that includes some random elements",style="bold red")
    time.sleep(1)
    c1.print(f"\nyou can type .i2 to view the table that are exists in the list",style="bold pink1")
    time.sleep(1.7)
def sf():
  print('simple sf')

e1 = att(sf)
e1.as1dorun()


while True:
  print(f"-"*36)
  print('\n\n')
  print('type:')
  print('1. *i1* for typing symbol elements')
  print('1. *i2* for showing the periodic table of elements ')
  print('3. *i3* for chlorine actions with elements')
  print('4. *i4* to exit')
  print("\n\n\n")
  print(' ask what you like sir?')
  list1 = ["H", "N", "O", "F", "Cl", "He", "Ne", "Kr", "Xe", "Rn"]
  list2 = ['*hydrogen*', '*Nitrogen*', '*oxygen*', '*Flourine*', '*Chlorine*', '*Helium*','*Neon*','*Kryton*','*Xenon*','*Radon*' ]
  int1 = input(' : ')
  if int1 == 'i1':
    while True:
      input1 = input('  wirte the elemnt short from what you want:  ')
      
      syn = dict(zip(list1, list2))
      if input1 in syn:
        print('icreasing...')
        time.sleep(0.0)
        console = Console()
        console.print(f"\nthe elemnt for {input1}, is {syn[input1]}!",style="bold yellow")
        time.sleep(0.0)
        print('type *1* to complete ')
        print('type *2* to quiet')
        m1 = input("\n:  ")
        if m1 == '1':
          continue
        elif m1 == '2':
          break
  elif int1 == 'i2':
    print("increasing...")
    ll1 = ["H", "N", "O", "F", "Cl", "He", "Ne", "Kr", "Xe", "Rn"]
    ll2 = ['hydrogen','Nitrogen','oxygen', 'Flourine','chlorine','Helium','Neon','Kryton','Xenon','Radon' ]
    time.sleep(2.0)
    for l1 ,l2 in zip(ll1,ll2):
      c1 = Console()
      c1.print(l1,":",l2,style="bold on white")
      time.sleep(1)
    @staticmethod
    def cons():
      print(f"—"*24)
      print("'~and as you see the names are order as the elements are.'||")
      print("\n~for an example the H in the first does stand for the *hydrogen* that its in the first too.")
      print(f"—"*24)

    cons()
  elif int1 == 'i3':
    time.sleep(1.0)
    c1 = Console()
    c1.print(list1,style="bold red")
    time.sleep(1.0)
    c1.print("\n here's a simple ex sir to help you to get chlorine actions with the p.e list", style='bold red')
    time.sleep(0.5)
    c1.print("\n Cl + H:",style="bold red")
    c1.print('\nCl₂ + H₂ → 2HCl',style='bold underline yellow')
    time.sleep(0.5)
    
    print(f"—"*38)
    print('\n1. print1 for a 1 + 1 simple calcuate')
    print('2. print2 to exit i3')
    in1 = input(': ')
    class calc:
      def __init__(self, in1 , in2 ,rwc):
        self.in1 = in1
        self.in2 = in2
        self.rwc = rwc
      def ascalcinrun(self):
        if in1 == '1':
          self.in1()
        elif in1 == '2':
          self.in2()
      @staticmethod
      def as1run():
        while True:
          print('increasing...')
          time.sleep(1.5)
          console = Console()
          console.print(list1,style='bold red')
      @staticmethod
      def as2run():
        print('just wait...')
        time.sleep(0.7)
        return

      @staticmethod
      def rwc(element):
        rea = {
          "H": "H₂ + Cl₂ → 2HCl",
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
        return rea.get(element,"not found")

      element = input("type a symbol from the list sir: ")
      print(rwc(element))
    
    k1 = calc(calc.as1run, calc.as2run , calc.rwc)
    k1.ascalcinrun()
    
  elif int1 == 'i4':
    break