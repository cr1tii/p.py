import re 

def process_input():
    user_input = input("type what you like sir: ") 
    list1 = ["time"]
    if re.search(list1[0],user_input,re.IGNORECASE): 
        print(list1[0]) 
    else: 
        print("we couldnt find your intger sir.")

process_input()
