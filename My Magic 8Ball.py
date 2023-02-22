import random
guess = random.randint(1,15)
name = ""

question =input("What would you like to know about your future? ")
answer = " "

#question rules
while question == "":
    if len(question) == 0:
        question = input("I cannot tell your fortune unless you ask a question! What would you like to know? ")


#Random fourtunes
if guess == 1:
    answer = "Yes - Definently"
elif guess == 2:
    answer = "It's decidedly so"
elif guess == 3:
    answer = "Without a doubt"
elif guess == 4:
    answer = "Reply hazy, try again"
elif guess == 5:
    answer = "Ask again later"
elif guess == 6:
    answer = "Better not tell you now"
elif guess == 7:
    answer = "My sources say no"
elif guess == 8:
    answer = "Outlook not so good"
elif guess == 9:
    answer = "Very doubtful"
elif guess == 10:
    answer = "The truth lies with _bool"
elif guess == 11:
    answer = "Without a doubt... NO"
elif guess == 12:
    answer = "On the fitfh day of the thrid month your truth shall be revealed"
elif guess == 13:
    answer = "Error 404"
elif guess == 14:
    answer = "Yes better than you can imagine"    
elif guess == 15:
    answer = "Your answer lies at home"
else:
    answer = "Error"
#learn to not use \n unless very basic projects
print(answer)

#edit this in later I dont want to forget it!
#if name == "":
  #print("Question:", question,"\nMagic 8-ball's answer: ",answer)
#elif question =="":
  #print("The magic 8-Ball can't answer a question unless you ask it something!")
#elif name !="" and question !="":
  #print(name+ " asks: "+ question)
  #print("Magic 8-Ball's answer: "+answer)