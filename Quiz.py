import random
import math

# "\033[31mThis is red text\033[0m" - ANSI code to change text color RED
# "\033[32mThis is green\033[0m" - ANSI code to change text color GREEN

#introduction, asking for name and explaining the quiz
player=input(("Type your Name "))
print(f'Hello {player} this is a quiz game to help with basic questions. ')

# better code for my LCM function using import features
def compute_LCM(x,y):
    return math.lcm(x,y)

# code for GCD function
def compute_GCD(x, y):
    return math.gcd(x, y)

# code for finding Square root 
def compute_Sqrt(x):
    return math.sqrt(x)


#loop to ask user if they want a similar question *LCM
while True:
    #generate random number for LCM
    LCM_num1=random.randint(1,10) 
    LCM_num2=random.randint(1,10)

    #equaling the correct answer with the correct lcm value
    correctAnswerLCM=compute_LCM(LCM_num1, LCM_num2)

    while True: # loop for when the question is wrong it loops until the answer is correct
    #user input for the lcm
        answerLCM= int(input(f'Find the LCM of {LCM_num1} and {LCM_num2} Please enter a Numerical value-> '))

        if answerLCM==correctAnswerLCM:
            print ("\033[32mCorrect!\033[0m")
            break
        else:
            print("\033[31mIncorrect\033[0m try again", compute_LCM(LCM_num1, LCM_num2) ) #this is not a permant print 

    #Ask another Answer
    retry = input("Would you like another question? (\033[32my\033[0m/\033[31mn\033[0m): ")
    if retry == 'n':
        print("Good work! On to the next set of questions")
        break
    if retry == 'y':
        quit


#loop to ask user if they want a similar question #GCD
while True:
    GCFnum1 =random.randint(1,10)
    GCFnum2 =random.randint(1,10)

    #equaling the correct answer with the correct GCD value
    correctAnswerGCD=compute_GCD(GCFnum1, GCFnum2)

    while True:# loop for when the question is wrong it loops until the answer is correct
        #user input for the GCD
        answerGCD= int(input(f'Find the GCD of {GCFnum1} and {GCFnum2} ->'))

        if answerGCD==correctAnswerGCD:
            print ("\033[32mCorrect!\033[0m")
            break
        else:
            print("\033[31mIncorrect\033[0m try again", compute_GCD(GCFnum1, GCFnum2))
    #Ask another Answer
    retry = input("Would you like another question? (\033[32my\033[0m/\033[31mn\033[0m): ")
    if retry == 'n':
        print("ere")
        break
    if retry == 'y':
        quit


# Loop to ask Square Root questions
while True:
    SQRTnum1 =random.randint(1,10)
    SQRTnum2=random.randint(1,10)

    # equaling the correct answer to the sqrt and rounding
    correctAnswerSQRT=round(compute_Sqrt(SQRTnum1), 2) # round the decimal to 2 values
    
    while True:# loop for when the question is wrong it loops until the answer is correct
        #user input for Square root
        answerSqrt= float(input(f'Find the Square Root of {SQRTnum1}, round to the 2nd decimal Ex:(X.XX) ->')) #allows for decmial values

        if answerSqrt==correctAnswerSQRT:
            print ("\033[32mCorrect!\033[0m")
            break
        else:
            print("\033[31mIncorrect\033[0m try again", round(compute_Sqrt(SQRTnum1), 2))
    #Ask another Answer
    retry = input("Would you like another question? (\033[32my\033[0m/\033[31mn\033[0m): ")
    if retry == 'n':
        print("Good work! Quiz ended.")
        break
    if retry == 'y':
        quit