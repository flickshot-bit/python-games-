import random
import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def slow_print(text):
    print(text)
    time.sleep(0.5)

def play_lottery():
    balance = 100
    ticket_cost = 5
    jackpot = 1000
    
    clear_screen()
    print("=" * 50)
    print("WELCOME TO THE PYTHON LOTTERY GAME!")
    print("=" * 50)
    print(f"\nYou have ${balance} to play with.")
    print(f"Each ticket costs ${ticket_cost}.")
    print(f"The jackpot is ${jackpot}!")
    
    name = input("\nWhat's your name? ")
    print(f"\nHi {name}! Let's play the lottery!")
    
    playing = True
    while playing:
        print(f"\nYour balance: ${balance}")
        
        if balance < ticket_cost:
            print("Sorry, you don't have enough money to play anymore.")
            break
        
        choice = input(f"\nWould you like to buy a ticket for ${ticket_cost}? (yes/no): ")
        if choice.lower() not in ['yes', 'y']:
            print("Thanks for playing!")
            break
            
        balance -= ticket_cost
        print(f"Ticket purchased! Your new balance: ${balance}")
        
        player_numbers = []
        print("\n--- PICK YOUR NUMBERS ---")
        print("You need to pick 5 different numbers between 1 and 20.")
        
        quick_pick = input("Want me to pick random numbers for you? (yes/no): ")
        
        if quick_pick.lower() in ['yes', 'y']:
            player_numbers = random.sample(range(1, 21), 5)
            print("\nGenerating your lucky numbers...")
            time.sleep(1)
            print(f"Your numbers are: {sorted(player_numbers)}")
        else:
            print("\nEnter your 5 lucky numbers:")
            while len(player_numbers) < 5:
                try:
                    num = int(input(f"Number {len(player_numbers)+1} (1-20): "))
                    if 1 <= num <= 20:
                        if num in player_numbers:
                            print("You already picked that number. Try another one.")
                        else:
                            player_numbers.append(num)
                    else:
                        print("Please enter a number between 1 and 20.")
                except ValueError:
                    print("That's not a valid number. Try again.")
            
            print(f"\nYour chosen numbers: {sorted(player_numbers)}")
        
        print("\n--- LOTTERY DRAW ---")
        print("Drawing the winning numbers...")
        time.sleep(1)
        print("Drum roll please...")
        time.sleep(1)
        
        winning_numbers = random.sample(range(1, 21), 5)
        
        print("\nAnd the numbers are...")
        for num in sorted(winning_numbers):
            time.sleep(0.7)
            print(f"  {num}!", end=" ", flush=True)
        print("\n")
        
        print(f"Winning numbers: {sorted(winning_numbers)}")
        print(f"Your numbers: {sorted(player_numbers)}")
        
        matches = len(set(player_numbers) & set(winning_numbers))
        print(f"\nYou matched {matches} number(s)!")
        
        prize = 0
        if matches == 2:
            prize = 10
            print(f"You won ${prize}!")
        elif matches == 3:
            prize = 50
            print(f"You won ${prize}!")
        elif matches == 4:
            prize = 500
            print(f"WOW! You won ${prize}!")
        elif matches == 5:
            prize = jackpot
            print(f"JACKPOT!!! You won ${prize}!!!")
        else:
            print("No prize this time. Better luck next round!")
        
        balance += prize
        print(f"Your new balance: ${balance}")
        
        again = input("\nWant to play again? (yes/no): ")
        if again.lower() not in ['yes', 'y']:
            playing = False
    
    print("\n--- GAME OVER ---")
    print(f"Thanks for playing, {name}!")
    print(f"You finished with ${balance}.")
    
    if balance > 100:
        print(f"You made a profit of ${balance - 100}! Well done!")
    elif balance < 100:
        print(f"You lost ${100 - balance}. Better luck next time!")
    else:
        print("You broke even! Not bad!")

if __name__ == "__main__":
    play_lottery()