"""
Name: <Ashlyn Whittemore>
<h2>.py

Problem: <Brief, one or two sentence description of the problem that this program solves, in your own words.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

# n  = number... use 'while'
def sum_of_threes():
    upperbound = int(input("What is the upper bound?"))
    # using 'int' because it needs a number
    s = 0
    k = 3
    while(k<=n):
        s+=k
        k+=3
    print("Sum is:",s)
sum_of_threes()




def multiplication_table():
    for i in range(1,11):
       for j in range(1,11):
           print(i*j, end='\t')
        print('')

multiplication_table()

def triangle_area():
    a = float(input("Enter side a length: "))
    b = float(input("Enter side b length: "))
    c = float(input("Enter side c length: "))
    # calculating perimeter
    p = (a+b+c)/2
    # getting area
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(area)
triangle_area()


def sum_squares(start, stop):
    # What is 'x times x' added to 'x times x' and what could the ranges be?
    total = 0
    for i in range(start, stop+1):
        total += i*i
    return total
    lr = int(input("Enter lower range: "))
    ur = int(input("Enter upper range: "))
    print(sum_squares(lr, ur))
sum_squares()






def power():
    pass


if __name__ == '__main__':
    pass
