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
        answer = input(f'Answer {len(user)+1}: ').lower()
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

def mcq(question, answer, choices):
    global incorrect, correct
    print (question)
    print (choices)
    userinput = input("\nEnter letter here: ").upper()
    if userinput == answer:
        print(Fore.GREEN + "✔️ Correct!" + Style.RESET_ALL)
        correct += 1
    else:
        print(Fore.RED + '❌ Wrong!' + Style.RESET_ALL)
        incorrect += 1


#main body
typing_effect(f"Hello, {name}, welcome to Project Mnemosyne!")
typing_effect("Instructions: Write your answer in the space provided after the colon." + Fore.RED + " DO NOT PRESS SPACE! " + Style.RESET_ALL + "Otherwise it will count the space and invalidate the answer.")
confirmation = input('So are you ready to start? type "Yes" if you are, "No" if you\'re not. ')
if confirmation.lower() == "yes":
    timer_start = time.time()
    #single answer
    print("Identification: The following 5 questions require only 1 answer. Good luck! 🌟")
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

    #call mcqs
    print("Multiple choice: The following 5 questions require you to choose a letter. Good luck! 🌟")
    print(Fore.LIGHTCYAN_EX + "================== First question ==================" + Style.RESET_ALL)
    mcq("What will be the result of this? \n x = 10" "\n y = 10" "\n print(x + y**2)", "B", "\n[A] None \n[B] 110 \n[C] 20 \n[D] 22")
    print(Fore.LIGHTCYAN_EX + "================== Second question ==================" + Style.RESET_ALL)
    mcq("Predict the output of this function \n def square(x): \n return x * x \n print(square(5))", "C","\n[A] 5 \n[B] 10 \n[C] 25 \n[D] 50")
    print(Fore.LIGHTCYAN_EX + "================== Third question ==================" + Style.RESET_ALL)
    mcq("How would you write this equation into a variable in Python: Find the kinetic energy of the SUV weighing 1700kg travelling at 30m/s. \n KE = 1/2MV^2", "A","\n[A] KE = (0.5)*(1700)*(30)**2 \n[B] KE = (1/2) x (1700) x (30)^2 \n[C] Kinetic Energy = 1/2*1700*30**2")
    print(Fore.LIGHTCYAN_EX + "================== Fourth question ==================" + Style.RESET_ALL)
    mcq("From the last question, once print(KE) is executed, what will the output be?", "C","\n[A] None \n[B] 765,000 \n[C] 765000.0 \n[D] 765000")
    print(Fore.LIGHTCYAN_EX + "================== Fifth question ==================" + Style.RESET_ALL)
    mcq("What Python keyword do we use to use external modules into our code?", "B","\n[A] include \n[B] import \n[C] install \n[D] use ")
    # call the function for multiple questions
    print ("Enumeration: The following 5 questions asks you to numerate a number of objects Good luck! 🌟")
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
    timer_end = time.time()

    # tally the scores
    totalall = incorrect + correct
    totalc = totalall - incorrect
    total_time = timer_end - timer_start
    print(Fore.MAGENTA + "================== Final Results ==================")
    print(f"Congratulations, {name}, You got {correct} correct answers!")
    print(f"You got {incorrect} wrong answers!")
    print(f"Total score: {totalc} out of {totalall}")
    print(f"Total time: {total_time:.2f} seconds.")


else:
    print ("oH OKAY then. Have a nice day.")

