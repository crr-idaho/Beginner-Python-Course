# Build a command-line quiz game that asks 5 questions and scores the user.
score = 0

n1 = input("What is the largest planet in our solar system? ")
if n1.lower() == "jupiter":
    print("Correct!")
    score += 1
else:
    print("Womp womp, that's wrong.")

n2 = input("What keyword is used to start a loop that continues while a condition is true? ")
if n2.lower() == "while":
    print("That's right!")
    score += 1
else:
    print("BAAAAA!!! Nope.")

n3 =  input("Which superhero is known as the “Caped Crusader”? ")
if n3.lower() == "batman":
    print("Wowee! You got it right.")
    score += 1
else:
    print("wow... idiot. That's not even close.")

n4 = input("True or False: A group of flamingos is called a 'flamboyance.' ")
if n4.lower() == "true":
    print("Unbelievable. You're a trivia master!")
    score += 1
else:
    print("BRUUUUHHH! How can you be this dumb?")

n5 = input("What function is used to get input from a user in Python? ")
if n5.lower() == "input":
    print("Fan-frickin-tastic! That's correct!")
    score += 1
else:
    print("Oh my goodness. You are such a dissapointment.")

print("Here's your final score:", score, "/ 5")