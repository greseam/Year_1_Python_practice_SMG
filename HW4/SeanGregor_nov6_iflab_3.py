####
# if lab
#
# sean gregor
#
# accepts quiz score as an input and uses a descicion structure to calculate the corresponding grade.
####

def main():
    print('Grade Scale\n')
    credits = float(input('Enter number of points (out of five): '))
    if credits >= 5:
        cls = 'A'
    elif credits >= 4:
        cls = 'B'
    elif credits >= 3:
        cls = 'C'
    elif credits >= 2:
        cls = 'D'
    elif credits >= 1:
        cls = 'F'   
    else:
        cls = 'F'

    print('The grade is', cls)

if __name__ == '__main__':
    main()