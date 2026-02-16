import requests
from colorama import Fore, Style, init
init(autoreset=True)
API_KEY = "YOUR_HUGGINGFACE_API_KEY"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

def summarize_text(text, min_length, max_length, model_name):
    API_URL = f"https://api-inference.huggingface.co/models/{model_name}"
    
    payload = {
        "inputs": text,
        "parameters": {
            "min_length": min_length,
            "max_length": max_length
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        result = response.json()
        return result[0]["summary_text"]
    else:
        print(Fore.RED + "Error:", response.json())
        return None

print(Fore.CYAN + Style.BRIGHT + "\n==== AI Text Summarizer ====\n")

user_name = input("Enter your name: ")
user_text = input("\nPaste your text to summarize:\n")

print("\nChoose a model:")
print("1 - BART (facebook/bart-large-cnn)")
print("2 - Pegasus (google/pegasus-xsum)")

model_choice_input = input("Enter 1 or 2: ").strip()

if model_choice_input == "2":
    model_choice = "google/pegasus-xsum"
else:
    model_choice = "facebook/bart-large-cnn"

print("\nChoose summarization style:")
print("1 - Standard")
print("2 - Enhanced (longer & detailed)")

style_choice = input("Enter 1 or 2: ").strip()

if style_choice == "2":
    min_length = 80
    max_length = 200
    print(Fore.BLUE + "Enhancing summarization process")
else:
    min_length = 50
    max_length = 150
    print(Fore.BLUE + "Using standard summarization settings")

summary = summarize_text(user_text, min_length, max_length, model_choice)

if summary:
    print(Fore.GREEN + Style.BRIGHT + f"\n AI Summarizer Output for {user_name}:\n")
    print(Fore.GREEN + summary)
else:
    print(Fore.RED + " Failed to generate summary.")

