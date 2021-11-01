'''
from file questionClass.py import class Question
'''
from questionClass import Question
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]
questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b")
]

#function
def run_test(questions):
    score = 0
    for question in questions:
        #input shows prompt
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("Your got " + str(score) + "/" + str(len(questions)) + " correct")

############### MAIN ###################
run_test(questions)
