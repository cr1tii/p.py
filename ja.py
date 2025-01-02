import arabic_reshaper
import time
from rich.console import Console 
from colorama import Fore, Style

c1 = Console()
c1.print("please type:",style="underline")
c1.print(f"   1. to see mercedes collection",style="bold")
print(Style.BRIGHT + Fore.BLUE + "   2. to see bmw collection")
c1.print("   3. to see lexus collection",style="bold color(8)")
print("(you can type option 4 in any setuation to close)\n")
class cars:
    def __init__(self, mercedes, bmw , lexus):
        self.mercedes = mercedes
        self.bmw = bmw
        self.lexus = lexus
    def run_menu(self):
        while True:
            s1 = input("     type an option:  ")
            if s1 == str(1):
                self.mercedes()
            elif s1 == str(2):
                self.bmw()
            elif s1 == str(3):
                self.lexus()
            elif s1 == str(4):
                print("wait...")
                break
            else:
                c2 = Console()
                c2.print("\n   error, please type a value from the list\n",style="red")
    @staticmethod
    def mercedes():
         print("\nthis place is empty.\n")
    @staticmethod
    def bmw():
        print('\nthis place is empty yet.\n')
    @staticmethod
    def lexus():
         print('\npass.\n')

a1 = cars(cars.mercedes, cars.bmw, cars.lexus)
a1.run_menu()
