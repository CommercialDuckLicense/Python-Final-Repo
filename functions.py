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
answerLCM= int(input(f'Find the LCM of {LCM_num1} and {LCM_num2} ->'))