max_attempts = 5

for attempts_left in range(max_attempts, 0, -1):
    user_input = input(f"You have {attempts_left} attempts left. Enter your guess: ")
    if user_input == "correct":
        print("Correct!")
        break
else:
    print("No attempts left. Game over.")   