import time
import random
from rich.console import Console
#note class in the start
class att:
  def __init__(self, at1):
    self.at1 = at1
  def as1(self):
    self.at1()
  @staticmethod
  def as1dorun():
    c1 = Console()
    c1.print(f"attention",style="bold underline red on black")
    time.sleep(1.5)
    c1.print(f"this is a simple code to simulate",style="bold red")
    c1.print(f"a chemical environment that includes some random elements",style="bold red")
    c1.print(f"\nyou can type .i2 to view the table that are exists in the list",style="bold pink1")
    time.sleep(1)
def sf():
  print('simple sf')

e1 = att(sf)
e1.as1dorun() # the end of note class

# list menu loop
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
  # i1 command in list menu
  if int1 == 'i1':
    while True:
      console = Console()
      console.print(f"\n(type 1 to exit if you want.)",style="bold underline cyan"      )
      input1 = input('  wirte the elemnt short from what you want:  ')
      syn = dict(zip(list1, list2))
      if input1 in syn:
        print('icreasing...')
        time.sleep(0.0)
        console.print(f"\nthe elemnt for {input1}, is {syn[input1]}!",style="bold yellow")
        time.sleep(0.0)
      elif input1 == '1':
          break
      else:
          console.print(f"\n  symbol not found!.",style="bold red")
          console.print(f"  check i2 to see the elements that exists in the list",style="bold red")
  # i2 command in list menu
  elif int1 == 'i2':
    print("increasing...")
    time.sleep(0.5)
    ll1 = ["H", "N", "O", "F", "Cl", "He", "Ne", "Kr", "Xe", "Rn"]
    ll2 = ['hydrogen','Nitrogen','oxygen', 'Flourine','chlorine','Helium','Neon','Kryton','Xenon','Radon' ]
    for l1 ,l2 in zip(ll1,ll2):
      c1 = Console()
      c1.print(l1,":",l2,style="bold blue")  # i3 command in list menu
  elif int1 == 'i3':
    c1 = Console()
    realist = ['H','O','F','Og', 'Ar','Na','Kr','Xe','Rn']
    c1.print(realist,style="bold red")
    c1.print("\n here's a simple ex sir to help you to get chlorine actions with the p.e list", style='bold red')
    c1.print("\n H + Cl:",style="bold red")
    c1.print('\n H₂ + Cl₂ → 2HCl',style='bold underline yellow')

    print(f"—"*38)
    print('\n1. print1 for a 1 + 1 simple calcuate')
    print('2. print2 to exit i3')
    in1 = input(': ')
    if in1 == '1':
      class rea1:
        def __init__(self):
          pass
        def asrea(self):
          while True:
            inp1 = input("\ntype a symbol (or type 1 to quit): ")
            c1 = Console()
            rea = {
          "H": "H₂ + Cl₂ → 2HCl",
          "N": "N₂ + 3 Cl₂ → 2 NCl₃",
          "O": "O₂ + 2 Cl₂ → 2 OCl₂",
          "F": "F₂ + Cl₂ → 2 ClF",
          "Og": "Og + Cl₂ → OgCl₂",
          "Ar": "Ar + Cl₂ →no reaction",
          "Na": "2Na + Cl₂ → 2NaCl",
          "Kr": "Kr + Cl₂ → KrCl₂",
          "Xe": "Xe + Cl₂ → XeCl₂",
          "Rn": "Rn + Cl₂ → RnCl₂",
      }
            reaction = rea.get(inp1,"symbol not found")
            c1.print(f"\n",reaction,style="bold underline yellow")
            if inp1 == '1':
              break
            else:
              continue
      @staticmethod
      def asrea1():
        pass
      @staticmethod
      def asrea2():
        pass

      roa = rea1()
      roa.asrea()
  # i4 command in list menu
  elif int1 == 'i4':
    break
  else:
      c1 = Console()
      c1.print(f"error, please right a word from the list.",style="bold red")
