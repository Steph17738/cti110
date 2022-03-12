# CTI-110
# P3HW2 - Pizza Order
# Stephen Misurak 
# 3/11/2022
import math
from time import process_time_ns
from traceback import print_tb

#Ask user to enter number of students she/he would like to order pizza for.  
#Ask user for number of people that will be sharing each pizza ( 1.5, 2 or 3). 
students = int(input('How many students do you want to order pizza for?\n'))
num_people = float(input('Enter number of people per pizza ( 1.5, 2 or 3):\n'))
#calculations for entries 
#If user enters 1.5 ( meaning 1.5 people per pizza), the program is to do the math and calculate number of Whole pizzas user needs to buy.
#If user enters 2 (2 people per pizza), the program is to calculate number of Whole pizzas user needs to buy
#If user enters 3 (meaning 3 people per pizza ), the program is to calculate number of Whole pizzas user needs to buy
if num_people == 1.5:
    pizza = math.ceil(students / num_people)
    price = pizza * 5
    final_price = price * 1.06
elif num_people == 2:
    pizza = math.ceil(students / num_people)
    price = pizza * 5
    final_price = price * 1.06
elif num_people == 3:
    pizza = math.ceil(students / num_people)
    price = pizza * 5
    final_price = price * 1.06
else:
    print('INVALID ENTRY!!!')
    print('You should have entered 1.5, 2 or 3\n')
    print('Run the program again')
#Order if inputs are correct
print('----Pizza Order---------')
print(f'Number of students {students}')
print(f'Pizzas Needed: {pizza}')
print(f'Price: ${final_price:.2f}')
print('-------------------------')
