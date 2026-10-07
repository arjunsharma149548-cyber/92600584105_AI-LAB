print("=====Welcome to AI ChatBot=====")
print("Type 'Bye' To Exit")           

while True:
    user = input("You : ").lower()

    if "hello" in user:
        print("Bot : How are you!")
    elif "fine" in user:
        print("Bot : Grate.. How can i help you?")
    elif "course" in user:
        print("Bot : You selected AI course.")
    elif "language" in user:
        print("Bot : You have learn a python language for AI course.")
    elif "class" in user:
        print("Bot : You in MCA class.")
    elif "departmant" in user:
        print("Bot : You are in FOCA dep.")
    elif "system" in user:
        print("Bot : You using lenovo pc.")
    elif "collage" in user:
        print("Bot : You are in studying in MU campus")
    elif "bye" in user:
        print("Bot : Good bye!.. Have a nice day.")
        break
    else:
        print("Bot : Sorry!.. I don`t understan youjr qustion?")
        
