import random

player=input(("Type your Name "))
print(f'Hello {player} this is a quiz game to help with basic math questions.')
print('Ready for the first question? ')


# Function to find LCM
def compute_lcm(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm 

#function to find GCD
def compute_GCD(x, y):
# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            GCD = i 
    return GCD

GCFnum1 =random.randint(1,10)
GCFnum2 =random.randint(1,10)

#generate random number for LCM
LCM_num1=random.randint(1,10) 
LCM_num2=random.randint(1,10)


#equaling the correct answer with the correct lcm value
correctAnswerLCM=compute_lcm(LCM_num1, LCM_num2)

#equaling the correct answer with the correct GCD value
correctAnswerGCD=compute_GCD(GCFnum1, GCFnum2)

#user input for the lcm
print('First Question:')
answerLCM= int(input(f'Find the LCM of {LCM_num1} and {LCM_num2} ->'))

if answerLCM==correctAnswerLCM:
    print ('Correct ')
else:
    print("Incorrect the L.C.M. is", compute_lcm(LCM_num1, LCM_num2))


#user input for the GCD
print('Second Question:')
answerGCD= int(input(f'Find the GCD of {GCFnum1} and {GCFnum2} ->'))

if answerGCD==correctAnswerGCD:
    print ('Correct ')
else:
    print("Incorrect the G.C.D is", compute_GCD(GCFnum1, GCFnum2))

QUESTIONS=[
    (f"Find the LCM of {LCM_num1} and {LCM_num2} ->",correctAnswerLCM)
    (f'Find the GCD of {GCFnum1} and {GCFnum2} ->', correctAnswerGCD)
]
for answerLCM,correctAnswerLCM in QUESTIONS:
    answer=input(f"{answerLCM}?")
    if answer ==correctAnswerLCM:
        print ('Correct ')
    else:
        print("Incorrect the L.C.M. is", compute_lcm(LCM_num1, LCM_num2))