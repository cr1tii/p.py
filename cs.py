import time
import random
from rich.console import Console

while True:
  print(f"-"*36)
  print('\n\n')
  print('type:')
  print('1. *i1* for typing symbol elemnts')
  print('1. *i2* for showing the periodic tabloip showe of elements')
  print('3. *i3* for chemistry calculations')
  print('4. *i4* to exit')
  print("\n\n\n")
  print(' ask what you like sir?')
  list1 = ["H", "N", "O", "F", "Cl"]
  list2 = ['*hydrogen*', '*Nitrogen*', '*oxygen*', '*Flourine*', '*chlorine*']
  int1 = input(' : ')
  if int1 == 'i1':
    while True:
      input1 = input('  wirte the elemnt short from what you want:  ')

      syn = dict(zip(list1, list2))
      if input1 in syn:
        print('icreasing...')
        time.sleep(1.0)
        console = Console()
        console.print(f"\nthe elemnt for {input1}, is {syn[input1]}!",style="bold yellow")
        time.sleep(0.5)
        print('type *1* to complete ')
        print('type *2* to quiet')
        m1 = input("\n:  ")
        if m1 == '1':
          continue
        elif m1 == '2':
          break
  elif int1 == 'i2':
    print("increasing...")
    time.sleep(2.0)
    c1 = Console()
    c1.print(f"\n"+str(list1)+" does stands for the periodic elemens",style="bold yellow")
    c1.print(f"\n"+str(list2)+" does stand for the names of the periodic elements",style="bold yellow")
    time.sleep(2.0)
    print(f"—"*24)
    print("'~and as you see the names are order as the elements are.'||")
    print("\n~for an example the H in the first does stand for the *hydrogen* that its in the first too.")
    print(f"—"*24)
  elif int1 == 'i3':
    time.sleep(1.0)
    c1 = Console()
    c1.print(list1,style="bold red")
    time.sleep(1.0)
    c1.print("\n here's a simple ex sir to help you calculating the p.e(periodic elements.)", style='bold red')
    time.sleep(0.5)
    c1.print("\n H + O:",style="bold red")
    c1.print('\n2H2 + O2 → 2H2O',style='bold underline yellow')
    time.sleep(0.5)

    print(f"—"*38)
    print('\n1. print1 for a 1 + 1 simple calcuate')
    print('2. print2 for a 1 + 1 + 1 calculate')
    print('3. for a 1 + 1 + 1 + 1 calculate')
    in1 = input(': ')
    class calc:
      def __init__(self, in1 , in2 ,in3):
        self.in1 = in1
        self.in2 = in2
        self.in3 = in3
      def ascalcinrun(self):
        if in1 == '1':
          self.in1()
      @staticmethod
      def as1run():
        while True:
          print('increasing...')
          time.sleep(1.5)
          console = Console()
          console.print(list1,style='bold red')
          in1in1 = input('first p.e: ')
          in2in2 = input('sec p.e: ')
          if in1in1 == 'Cl' and in2in2 == 'F':
            console.print('\n\nCl₂ + F₂ → 2ClF.',style='bold yellow')
            d1 = input('do you want to complete sir?: ')
            if d1 == 'yes':
              continue
          else:
              break
          break
      @staticmethod
      def as2run():
        pass
      @staticmethod
      def as3run():
        pass

    k1 = calc(calc.as1run, calc.as2run , calc.as3run)
    k1.ascalcinrun()

  elif int1 == 'i4':
    break
