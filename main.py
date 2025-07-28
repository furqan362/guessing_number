import random
number = random.randint(1, 100)

attempts = 0  

print(number)

while True:
    
    guess = int(input("Guess a number between 1 to 100: "))
    attempts += 1  

    if guess == number:
        print(f"Your guess is correct! You got it in {attempts} attempts!")
        break
    
    elif guess > number:
        print("Your guess is greater than the number")
    
    else:
        print("Your guess is less than the number")


