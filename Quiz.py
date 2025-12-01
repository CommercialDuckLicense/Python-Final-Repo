import random
import math

# "\033[31mThis is red text\033[0m" - ANSI code to change text color RED
# "\033[32mThis is green\033[0m" - ANSI code to change text color GREEN
# "\033[33mThis is yellow\033[0m" - ANSI code to change color YELLOW
# "\033[36mThis is Cyan\033[0m" - ANSI code to change color to CYAN

#introduction, asking for name and explaining the quiz
player=input(("Type your Name "))
print(f'Hello \033[36m{player}\033[0m this is a quiz game to help with math questions. ')
print(f'So far there are questions about Least Common Denominator (LCM), Greatest Common Divisor(GCD), and finding the Square Root(Sqrt)')


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
    
    max_attempts=3 # number of max attempts

    #equaling the correct answer with the correct lcm value
    correctAnswerLCM=compute_LCM(LCM_num1, LCM_num2)

    # loop for when the question is wrong it loops until the answer is correct
    #user input for the lcm
    for attemptsLeft in range(max_attempts,0,-1):
        answerLCM= int(input(f'Find the LCM of {LCM_num1} and {LCM_num2} Please enter a Numerical value-> '))
        print(f'\033[33mYou have {attemptsLeft-1} attempts left.\033[0m')

        if answerLCM==correctAnswerLCM:
            print ("\033[32mCorrect!\033[0m")
            break
    else:
        print(f"\033[31mIncorrect try again the answer is {correctAnswerLCM}\033[0m") #this is not a permant print 

    #Ask another Answer
    retry = input("Would you like to practice again or move onto the next question? (\033[32my\033[0m/\033[31mn\033[0m): ")
    if retry == 'n':
        print("Good work! On to the next set of questions")
        break
    if retry == 'y':
        quit


#loop to ask user if they want a similar question #GCD
while True:
    GCFnum1 =random.randint(1,10)
    GCFnum2 =random.randint(1,10)
    
    max_attempts=3#number of max attempts

    #equaling the correct answer with the correct GCD value
    correctAnswerGCD=compute_GCD(GCFnum1, GCFnum2)

    # loop for when the question is wrong it loops until the answer is correct
    #user input for the GCD
    for attemptsLeft in range(max_attempts,0,-1):
        answerGCD= int(input(f'Find the GCD of {GCFnum1} and {GCFnum2} ->'))
        print(f'\033[33mYou have {attemptsLeft-1} attempts left.\033[0m')

        if answerGCD==correctAnswerGCD:
            print ("\033[32mCorrect!\033[0m")
            break
    else:
        print(f"\033[31mIncorrect try again the answer is {correctAnswerGCD}\033[0m")

    #Ask another Answer
    retry = input("Would you like to review similar questions? (\033[32my\033[0m/\033[31mn\033[0m): ")
    if retry == 'n':
        print("Good work! on to the next type of questions")
        break
    if retry == 'y':
        quit

# Loop to ask Square Root questions
while True:
    SQRTnum1 =random.randint(1,10)

    # equaling the correct answer to the sqrt and rounding
    correctAnswerSQRT=round(compute_Sqrt(SQRTnum1), 2) # round the decimal to 2 values
    
    max_attempts = 3
    
    #user input for Square root
    # loop for when the question is wrong it loops until the answer is correct
    for attemptsLeft in range(max_attempts , 0, -1): 
        answerSqrt= float(input(f'Find the Square Root of {SQRTnum1}, Round to the 2nd decimal Ex:(X.XX) ->')) #allows for decmial values
        print(f'\033[33mYou have {attemptsLeft-1} attempts left.\033[0m') 
    
        if answerSqrt==correctAnswerSQRT:
            print ("\033[32mCorrect!\033[0m")
            break
    else:
        print(f"\033[31mIncorrect try again the answer is {correctAnswerSQRT}\033[0m")
            
    #Ask another Answer
    retry = input("Would you like to practice more? (\033[32my\033[0m/\033[31mn\033[0m): ")
    if retry == 'n':
        print("Good work! Quiz ended.")
        break
    if retry == 'y':
        quit