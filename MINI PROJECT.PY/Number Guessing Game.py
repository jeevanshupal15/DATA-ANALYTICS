import random

def play_game():
    difficulty = input("Choose difficulty - Easy (1-50), Medium (1-100), Hard (1-500): ").lower()
    
    if difficulty == "easy":
        low, high, max_attempts = 1, 50, 7
    elif difficulty == "hard":
        low, high, max_attempts = 1, 500, 10
    else:
        low, high, max_attempts = 1, 100, 7
    
    target = random.randint(low, high)
    attempts = 0
    
    print(f"\nI'm thinking of a number between {low} and {high}. You have {max_attempts} attempts.\n")
    
    while attempts < max_attempts:
        guess = input(f"Attempt {attempts + 1}: ")
        
        try:
            guess = int(guess)
        except ValueError:
            print("That's not a valid whole number. Try again.\n")
            continue
        
        attempts += 1
        
        if guess == target:
            print(f"\n🎉 Correct! You guessed it in {attempts} tries.")
            break
        
        diff = abs(guess - target)
        
        if diff <= 5:
            hint = "Very close!"
        elif diff <= 15:
            hint = "Close."
        else:
            hint = ""
        
        if guess < target:
            print(f"Too low! {hint}\n")
        else:
            print(f"Too high! {hint}\n")
        
        if attempts == max_attempts:
            print(f"\nOut of attempts! The number was {target}.")

def main():
    while True:
        play_game()
        again = input("\nPlay again? (y/n): ")
        if again.lower() != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()