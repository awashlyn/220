"""
Name: <Ashlyn Whittemore>
<lab2>.py

What will the program do?
Use three different ways to get the average set of numbers.

Inputs will be:
The equations with a user input 'for i in range'...
The user will put in what they want for output only.
Outputs:
What the user will enter to get the computed value.

Step-by-step list:
1. Get forumulas used from document
2. import math to use sqrt()
3. use range and with the different numbers to get
4. Write out user input

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math
x = [0] * (10)
n = int(input("Enter the values to be entered :"))
#read n numbers
for i in range(0, n - 1 + 1, 1):
    x[i] = int(input("Enter value :"))

# Here I write a loop to compute rms average
sum = 0
for i in range(0, n - 1 + 1, 1):
    sum = sum + x[i] * x[i]
rms = math.sqrt(float(sum) / n)
print(round(rms,3))

# Compute harmonic mean
sum = 0
for i in range(0, n - 1 + 1, 1):
    sum = sum + float(1) / x[i]
harmonic = float(n) / sum
print(round(harmonic,3))

# Compute Geometric Mean
product = 1
for i in range(0, n - 1 + 1, 1):
    product = product * x[i]
geometric = math.pow(product,1/n)
print(round(geometric,3))