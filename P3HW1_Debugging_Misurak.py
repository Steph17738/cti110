# This program takes the users's grade as an input and calculates what letter grade the user has.
# Misurak

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    # TO DO: define the rest of the scores
    A_score = 90
    B_score = 80
    C_score = 70
    D_score = 60
   
    
    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')
    elif score >= B_score:
        print('Your grade is: B')
    elif score >= C_score:
        print('Your grade is: C')
    elif score >= D_score:
        print('Your grade is: D')
    else:
        print('Your grade is: F') # TO DO: finish this







# program start
main()