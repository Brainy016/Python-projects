# Python Quiz game

questions=("1. How many elements are in the periodic table?: ",
          "2. Which animal lay the largest egg?: ",
          "3. What is the most abundant gas in Earth's Atmosphere?: ",
          "4. How many bones are in the human body?: ",
          "5. Which planet in the solar system is the hottest?: ")
options=(("A.116", "B. 117", "C. 118", "D. 119"),
         ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
         ("A.Nitrogen", "B. Oxygen", "C. Carbib-dioxide", "D. Hydrogen"),
         ("A. 206", "B. 207", "C. 208", "D. 209"),
         ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))
answers=("C","D","A","A","B")
guesses=[]
question_num=0
score=0

for question in questions:
    print(question)
    print("------------------------")
    for option in options[question_num]:
        print(option, end=" ")
    print()
    guess=input("  Enter (A,B,C OR D):  ").upper()
    guesses.append(guess)
    if guess== answers[question_num]:
        score+=1
        print("CORRECT")
    else:
        print("INCORRECT")
        #print(f"Correct answer is {answers[question_num]}")

    question_num += 1

print("-------------------")
print("       RESULT    ")
print("-------------------")

print("answer:", end="")
for answer in answers:
    print(answer, end=" ")

print()
print("Guess:", end=" ")
for gues in guesses:
    print(gues, end=" ")

print()
score= float(score/len(questions) * 100)
print(f"score is {score}%")

