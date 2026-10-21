quiz_data = [
    {
        "Question": "There are five candles burning in a room. If two of them are blown out, tell me how many candles will be left in the room?",
        "choices": ["A) 2", "B) 3", "C) 5", "D) 1"],
        "answer": "C"
    },
    {
        "Question": "If a clock shows 3:00 and it gains 5 minutes every hour, what time will the clock show after 2 hours?",
        "choices": ["A) 5", "B) 5:10", "C) 5:20", "D) 5:05"],
        "answer": "B"
    },
    {
        "Question": "If the price of 3 pencils is Rs 15, what will be the price of 7 pencils?",
        "choices": ["A) 30", "B) 35", "C) 40", "D) 45"],
        "answer": "B"
    }
]
def run_quiz(questions):
    score = 0  
    print("--- Welcome to the Python Quiz! ---\n")
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for choice in q["choices"]:
            print(choice)
        user_answer = input("Your answer (A, B, C, or D): ").strip().upper()
        if user_answer == q["answer"]:
            print("Correct! 🎉\n")
            score += 1
        else:
            print(f"Incorrect. The correct answer was {q['answer']}.\n")
    total_questions = len(questions)
    percentage = (score / total_questions) * 100
    print("--- Quiz Results ---")
    print(f"You answered {score}/{total_questions} questions correctly.")
    print(f"Your final score is: {percentage:.1f}%")
if __name__ == "__main__":
    run_quiz(quiz_data)