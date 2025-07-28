import random

def guess_number():

    number = random.randint(1, 100)
    attempts = 0  

    print(number)
    while True:
        try:
            guess = int(input("Guess a number between 1 to 100: "))
        except ValueError:
            return "please enter correct value"
            
        attempts += 1  

        if guess == number:
            print(f"Your guess is correct! You got it in {attempts} attempts!")
            break
        
        elif guess > number:
            print("Your guess is greater than the number")
        
        else:
            print("Your guess is less than the number")

while True:
    guess_number()
    choise=input("enter e for exit: \n enter c for continue: ").lower()
    if choise=="c":
        continue
    else:
        exit
