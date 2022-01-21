"""
Name: <Ashlyn Whittemore>
<hw1>.py

Problem: <Needing to know how input works answering simple function questions producing output and do arithmatic.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is entirely my own work.

"""


def calc_rec_area():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    area = length * width
    print("Area =", area)


def calc_volume():
    length = eval(input("Enter the length: "))
    width = eval(input("Enter the width: "))
    height = eval(input("Enter the height: "))
    volume = length * width * height
    print("Volume=", volume)

calc_volume()


def shooting_percentage():
    total_shot = eval(input("Enter the player's total shots: "))
    shot_made = eval(input("Enter how many shots the player made: "))
    shot_percentage = shot_made/total_shot

    print("Shooting Percentage %: ", shot_percentage)

shooting_percentage()

# Asking for cost of shipping a coffee order
# Remember, when defining variables, you can call back to them to do arithmatic

def coffee():

    cost_cof = 10.50
    ship = 0.86
    cost_ovh = 1.50
    pound_amt = float(input("How many pounds of coffee would you like? : "))
    total_cost = cost_ovh + (cost_cof*pound_amt) + (ship*pound_amt)
    # cost of overhead is separate because it is per order

    print("The cost of your order would equal $", total_cost)

coffee()

def kilometers_to_miles():

    km = float(input("How many kilometers did you travel?: "))
    miles = km * 0.6214  # Does not matter the integer in miles because it will be multiplied.

    print("Number of Miles", miles)

kilometers_to_miles()

# Not sure what this is for below

if __name__ == '__main__':
    pass
