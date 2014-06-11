ISBN=input('Please enter your 10 digit number: ')

while len(ISBN)!= 10:

    print('Please make sure you have entered a number which is exactly 10 characters long.')
    ISBN=int(input('Please enter the 10 digit number: '))
    continue


else:

    Digit1=int(ISBN[0])*11
    Digit2=int(ISBN[1])*10
    Digit3=int(ISBN[2])*9
    Digit4=int(ISBN[3])*8
    Digit5=int(ISBN[4])*7
    Digit6=int(ISBN[5])*6
    Digit7=int(ISBN[6])*5
    Digit8=int(ISBN[7])*4
    Digit9=int(ISBN[8])*3
    Digit10=int(ISBN[9])*2
    Result=(Digit1+Digit2+Digit3+Digit4+Digit5+Digit6+Digit7+Digit8+Digit9+Digit10)
    Remainder=Result%11
    Digit11=11-Remainder
    if Digit11==10:
       Digit11='X'
    ISBNNumber=str(ISBN)+str(Digit11)
    print('Your 11 digit ISBN Number is ' + ISBNNumber)
