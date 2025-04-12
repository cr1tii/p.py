import re
import random 
from rich.console import Console

def chlorina():
    while True:
        l1 =[["hi", "hi", "nice to meet you","hi,im Chloe!"],["i want to know about chimstery", "sure! what do you want to know about?"], "chimestry", "ofc!", "sure i can help you!",["elements", "okay which one?","chlorine"],["chlorine", "i can help you whatever you like!.."]] #the list
        int1 = input("chat with chloe : ")
        add = l1.pop(0) # here he should pop a list from l1 
        l2 = [] #L2 list
        l2.append(add) #and then adding it to l2 list
        if re.search(l2[0][0],int1 ,re.IGNORECASE): #the search line code
            print(random.choice(l2[0][1:3])) # the first message from l2 matches with int1(input) he should choose a normal message from 1:3 (canceled the first message cause its the True reason) and then print it
        elif re.search(l2[0][0],int1,re.IGNORECASE) is None: # here if the message didnt match
            l1.append(l2.pop(0)) #he pop the list from L2 
            add2 = l1.pop(0) 
            l2.append(add2) # and then adding it again to L1 so he can repeat searching when the input asks again
            print(random.choice(l2[0][1:3])) # then he should pop a random choice to right it 
        elif int1 == "q":
            print("quiting...")
            return        
                
chlorina()

