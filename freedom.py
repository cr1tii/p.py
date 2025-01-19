import re 

def process_input():
    user_input = input("type what you like sir: ") 
    if re.search(r'\bcircle\b',user_input,re.IGNORECASE):
        list1 = ["circle!"] 
        print(list1[0]) 
    else: 
        print("we couldnt find your intger sir.")

process_input()
