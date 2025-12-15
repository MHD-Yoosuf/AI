import requests
def get_random_fact():
    url = "https://uselessfacts.jsph.pl/random.json?language=en"
    response = requests.get(url)
    data = response.json()
    print("\n Random Fact:")
    print(data["text"])


def get_today_fact():
    url = "https://uselessfacts.jsph.pl/today.json?language=en"
    response = requests.get(url)
    data = response.json()
    print("\n📅 Fact of the Day:")
    print(data["text"])


print("=== Facts API Explorer ===")
print("1. Random Fact")
print("2. Fact of the Day")

choice = input("Choose an option (1 or 2): ")

if choice == "1":
    get_random_fact()
elif choice == "2":
    get_today_fact()
else:
    print(" Invalid choice")
