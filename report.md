#Controlled Assessment Report
#Aidan King Centre Number - 64305 Candidate Number - 0102
##Task 1 -

###Design
The task was to create a currency converter that -

a) Has exchange rates that can be regularly changed by the user. 

b) User should be able to enter an amount, select chosen currency, and the currency to convert it into. 

c) Figure shown should be to two decimal places.

The Currencies required to convert are: GBP (£) Euro (€) USD ($) and JPY (¥).
###Programming Techniques
####list - I used this to list the four currencies (Pound Sterling, Euro, Yen and Dollars)
####sensible variable name - I could have used any variable, however throughout my code I set the variables the sensible names, for example c_type1 represents currency type 1. short_hand represents the short version of the currency
####def function - I used this as functions are useful to repeat tasks without returning values
####input - I used this to store the input, this was then used later on to convert
####output - I used output to show the user what their converted amount was
####if statement - I used this so the program could tell what the user wanted to conver to and from, and when it knew that, it could then do the calculations to find out the converted amount.
####if loop - if, elif, else. I used if loop as I used (x,y,z). This was used to convert at the end of the program. If it was not one calculation, elif was used, and if it was not that, else was then used.
###Possible Problems
There are a few problems that I have thought may occur. One of these would be what would happen if I entered a letter instead of a number when converting. After testing my code, when I enter a letter, the program simply stops, and gives an error. Another problem I thought of is where the currency changes over time. This may cause incorrect currency rates. However this can be edited in the code itself on the second line. If I had more time I would have tried to link the rates to a automatically updating currency converting website, and get the rates directly from there. However, I did not have enough time to do this. I would also make a while loop in the code. This would make it so that after you have converted an amount of money, you could then convert something else, instead of the program stopping
The problem I had with the first code, was that it was not as good as the second one. I liked the second one as I made it to show the conversion rates before you actually convert the amount. This is extremely useful as it is much more advances than the first code.

###PSEUDOCODE for the first task -
```
BEGIN
INPUT currency to be converted, currency converting to (Pound Sterling/Euro/US Dollar/Japanese Yen)
ASSIGN to variables: c_type1, c_type2
INPUT numb1 as c_type1[key]
MATCH c_type1, c_type2 to key in dictionary
IF c_type1 != Pound Sterling and c_type2 != Pound Sterling:
    CONVERT c_type1 into Pound Sterling
    CONVERT Pound Sterling into c_type2
    RETURN int of c_type2
ELSE:
    IDENTIFY Pound Sterling as c_type1 or c_type2
    CHANGE this value to or from Pound Sterling
    RETURN int of c_type2
```
###Python code for the first task (This worked, however not how I wanted it to.)
```python
allowables = ["pounds", "dollars", "euro", "yen"]
rates = [1,1.68,1.23,171.61] 
pounds = 'pounds'
dollars = 'dollars'
yen = 'yen'
euro = 'euro'
print("Welcome to the currency converter")

var1 = None
while var1 not in range(len(allowables)):
    print('Please type the currency code you wish to convert from')
    for index, currency in enumerate(allowables):
        print ('enter {0} for {1}'.format(index, currency))
    var1 = input("Please type what currency you wish to convert from ")
var1 = int(var1)

var2 = None
while var2 not in range(len(allowables)):
    print('Please type the currency code you wish to convert to')
    for index, currency in enumerate(allowables):
        print ('enter {0} for {1}'.format(index, currency))
    var2 = input("Please type the currency that you wish to convert to ")
var2 = int(var2)

var3 = float(input("Please type the amount of currency you wish to convert "))

amount = var3/rates[var1] *rates[var2]
print(' your converted amount is {0} {1}'.format(amount,allowables[var2]))
```
###Successful code (attempt 2, exactly how I wanted)
```python
currencies= {
    "GBP": 1, 
    "EUR": 1.2, 
    "USD": 1.6, 
    "JPY": 200
    }
#This is a dictionary storing the easily changeable exchange rates for each: GBP, EUR, USD and JPY.

def get_c(dr):
    '''This function ensures that the currencies inputted by user are of the valid currencies:
    if it is, it returns which currency has been inputted,
    if it isn't, it asks the user to input again'''
    answer = ""
    while answer not in ["GBP", "EUR", "USD", "JPY"]:
        answer = raw_input("Please enter a valid currency to convert {0}- GBP/EUR/USD/JPY: ".format(dr))
        answer = answer.upper()
    else:
        print "You entered %s" %answer
    return answer

c_type1 = get_c("from")
c_type2 = get_c("to")
#This causes the placeholder: '{0}' in line 15 to be either "to" or "from", depending on which is converted from and which is converted to

def rate(c_type1, c_type2):
    '''This function just prints the line below, with the placeholders representing the exchange rate and the currency'''
    print ("Exchange rate is {0}{1} to {2}{3}".format( currencies[c_type1], c_type1, currencies[c_type2], c_type2))

rate(c_type1, c_type2)
#This calls the function using the variables c_type1 and c_type2 in the function

numb1 = float(raw_input("How much %s do you wish to convert? " %c_type1))
#This stores the answer to the printed question as numb1

def conversion(w, x, y):
    '''This function converts each the chosen currencies using the exchange rates and the starting currency amount'''
    if w == "GBP":
        z = y * float(currencies[x])
        return round(z, 2)
    elif x == "GBP":
        z = y / float(currencies[w])
        return round(z, 2)
    else:
        z = y / float(currencies[w])
        z = z * float(currencies[x])
        return round(z, 2)

print "%.2f %s is %.2f %s" %(numb1, c_type1, conversion(c_type1, c_type2, numb1), c_type2)
#This prints out the results of the conversion, using the starting currency, the result of the conversion and the currency types
```
###Development and Evaluation
I think the final code is very successful. It works exactly how I wanted it to and I think I have done a good job. Next time however I would link it to an automatically updating currency converting website, so that the conversion rates are never wrong. In this code, if they are wrong the user simply has to go into the code and change the rates manually
###Task 2 -

###Design
The task was to create a database that -

1) A system that stores: a) Surname and First name. b) Two lines of address and postcode. c) A telephone number. d) date of birth. e) email address.

2) A search feature which iterates through the entries.

3) Can search through the surname entries and displays a contact.

4) Can search through the date of birth entries by month and display entries within this month.
###Programming Techniques
####input - this will tell the program whether the user wants to create and entry or to search for one
####output - if it is a valid search the program will output the information of the person they were trying to search. If it is not valid it will print 'no results found'
####file - create file, this was used to store all of the information in the database for the user to search. open file, this was used when the user was searching. The program would open the database and then the program would search for a line that has the relevant information and read file, this is where the program would read the file line by line
####variable - this is used to name something. I used a variable that was temp1. I should have named it something useful, like I did in Task 1
####for loop - this is used when the program is searching in the database on each line
####if loop - if the program has found the correct information it will print it
####search criteria - so the user could search for certain aspects in the database. The criteria is stated in the first part of the code
####line with file - this can find the information in the database
```python
elif answer == "2" : #if the user enters 2 it means they want to search
    print ("This is where we search") #tells the user they are searching
    searchcriteria = raw_input("Enter your search Criteria: Name, Phone Number, Address, Email, Postcode, or Town ") #these are the things the user can search for
    print searchcriteria #this prints everything the user can search for
    temp1 = open("addressbookdata","r") #temporatily opens the addressbook file
    for line in temp1: #if it is in the line
        if searchcriteria in line: #if the search criteria is correct,
            print line  #print this line
        else: #if not, print no results found
            print ("No results found")
```
###Possible Problems
The main problem that I could encounter would be if the user entered a search criteria that was not valid. This could be hard to create a code that is only going to show information that the user wants to see. I think it will also be hard to be able to find a file by month. So instead of using letters, the user will have to search using '04' for example, this would search for someone that was born in the month April. I do not think this is too bad, as it still shows the month that the person was born in. I could not actually implement something that would allow the user to delete file's in the database, however this can easily be done if the user looks into the text file which has all the file's in it. The program links to the text file that holds all the information, so this would work very well.

###First PSEUDOCODE for the second task -
```
BEGIN
CHOOSE either create an entry or search an entry
IF creating:
    INPUT details:
                  -lastname
                  -firstname
                  -phone
                  -email
                  -address
                  -postcode
STORE details in addressbookdata
Print ('Data Entry Successful')

ELSE IF searching:
    INPUT information being searched
    FOR each category conatining necessary data 
Print whole data entry

ELSE Print ('No Results Found')
End
```
###Second PSEUDOCODE for the second task –
```
BEGIN

CHOOSE either search by surname or search by birthday month
IF by surname:
    INPUT surname to be searched
    FOR each surname:
        IF surname == surname entered:
            PRINT whole address entry

ELSE IF by birthday month:
    INPUT birthday month to be searched (number format)
    FOR each birthday month digits (mm of dd/mm/yy) in each address entry:
        IF birthday month == birthday month entered:
            PRINT whole address entry

END
```
```
addressbookdata contains:
Jackson, Samantha, 2 Heather Row, Basingstoke, RG21 3SD, 01256 135434, 23/04/1973, sam.jackson@hotmail.com
Vickers, Jonathan, 18 Saville Gardens, Reading, RG3 5FH, 01196 678254, 04/02/1965, the_man@btinternet.com
Morris, Sally, The Old Lodge, Hook, RG23 5RD, 01256 728443, 19/02/1975, smorris@fgh.co.uk
Cobbly, Harry, 345 The High Street, Guildford, GU2 4KJ, 01458 288763, 30/03/1960, harry.cobbly@somewhere.org.uk
Khan, Jasmine, 36 Hever Avenue, Edenbridge, TN34 4FG, 01569 276524, 28/02/1980, jas.khan@hotmail.com
Vickers, Harriet, 45 Sage Gardens, Brighton, BN3 2FG, 01675 662554, 04/04/1968, harriet.vickers@btinternet.com
```
###Python code for the second task –
```python
answer = raw_input("Are You Creating An Entry [Press 1] \nOr Are You Searching An Entry [Press 2] ") 
#this line finds out whether the user wants to create or search

# IF we are creating 

if answer == "1" : 
    #print ("This is where we create")
    # collect information

    lastname = raw_input("What is the persons last name? ") #these lines gets all the person's information to store
    firstname = raw_input("What is the persons first name? ")
    phone = raw_input("What id the persons phone number? ")
    email = raw_input("What is the persons email address? ")
    address = raw_input("What is the persons address? ")

    #create or append addressbookdata

    temp1 = open("addressbookdata","a")
    
    #create string to print to file
    #print temp1
    #print (firstname + " " + lastname + ", " + phone + ", " + email + ", " + address) 

    temp1.write(firstname + " " + lastname + ", " + phone + ", " + email + ", " + address)
    temp1.write("\n")

# SEARCHING FOR A RECORD

elif answer == "2" :
    print ("This is where we search")
    searchcriteria = raw_input("Enter your search Criteria: Name, Phone Number, Address, Email, Postcode, or Town ")
    print searchcriteria
    temp1 = open("addressbookdata","r") #this opens the text file of the database to search frrom
    for line in temp1:
        if searchcriteria in line:
            print line  #this will print the information frrom the database
        else:
            print ("No results found") #if no file can be found


# USER DID NOT PICK CREATE OR SEARCH 

else:
    print ("Incorrect Answer")
    exit()
```
###Development and Evaluation
I am very happy with this code. It works efficiently and does what it needs to. Instead of only searching by surname and date of birth, I added a feature where the user can enter any information about a person, and the program will look in the database and print all of that person’s information,.
###Task 3

###Design -
The task was to create a program that will take in a 10 digit number and calculate the correct 11 digit ISBN.

a) the number entered must be the correct length

b) only contains the digits 0 to 9.
###Programming Techniques
####while – I used this at the start of the code, to check that the amount of numbers that the user entered was equal to 10.
####input – so the user could enter their 10 digits
####output (print) – so that the user could see what their ISBN number actually was
####int() – this turns the numbers in the list into an integer

###Possible problems
The main problem of this task would be to make sure the user has not entered any letters, and also that they have entered a 10 digits. This will be hard to stop, as I am not sure exactly how am I going to make sure that the user has entered 10 digits, however I will look into it. One other problem is to make the code output the original 10 numbers and then the ISBN number added onto it, howvever I think I can do this by using print and then adding some other code onto it that stores the 10 digit number that was first entered at the start of the program.
###PSEUDOCODE for the third task -

```
Asks the user to input ten numbers
If the digit number is not 10 it then loops to enter a 10 digit number
Once the user has input a 10 digit number
Program calculates ISBN number
Outputs the 10 digit number with ISBN number on the end
```
###Python code for the third task -
```python
ISBN=''

while len(str(ISBN))!=10:

    print('Please make sure you have entered a number which is exactly 10 characters long.')
    ISBN=raw_input('Please enter the 10 digit number: ')
    

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
```
###Development and Evaluation
This was the easiest code to create out of all of them, this was because it was rather simple to create the calculation code, surprisingly at the start I thought it would actually be the hardest. There is nothing I think I could improve on for this code, apart from create a loop so that at the end of the program, it would ask if the user wanted to find another ISBN number. I would have done this if I had a bit more time.



