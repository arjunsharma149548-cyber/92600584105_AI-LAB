print('========================================================')
print('             NUMBER GUESSING SYSTEM                     ')
print('========================================================')

# Initialize range
l = 1
h = 100

print("Think of a number between 1 and 100.")
print("Respond with 'h' for Higher, 'l' for Lower, or 'c' for Correct.\n")

while l <= h:

    # Calculate the middle number
    g = (l + h) // 2

    print("System Guess:", g)

    # Take user's response
    user = input("You: ").lower().strip()

    # If user's number is higher
    if user == 'h':
        l = g + 1

    # If user's number is lower
    elif user == 'l':
        h = g - 1

    # If system guessed correctly
    elif user == 'c':
        print("\nCorrect number:", g)
        print("System guessed your number!")
        break

    # Invalid input
    else:
        print("Invalid input!")
        print("Please enter only 'h', 'l', or 'c'.")
        print()

# If hints were contradictory
if l > h:
    print("\nYour hints are contradictory!")
    print("Please restart the game and give correct hints.")

print("\n========================================================")
print("                 GAME OVER")
print("========================================================")