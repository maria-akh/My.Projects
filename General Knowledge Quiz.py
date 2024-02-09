import sys

from colorama import init
init()

from colorama import Fore, Style

print("\n")

print(Fore.CYAN + "Welcome to my general knowledge quiz! :)")

print("\n")

playing = input(Fore.WHITE + "Are you ready to play? Please type 'yes' to continue: ")

print("\n")
#This adds a space between the lines

if playing.lower() != "yes":
    print("No worries! Please exit the quiz and check back in when you're ready!")
    sys.exit()
    quit()
else:
        print(Fore.CYAN + "Okay! Let's go!")
#The .lower converts the answer into lower case
#So it doesn't matter what case the answer is in
        
score = 0

print("\n")

answer = input(Fore.WHITE + "What is the capital of Australia? ")
if answer.lower() == "canberra":
    print(Fore.GREEN + "Correct!")
    score +=1
else:
    print(Fore.RED + "Incorrect!")
    print(Fore.RED + "The answer is Canberra")

print("\n")

answer = input(Fore.WHITE + "How many goals in a hat-trick? ")
if answer.lower() == "3":
    print(Fore.GREEN + "Correct!")
    score +=1
else:
    print(Fore.RED + "Incorrect!")
    print(Fore.RED + "The answer is 3")

print("\n")

answer = input(Fore.WHITE + "What does 'Au' stand for in the Periodic Table? ")
if answer.lower() == "gold":
    print(Fore.GREEN + "Correct!")
    score +=1
else:
    print(Fore.RED + "Incorrect!")
    print(Fore.RED + "The answer is Gold")

print("\n")

answer = input(Fore.WHITE + "Which planet is closest to the sun? ")
if answer.lower() == "mercury":
    print(Fore.GREEN + "Correct!")
    score +=1
else:
    print(Fore.RED + "Incorrect!")
    print(Fore.RED + "The answer is Mercury")

print("\n")

answer = input(Fore.WHITE + "How many sides does a dodecagon have? ")
if answer.lower() == "12":
    score +=1
    print(Fore.GREEN + "Correct!")
else:
    print(Fore.RED + "Incorrect!")
    print(Fore.RED + "The answer is 12")

print("\n")

answer = input(Fore.WHITE + "Who tries to steal the secret formula in Spongebob Squarepants? ")
if answer.lower() == "plankton":
    print(Fore.GREEN + "Correct!")
    score +=1
else:
    print(Fore.RED + "Incorrect!")
    print(Fore.RED + "The answer is Plankton")

print("\n")

answer = input(Fore.WHITE + "Which supermarket uses the slogan, 'Every Little Helps'? ")
if answer.lower() == "tesco":
    print(Fore.GREEN + "Correct!")
    score +=1
else:
    print(Fore.RED + "Incorrect!")
    print(Fore.RED + "The answer is Tesco")

print("\n")

answer = input(Fore.WHITE + "Which brand are the following car models: Fiesta, Focus, and Puma? ")
if answer.lower() == "ford":
    print(Fore.GREEN + "Correct!")
    score +=1
else:
    print(Fore.RED + "Incorrect!")
    print(Fore.RED + "The answer is Ford")

print("\n")

answer = input(Fore.WHITE + "What are human nails made up of? ")
if answer.lower() == "keratin":
    print(Fore.GREEN + "Correct!")
    score +=1
else:
    print(Fore.RED + "Incorrect!")
    print(Fore.RED + "The answer is Keratin")

print("\n")

answer = input(Fore.WHITE + "And finally, how many days in a leap year? ")
if answer.lower() == "366":
    print(Fore.GREEN + "Correct!")
    score +=1
else:
    print(Fore.RED + "Incorrect!")
    print(Fore.RED + "The answer is 366")

print("\n")

print(Fore.CYAN + "Congratulations on making it to the end of this quiz!")

print("\n")

print(Fore.YELLOW + "You got "+ str(score) +"/10 questions right!")

if score > 5:
    print(Fore.YELLOW + "Your final score is "+str((score / 10) * 100)+"% - Well Done! :)")
else:
    print(Fore.YELLOW + "Your final score is "+str((score / 10) * 100)+"% - Good Effort! :)")

print("\n")

input(Fore.WHITE + "Thank you for playing. Please press ENTER to exit now :)")