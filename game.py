def display_question(question, options):
    print(question)
    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")
    user_input = int(input("Enter your choice (1, 2, 3, or 4): "))
    return user_input

def evaluate_answer(user_input, correct_answer, score):
    if user_input == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")
    return score

def main():
    questions = [
        {"question": "What is the capital of France?",
         "options": ["London", "Paris", "Rome", "Berlin"],
         "correct_answer": 2},
        {"question": "Who wrote 'To Kill a Mockingbird'?",
         "options": ["Harper Lee", "J.K. Rowling", "Stephen King", "Mark Twain"],
         "correct_answer": 1},
        {"question": "What is the largest planet in our solar system?",
         "options": ["Earth", "Jupiter", "Saturn", "Mars"],
         "correct_answer": 2}
    ]

    score = 0

    for question in questions:
        user_input = display_question(question["question"], question["options"])
        score = evaluate_answer(user_input, question["correct_answer"], score)
        print("Your current score is:", score)

    print("\nQuiz Finished!")
    print("Your final score is:", score)
    if score == len(questions):
        print("Well done! You got all the questions correct.")
    elif score == 0:
        print("Better luck next time! You didn't get any questions correct.")
    else:
        print("Good job! You got some questions correct.")

if _name_ == "_main_":
    main()
