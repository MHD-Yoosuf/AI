import requests
import random
import html
url = "https://opentdb.com/api.php?amount=5&type=multiple"
response = requests.get(url)
data = response.json()
score = 0
print(" Welcome to the Trivia Quiz!\n")
for i, question_data in enumerate(data["results"], start=1):
    question = html.unescape(question_data["question"])
    correct_answer = html.unescape(question_data["correct_answer"])
    options = question_data["incorrect_answers"]
    options = [html.unescape(opt) for opt in options]
    options.append(correct_answer)
    random.shuffle(options)

    print(f"Q{i}. {question}")
    for idx, option in enumerate(options, start=1):
        print(f"{idx}. {option}")

    user_choice = int(input("Your answer (1-4): "))

    if options[user_choice - 1] == correct_answer:
        print("Correct!\n")
        score += 1
    else:
        print(f" Wrong! Correct answer: {correct_answer}\n")

print(f" Quiz Finished! Your score: {score}/5")

