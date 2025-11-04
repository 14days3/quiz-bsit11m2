import time
from colorama import Fore, Style
#initialize the tally
correct = 0
incorrect = 0

name = input("Enter name: ")
def typing_effect(text, delay=0.0001):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def multiple_answers(question, answerlist, no_of_answers):
    global incorrect, correct
    user = []
    print (question)
    while len(user) < no_of_answers:
        answer = input(f'Answer {len(user)+1}:').lower()
        if answer in user:
            print(Fore.RED + "You've already answered this. Try again." + Style.RESET_ALL)
            continue
        user.append(answer)

        if answer in [a.lower() for a in answerlist]:
            print (Fore.GREEN + "✔️ Correct!" + Style.RESET_ALL)
            correct += 1
        else:
            print (Fore.RED + '❌ Wrong!' + Style.RESET_ALL)
            incorrect += 1
#shit
typing_effect(f"Hello, {name}, welcome to Project Mnemosyne!")
typing_effect("This is no ordinary quiz, this is an adventure! Fail and ye shall be eaten by the treacherous serpent. May the goddess of memory have mercy upon thee.")
confirmation = input('So are you ready to start? type "Yes" if you are, "No" if you\'re not. ')
if confirmation.lower() == "yes":
    #single answer
    print("The following 5 questions require only 1 answer. Good luck! 🌟")
    print(Fore.LIGHTCYAN_EX + "================== First question ==================" + Style.RESET_ALL)
    multiple_answers("Who created Python?. (his last name)", ["Rossum"], 1)
    print(Fore.LIGHTCYAN_EX + "================== Second question ==================" + Style.RESET_ALL)
    multiple_answers("What data type is the following: 'True'", ["Boolean"], 1)
    print(Fore.LIGHTCYAN_EX + "================== Third question ==================" + Style.RESET_ALL)
    multiple_answers("Which String method do you use for lowercase?", ["lower", ".lower()", "lower()"], 1)
    print(Fore.LIGHTCYAN_EX + "================== Fourth question ==================" + Style.RESET_ALL)
    multiple_answers("What keyword is used in declaring a function?", ["def", "def()"], 1)
    print(Fore.LIGHTCYAN_EX + "================== Fifth question ==================" + Style.RESET_ALL)
    multiple_answers("Which function is used to get the length of a string?", ["len", "len()", ".len()"], 1)


    print ("The following questions are in enumeration. Good luck! 🌟")
    # call the function for multiple questions
    print(Fore.LIGHTCYAN_EX + "================== First question ==================" + Style.RESET_ALL)
    multiple_answers("Name 3 data types in python.", ["string", "integer", "boolean", "float"], 3)
    print(Fore.LIGHTCYAN_EX + "================== Second question ==================" + Style.RESET_ALL)
    multiple_answers("Name 2 of Python's loops.", ["for", "while"], 2)
    print(Fore.LIGHTCYAN_EX + "================== Third question ==================" + Style.RESET_ALL)
    multiple_answers("Name 4 collections of data types.", ['list', 'tuple', 'dictionary', 'set'], 4)
    print(Fore.LIGHTCYAN_EX + "================== Fourth question ==================" + Style.RESET_ALL)
    multiple_answers("Name atleast 3 Python keywords", ["def", "class", "if", "elif", "else", "import", "return", "yield"], 3)
    print(Fore.LIGHTCYAN_EX + "================== Fifth question ==================" + Style.RESET_ALL)
    multiple_answers("What are all the conditional statements Python has?", ["if", "else","elif"], 3)

else:
    print ("oH OKAY then. Have a nice day.")





#tally the scores
totalall = incorrect + correct
totalc = totalall - incorrect
print(Fore.MAGENTA + "Final Results:")
print(f"You got {correct} correct answers!")
print(f"You got {incorrect} wrong answers!")
print(f"Total score: {totalc} out of {totalall}")
