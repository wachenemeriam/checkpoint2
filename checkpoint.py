# checkpoint2
Q1:
mylist=[]
for x in range(2000,3200):
    if(x%7==0 and x%5!=0):
        mylist.append(str(x))
    print(mylist)
    
Q2:

 N = int(input("Enter a number: "))
factorial = 1
if N >= 1:
    for i in range (1,N+1):
       factorial = factorial * i
print(f"Factorail of {N} is: {factorial}")

Q3:

  number = int(input("Type a number: "))

numberDict = {}
for i in range(1, number+1):
    numberDict[i] = i*i

print(numberDict)
Q4:
def missing_char(str, n):
    front = str[:n]  
    back = str[n+1:]  
    return front + back
missing_char('kitten',4)
Q5:
import numpy as np
arr = np.array([[0,1],[2,3],[4,5]])
print(f'NumPy Array:\n {arr}')
list1 = arr.tolist()
print(f'List: {list1}')
Q6:

import numpy as np
x = np.array([0, 1, 2])
y = np.array([2, 1, 0])
print("\nOriginal array1:")
print(x)
print("\nOriginal array1:")
print(y)
print("\nCovariance matrix of the said arrays:\n",np.cov(x, y))
Q7:

import math

numbers = input("Provide D: ")
numbers = numbers.split(',')

result_list = []
for D in numbers:
    Q = round(math.sqrt(2 * 50 * int(D) / 30))
    result_list.append(Q)
print(result_list)
    
    
