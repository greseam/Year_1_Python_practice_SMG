def main():
    print('weekly pay calculator\n')
    hours = float(input('Enter hours worked: '))#float is used instead of eval to lock any input as a float
    wage = float(input('Enter hourly wage: '))
    if hours <= 40:
        pay = hours * wage #life in a nutshell
    else:
        pay = 40 * wage + (hours - 40) * 1.5 * wage 
    print("Your week's pay is ${0:0.2f}".format(pay)) #formats the outcome rounded to 2 decimal places
if __name__ == '__main__': #checks if its the main program or a secondary one
    main()