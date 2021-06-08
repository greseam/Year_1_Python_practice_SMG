####
# 
#
# Sean Gregor
#
#
####

def main():
    print('college Classification\n')
    credits = float(input('Enter number of credits'))
    if credits < 7:
        cls = 'Freshman'
    elif credits < 16:
        cls = 'Sophmore'
    elif credits < 26:
        cls = 'Junior'
    else:
        cls = 'Senior'

    print('The classification is', cls)

if __name__ == '__main__':
    main()