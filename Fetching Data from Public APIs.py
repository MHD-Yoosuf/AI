import requests
def get_random_joke():
    url = "https://official-joke-api.appspot.com/random_joke"
    response = requests.get(url)
    if response.status_code == 200:
        joke = response.json()
        return f"{joke['setup']} - {joke['punchline']}"
    else:
        return "Failed to retrieve joke."
    
def main():
   print("Welcome to Random Joke Generator!")

   while True:
      user_input("Press Enter to get a new joke,or type 'q'/exit to quit: ").strip().lower()
           if user_input in ['q', 'exit']:
               print("Goodbye!")
                 break 
      
             joke = get_random_joke()
                print(joke) 
if __name__ == "__main__":
    main()  


url="https://official-joke-api.appspot.com/random_joke" 
response = requests.get(url) 
   
if response.status_code == 200:
    joke_data = response.json() 
    print(f"{joke['setup']} - {joke['punchline']}")

else:
       print("Failed to retrieve joke.")                           
      

