import requests

def main():
    amount = get_valid_amount()
    difficulty = get_valid_difficulty()
    questions = get_questions(amount, difficulty=difficulty)
    quiz(questions)


def get_questions(amount, category=18, q_type="boolean", difficulty=None):
    params = {
        "amount": amount,
        "category": category,
        "type": q_type,
        "difficulty": difficulty,
    }

    base_url = "https://opentdb.com/api.php"
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
    # Krijimi i Listës së Pyetjeve
        questions_list = []
        for item in data["results"]:
            question_data = {
                "question": item["question"],
                "correct_answer": item["correct_answer"],
                "incorrect_answers": item["incorrect_answers"]
            }
            questions_list.append(question_data)
        return questions_list

    else:
        print("Error with the API request.")
        return None


def get_valid_amount():
    while True:
        try:
            amount = int(input("Enter the number of questions (1 to 10): "))
            if amount < 1 or amount > 10:
                raise ValueError("The number of questions must be between 1 and 10.")
            return amount
        except ValueError as ve:
            print(f"Invalid input: {ve}. Please try again.")

def get_valid_difficulty():
    while True:
        difficulty = input("Enter the difficulty (easy, medium, hard): ").lower()
        if difficulty in ["easy", "medium", "hard"]:
            return difficulty
        else:
            print("Invalid difficulty level. Please choose from 'easy', 'medium', or 'hard'.")


def quiz(questions):
    score = 0  # Initialize score

    for question in questions:
        print(question['question'])
        user_answer = input("Your answer (True/False): ").strip().capitalize()
        if user_answer not in ["True", "False"]:
            print("Invalid option. Please choose True or False.")
            continue
        if user_answer == question['correct_answer']:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect. The correct answer is:", question['correct_answer'], "\n")

    print("Your score is", score, "correct answers out of a total of", len(questions), "questions!")


if __name__ == "__main__":
    main()

