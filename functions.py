import random
import math

def compute_GCD(x, y):
    return math.gcd(x, y)

GCDnum1 = 2
GCDnum2 = 2
print("The GCD is", compute_GCD(GCDnum1, GCDnum2))

def comupte_LCM(x,y):
    return math.lcm(x,y)

LCM_num1=random.randint(1,10) 
LCM_num2=random.randint(1,10)
print('the LCM is', comupte_LCM(LCM_num1,LCM_num2))


# code for finding Square root 
def compute_Sqrt(x):
    return math.sqrt(x)

# Loop to ask Square Root questions
while True:
    SQRTnum1 =random.randint(1,10)
    SQRTnum2=random.randint(1,10)

    # equaling the correct answer to the sqrt and rounding
    correctAnswerSQRT=round(compute_Sqrt(SQRTnum1), 2) # round the decimal to 2 values
    
    max_attempts = 4
    # loop for when the question is wrong it loops until the answer is correct
        #user input for Square root

    for attemptsLeft in range(max_attempts , 0, -1):
        answerSqrt= float(input(f'Find the Square Root of {SQRTnum1}, round to the 2nd decimal Ex:(X.XX) ->')) 
        print(f'You have {attemptsLeft(+1)} attempts left.') #allows for decmial values
        

        if answerSqrt==correctAnswerSQRT:
            print ("\033[32mCorrect!\033[0m")
            break
    else:
        print("\033[31mIncorrect\033[0m try again", correctAnswerSQRT)
            
    

    #Ask another Answer
    retry = input("Would you like another question? (\033[32my\033[0m/\033[31mn\033[0m): ")
    if retry == 'n':
        print("Good work! Quiz ended.")
        break
    if retry == 'y':
        quit