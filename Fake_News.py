# This is Fake News Generator, Who gives you fake news or also this is Funny
import random

subjects = ["Virat kohli","Rohit sharma","Shubhman gill","Sharukh khan","Deepika","Ranveer","Modi ji","Monkey form Mumbai"]

action = ["launches","eats","ridding","swimming","singing","dancing ","laughing "]

places = ["in Mumbai's local train","at Red Fort","in Bathroom","at Public Place","at Gate way of India","at Dubai"]

print("\n1. Do you want to Genetrate News\n2.Do you want to Add any Word\n")
choice = int(input("Enter a choice: "))
if choice == int(1):
    while True:
        sub = random.choice(subjects)
        act = random.choice(action)
        place = random.choice(places)

        headline = f"BREAKING NEWS: {sub} {act} {place}\n"
        print(headline)

        user_input = input("\nDo you want another One(yes/no): \n".lower().strip())
        if user_input == "no":
            break


elif choice == int(2):
    print("What do you want to Change:-\n1. Subject\n2. Action\n3. Places")
    choice1 = int(input("Enter your choice:"))
    if choice1 == int(1):
        add_subject = input("Enter a Subject: ".capitalize())
        subjects.append(add_subject)
        
    elif choice1 == int(2):
        add_action = input("Enter a Action: ".lower())
        action.append(add_action)
        
    elif choice1 == int(3):
        add_place = input("Enter a Place: ")
        places.append(add_place)
        
    else:
        print("You Entered Wrong Choice !..")


    while True:
        sub = random.choice(subjects)
        act = random.choice(action)
        place = random.choice(places)

        headline = f"BREAKING NEWS: {sub} {act} {place}\n"
        print(headline)

        user_input = input("\nDo you want another One(yes/no): \n".lower().strip())
        if user_input == "no":
            break


else:
    print("You Entred Wrong Choice!...")


print("\nThanks for using Fake News Generator!.. GoodBye :)")
