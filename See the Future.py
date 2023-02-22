import random

#random responses to questions
responses = ["yes - Definently", "It's decidedly so", "Without a doubt", "Reply hazy, try again",
"Ask again later", "I better not tell you now", "My sources say no", "Outlook not so good",
"Very doubtful", "The truth lies with bool", "On the fith day of the third month your truth shall be revealed",
"Error 404", "Yes better than you can imagine", "Your answer lies at home"]


#asking a question
first_question = input("Hello my friend, would you like to learn about your future? ")
welcome = first_question.lower()
if welcome != "yes":
    print("Ok, come back when you would like to learn something.")
    quit() 

#ask question
more = ("I can answer so much more!.. ")
def ask_a_question(): 
    question = input("\nWhat would you like to know? ")  
    answer = random.choice(responses)   
#responses to incorrect question input
    if question.isdigit():
        print("Sorry I can't decipher numbers, ask something else next time.") 
        quit()
    elif question == "":
        question = input("I can't read your mind! What would you like to know. ")
        if question == "":
            print("Maybe next time then... ")
            quit()
        elif question.isdigit():
            print("I can't decipher numbers... Maybe next time then...")
            quit()
    input(f"\nSo you want to know \"{question}\", Let me search for your answer...\nMy source says: {answer}.\n")
    return more 

#start the loop
print(ask_a_question())
second_question = input("Would you like to ask another question? ")
again = second_question.lower()
while again == "yes":
    print(ask_a_question())
    second_question = input("Would you like to ask another question? ")
    again = second_question.lower()
else:
    quit()

