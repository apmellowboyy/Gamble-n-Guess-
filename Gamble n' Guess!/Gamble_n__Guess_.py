
import random
import sys

def guessingGame():
    wins = 0
    losses = 0
    balance = 500
    
    name = input("What is your name?")
    print(f'Welcome to Gamble N\' Guess, {name}! Place a bet and hope you choose right!\n')

    
    while True:
        ethan = random.randint(1, 10)
        lives = 3
        
        bet = int(input(f"Your balance is ${balance}, how much do you want to bet? "))
        
        while bet > balance or bet <= 0:
            bet = int(input(f"Invalid bet. Your balance is ${balance}, please place a valid bet: "))

        initial_bet = bet

        while lives > 0:
            guess = int(input(f"Guess a number between 1 and 10!\n"))
            if guess > ethan:
                lives -= 1
                bet = max(bet - int(bet * 0.2), 0)  # Decrease bet by 20% or set to 0
                print(f"Too high, try again! You have {lives} lives remaining. Current bet: ${bet}")
            elif guess < ethan:
                lives -= 1
                bet = max(bet - int(bet * 0.6), 0)  # Decrease bet by 20% or set to 0
                print(f"Too low, try again! You have {lives} lives remaining. Current bet: ${bet}")
            elif guess == ethan:
                wins += 1
                balance += bet
                print(f"You got it with {lives} lives remaining!")
                print(f"You won ${bet}!")
                print(f"Total wins: {wins}")
                print(f"Total losses: {losses}")
                break

        if lives == 0:
            losses += 1
            balance -= initial_bet 
            print(f"GAME OVER! You should have guessed {ethan}")
            print(f"You lost your bet of ${initial_bet}...")
            print(f"Total wins: {wins}")
            print(f"Total losses: {losses}")
            if balance <= 0:
                print("You have no more money left. Game over!")
                sys.exit()

        replay = input("Would you like to play another round? y or n?")
        if replay.lower() != "y":
            print(f"Thanks for playing! Total wins: {wins}, Total losses: {losses}, Final balance: ${balance}")
            sys.exit()

guessingGame()
