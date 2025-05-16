print("Welcome to the Python Quiz Game!")
print("Answer the following questions by typing a, b, c, or d.\n")

# List of questions
questions = [
    {
        "question": "What is the output of 21 + 2?",
        "options": ["a) 3", "b) 4", "c) 23", "d) 22"],
        "answer": "b"
    },
    {
        "question": "Which one is a programming language?",
        "options": ["a) HTML", "b) CSS", "c) Python", "d) HTTP"],
        "answer": "c"
    },
    {
        "question": "What does 'len()' function do in Python?",
        "options": ["a) Add numbers", "b) Find length", "c) Compare", "d) Loop"],
        "answer": "b"
    }
]

score = 0

# Loop through each question
for q in questions:
    print(q["question"])
    for option in q["options"]:
        print(option)
    user_answer = input("Your answer: ").lower()
    
    if user_answer == q["answer"]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.\n")

# Final score
print(f"You got {score} out of {len(questions)} questions right!")
