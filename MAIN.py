import random
n = random.randint(1,100)
a = -1
guesses = 1 
print("Guess the number between 1 to 100")
while (a != n):
    a = int(input("Guess the number: "))
    if (a<n):
        print("Enter higher number please")
        guesses +=1
    elif (a>n):
        print("Enter lower number please")
        guesses +=1

print(f"You Guessed the number {n} correctly in {guesses} attempts. Congrats!")