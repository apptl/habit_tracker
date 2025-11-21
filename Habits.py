from datetime import date
import json
import sys

def create_entry(gym,water,study,pnl,pickleball):
    data = {
        "Date": date.today().isoformat(),
        "Gym": gym,
        "water": water,
        "study": study,
        "green P&L": pnl,
        "Pickleball": pickleball,
    }
    return data
    

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

def load_db():
    try:
        with open("habits.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []

def save_db(data):
    with open("habits.json", "w") as f:
        json.dump(data, f, indent=4)

def print_all():
    data = load_db()
    if not data:
        print("No entries found")
        return

    for entry in data:
        printing_template(entry)

def print_last_entry():
    temp = load_db()
    if not temp:
        print("No entries found")
        return 
    
    data = temp[-1]
    printing_template(data)

def printing_template(entry):

    print("\n===== Summary =====")
    print(f"Date: {entry['Date']}")
    print(f"Gym: {'Yes' if entry['Gym'] else 'No'}")
    print(f"Water: {entry['water']} L")
    print(f"Study: {'Yes' if entry['study'] else 'No'}")
    print(f"Green P&L: {'Yes' if entry['green P&L'] else 'No'}")
    print(f"Pickleball: {'Yes' if entry['Pickleball'] else 'No'}")
    print("======================\n")
    

def log_habits():
    gym = yes_or_no("Did you go to the Gym(Yes/No) ?")
    water = ask_float("How many liters of water did you drink?")
    study = yes_or_no("Did you study(Yes/No) ?")
    pnl = yes_or_no("Did you have a green day(Yes/No) ?")
    pickleball = yes_or_no("Did you go play pickleball(Yes/No) ?")
    entry = create_entry(gym, water, study, pnl, pickleball)
    db = load_db()
    db.append(entry)
    save_db(db)
    return entry


def main():
    while True:
        function_selection = input("1. Log today\n2. View last entry\n3. View full history\n4. Exit\n")
        if(function_selection == "1"):
            log_habits()
            print_last_entry()
        elif(function_selection == "2"):
            print_last_entry()
        elif(function_selection == "3"):
            print_all()
        elif(function_selection == "4"):
            print("Have a great day!!")
            sys.exit()
        else:
            print("Invalid option. Please choose 1–4.")


# Using the special variable 
# __name__
if __name__=="__main__":
    main()
