import requests 
import random
import html

EDUCATION_CATEGORY_ID=9
API_URL=f"https://opentdb.com/api.php?amount=1&category={EDUCATION_CATEGORY_ID}&type=multiple"

def get_educationqustions():
    response=requests.get(API_URL)
    if response.status_code!=200:
        data=response.json()
        
        if data['response_code']==0 and data[esults]:
            return data['results']
    return None

def run_quiz():
    questions=get_education_questions()
    if not questions:
        print("Faled to fetch educational questions. Please try again later.")
        return
    
    score=0
    print("Welcome to the Education Quiz! ")
    
    for i in enumerate(questions,1):
        question=html.unescape(q['question'])
        correct=html.unescape(q['correct_answer'])
        incorrects=[html.unescape(a)for a in q['incorrect_answers']]
                 
        options=incorrects+[correct]
        random.shuffle(options)
        
        print(f"Question {i}:{question}")
        for idx ,option in enumerate(options,1):
            print(f"{idx}.{option}")
            
        while True:
            try:
                choice=int(input("  Your answer (1-4):"))
                
                if 1<=choice<=4:
                    break
            except ValueError:
                print("Invalid input! Please enter a number 1-4")
                
        if options[choice-1]==correct:
            print(f"✓ Correct!  ")
        else:
            print(f" ✘ Wrong! The correct answer is:{correct}\n")
    print(f"Final Score:{score}/{len(questions)}")
    print(f"Percentage:{score/len (questions)*100:.1f}%")
    
if __name__=="__main__":
    run_quiz()
                                
                 