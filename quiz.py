correct = 0
incorrect = 0

def multiple_answers(question, answerlist, no_of_answers):
    global incorrect, correct
    user = []
    print (question)
    while len(user) < no_of_answers:
        answer = input(f'Answer {len(user)+1}:').lower()
        if answer in user:
            print("You've already answered this. Try again.")
            continue
        user.append(answer)

        if answer in [a.lower() for a in answerlist]:
            print ("Correct!")
            correct += 1
        else:
            print ('wrong')
            incorrect += 1


#call the function
print ("================== First question ==================")
multiple_answers("Name 3 data types in python.",["string","integer","boolean","float"], 3)
print ("================== Second question ==================")
multiple_answers("Name 2 of Python's loops.", ["for", "while"], 2)
print ("================== Third question ==================")
multiple_answers("Name 4 collections of data types.",['list', 'tuple', 'dictionary', 'set'], 4)


#tally the scores
totalall = incorrect + correct
totalc = totalall - incorrect
print(f"You got {correct} correct answers!\n")
print (f"You got {incorrect} wrong answers!\n")
print (f'Total score: {totalc} out of {totalall}')
