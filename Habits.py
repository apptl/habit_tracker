import json
from datetime import date
import sys

#function to write to a file
def write_to_file(output):
    with open('Habits.txt','a') as file:
        file.write(output+"\n")

#function to read file content
def read_from_file():
    with open('Habits.txt','r') as file:
        lines = file.readlines()
        if not lines:         
            return None
        return lines  

def initialize_json(gym,water,study,pnl,pickleball):
    data = {
        "Date": date.today().isoformat(),
        "Gym": gym,
        "water": water,
        "study": study,
        "green P&L": pnl,
        "Pickleball": pickleball,
    }
    return data
    
#print format template 
def print_summary(entry):
    
    data = json.loads(entry)
    print("\n===== Summary =====")
    print(f"Date: {data['Date']}")
    print(f"Gym: {'Yes' if data['Gym'] else 'No'}")
    print(f"Water: {data['water']} L")
    print(f"Study: {'Yes' if data['study'] else 'No'}")
    print(f"Green P&L: {'Yes' if data['green P&L'] else 'No'}")
    print(f"Pickleball: {'Yes' if data['Pickleball'] else 'No'}")
    print("======================\n")

#fucntion to get user input for streaks 
def yes_or_no(prompt):
    user_response = input(prompt).strip().lower()
    if( user_response == "yes"):
        return True
    elif(user_response == "no"):
        return False
    else:
        print("please type a Valid Answer(Yes/No)")
        return yes_or_no(prompt)
    
#Water input failsafe. incase user enters non float input
def ask_float(prompt):
    while True:
        user_input = input(prompt).strip()

        try:
            return float(user_input)
        except ValueError:
            print("Please enter a valid number (e.g. 2 or 2.5)")

#Create json object and populate it with user input and write to a file
def log_habits():

    gym = yes_or_no("Did you go to the Gym(Yes/No) ?")
    water = ask_float("How many liters of water did you drink?")
    study = yes_or_no("Did you study(Yes/No) ?")
    pnl = yes_or_no("Did you have a green day(Yes/No) ?")
    pickleball = yes_or_no("Did you go play pickleball(Yes/No) ?")
    habits= initialize_json(gym, water, study, pnl, pickleball)
    json_string = json.dumps(habits)
    write_to_file(json_string)
    return json_string

#Function to print the last entry 
def print_last_entry():
    lines = read_from_file()
    if not lines:
        print("No previous entries.")
        return
    last_entry = lines[-1].strip() 
    print_summary(last_entry)

#Fucntion to print the entire history
def print_full_history ():
    lines = read_from_file()
    if not lines:
        print("No Data")
        return
    for line in lines:
        print_summary(line)

# Defining main function
def main():
    while True:
        function_selection = input("1. Log today\n2. View last entry\n3. View full history\n4. Exit\n")
        if(function_selection == "1"):
            todays_habit = log_habits()
            print_summary(todays_habit)
        elif(function_selection == "2"):
            print_last_entry()
        elif(function_selection == "3"):
            print_full_history()
        elif(function_selection == "4"):
            print("Have a great day!!")
            sys.exit()
        else:
            print("Invalid option. Please choose 1–4.")


# Using the special variable 
# __name__
if __name__=="__main__":
    main()
