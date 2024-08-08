import random

def main():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 0 and 999. Can you guess it?")
    
    secret_number = random.randint(0, 999)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        guess = int(input("\nEnter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Hint: The number is greater than your guess.")
        elif guess > secret_number:
            print("Hint: The number is smaller than your guess.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
            break
        
        remaining_attempts = max_attempts - attempts
        if remaining_attempts > 0:
            print(f"You have {remaining_attempts} attempts left.")
        else:
            print(f"Sorry, you've run out of attempts. The secret number was {secret_number}.")
    
    print("\nThank you for playing!")

if __name__ == "__main__":
    main()
