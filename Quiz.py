import random
import math


player=input(("Type your Name "))
print(f'Hello {player} this is a quiz game to help with basic math questions.')

def compute_LCM(x,y):
    return math.lcm(x,y)


def compute_GCD(x, y):
    return math.gcd(x, y)

while True:
    #generate random number for LCM
    LCM_num1=random.randint(1,10) 
    LCM_num2=random.randint(1,10)

    #equaling the correct answer with the correct lcm value
    correctAnswerLCM=compute_LCM(LCM_num1, LCM_num2)

    while True: # loop for when the question is wrong it loops until the answer is correct
    #user input for the lcm
        answerLCM= int(input(f'Find the LCM of {LCM_num1} and {LCM_num2} ->'))

        if answerLCM==correctAnswerLCM:
            print ('Correct ')
            break
        else:
            print("Incorrect the L.C.M. is", compute_LCM(LCM_num1, LCM_num2))

    #Ask another Answer
    retry = input("Would you like another similar question? (y/n): ")
    if retry != 'y':
        print("Good work! On to the next set of questions")
        break

while True:
    GCFnum1 =random.randint(1,10)
    GCFnum2 =random.randint(1,10)

    #equaling the correct answer with the correct GCD value
    correctAnswerGCD=compute_GCD(GCFnum1, GCFnum2)

    while True:# loop for when the question is wrong it loops until the answer is correct
        #user input for the GCD
        answerGCD= int(input(f'Find the GCD of {GCFnum1} and {GCFnum2} ->'))

        if answerGCD==correctAnswerGCD:
            print ('Correct ')
            break
        else:
            print("Incorrect the G.C.D is", compute_GCD(GCFnum1, GCFnum2))
        #Ask another Answer
    retry = input("Would you like another question? (y/n): ")
    if retry != 'y':
        print("Good work! Quiz ended.")
        break

