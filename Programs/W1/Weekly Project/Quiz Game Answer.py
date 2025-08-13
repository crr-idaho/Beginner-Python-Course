score = 0

questions = [
    ("What is the largest planet in our solar system?", "jupiter"),
    ("What keyword is used to start a loop that continues while a condition is true?", "while"),
    ("Which superhero is known as the “Caped Crusader”?", "batman"),
    ("True or False: A group of flamingos is called a 'flamboyance.'", "true"),
    ("What function is used to get input from a user in Python?", "input")
]

for question, answer in questions:
    user_input = input(question + " ")
    if user_input.lower().strip() == answer:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was: {answer}\n")

print("🎯 Final Score:", score, "/ 5")