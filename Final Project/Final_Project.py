#Creation of Question bank
dic={"What is the Capital city of Republic of Turkey?":"Ankara",
    "How many seasons are there in the Friens TV series?":"10",
     "What is the name of the manager in The Office TV series?":"Micheal Scott",
     "What is real name of the baby Yoda?":"Grogu",
     "When did the French Revolution occur?":"1789",
     "How many atomic bomb did lunch in the second world war?":"2",
     "When did touch screen telephone invented?":"1992",
     "Which language is the most common in the World?":"English",
     "What is the name of the cutest dog in the world?":"Mocha",
     "Which bear is the best? :D": "Grizzly Bear"}

i=0 #correct answer counter
q=1 #question number

for k,v in dic.items():
    print("Question",q, k)
    q +=1
    x=input("Please answer the question: ")

    if x == v:
        i +=1
    else:
        continue

# Evaluation of the grades
if i > 5:
    print("Your score is", i*10, "and you pass the exam, congratulations!")
else:
    print("Your score is", i*10, "unfortunately you did not pass the exam, you should work harder!")