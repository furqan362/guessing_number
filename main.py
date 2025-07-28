import random
number = random.randint(1, 100)
running = True
print(number)
while running:
    
    guess = int(input("Guess a number between 1 to 100: "))
    if guess == number:
        print("Your guess is correct!")
        running = False
    
    elif guess > number:
        print("Your guess is greater than the number")
    else:
        print("Your guess is less than the number")
        
print("Thank you for playing!")