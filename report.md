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
#list - I used this to list the four currencies (Pound Sterling, Euro, Yen and Dollars)
sesnsible variable name - I could have used any variable, however throughtout my code I set the variables the sensible names, for example c_type1 represents currenct type 1. short_hand represents the short version of the currency
#def function - I used this as functions are useful to repeat tasks without returning values
#input - I used this to store the input, this was then used later on to convert
#output - I used output to show the user what their converted amount was
#if statement - I used this so the program could tell what the user wanted to conver to and from, and when it knew that, it could then do the calculations to find out the converted amount.
#if loop - if, elif, else. I used if loop as I used (x,y,z). Which was used to convert at the end of the program. If it was not one calculation, elif was used, and if it was not that, else was then used.
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
    "Pound Sterling": 1, 
    "Euro": 1.2, 
    "US Dollar": 1.25
    "Japanese Yen": 171.07
    }
#This is a dictionary storing the easily changeable exchange rates for each: GBP, EUR, USD and JPY.

short_hand = {
    "GBP": "Pound Sterling",
    "EUR": "Euro",
    "USD": "US Dollar",
    "JPY": "Japanese Yen"
    }
#This is a dictionary showing the programmer which three letter code relates to which currency.

print short_hand
#This shows the user which currency relates to which three letter code.

c_type1 = raw_input("What Currency are you converting from? GBP/EUR/USD/JPY: ")
c_type1 = c_type1.upper()
#This allows the user to input a currency to convert from and stores it as the variable 'c_type1' and then capitalises it for the program to read.

if c_type1 == "GBP" or "EUR" or "USD" or "JPY":
    "You entered %s" %(c_type1)
else:
    print c_type1, "is not a valid input"
    c_type1 = raw_input("Please enter a valid currency to convert from- GBP/EUR/USD/JPY: ")
    
c_type2 = raw_input("What Currency are you converting to? GBP/EUR/USD/JPY: ")
c_type2 = c_type2.upper()

if c_type2 == "GBP" or "EUR" or "USD" or "JPY":
    "You entered %s" %(c_type1)
else:
    print c_type2, "is not a valid input"
    c_type2 = raw_input("Please enter a valid currency to convert to- GBP/EUR/USD/JPY: ")

def rate(c_type1, c_type2): #this is used after the user chooses what they want to convert to and from
    if c_type1 == "GBP":
        print "exchange rate is", currencies["Pound Sterling"]
    if c_type1 == "EUR":
        print "exchange rate is", currencies["Euro"]
    if c_type1 == "USD":
        print "exchange rate is", currencies["US Dollar"]
    if c_type1 == "JPY":
        print "exchange rate is", currencies["Japanese Yen"]
    if c_type2 == "GBP":
        print "to", currencies["Pound Sterling"]
    if c_type2 == "EUR":
        print "to", currencies["Euro"]
    if c_type2 == "USD":
        print "to", currencies["US Dollar"]
    if c_type2 == "JPY":
        print "to", currencies["Japanese Yen"]

rate(c_type1, c_type2)

numb1 = float(raw_input("How much %s do you wish to convert? " %c_type1)) #this asks the user how much they want to convert

def conversion(w, x, y):  #this does the calculations for the convertor
    if w == "GBP":
        z = y * float(currencies[short_hand[x]])
        return round(z, 2)
    elif x == "GBP":
        z = y / float(currencies[short_hand[w]])
        return round(z, 2)
    else:
        z = y / float(currencies[short_hand[w]])
        z = z * float(currencies[short_hand[x]])
        return round(z, 2)

print "%.2f %s is %.2f %s" %(numb1, short_hand[c_type1], conversion(c_type1, c_type2, numb1), short_hand[c_type2])
#this prints the converted amount
```
###Task 2 -

###Design
The task was to create a database that -

1) A system that stores: a) Surname and First name. b) Two lines of address and postcode. c) A telephone number. d) date of birth. e) email address.

2) A search feature which iterates through the entries.

3) Can search through the surname entries and displays a contact.

4) Can search through the date of birth entries by month and display entries within this month.
###Programming Techniques
#input - where the user inputs
#output - if it is a valid search the program will output the information
#file - create file, open file and read file
#variable - 
#for loop - 
#if loop - if the user said 2 or 1
#search criteria - so the user could search for certain aspects in the database
#line with file - this can find the information in the database
```
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

###PSEUDOCODE for the second task -
```
Welcome the user to the address book     
The address book will then ask the user to input 1 or 2 to select if they want to add or search for a file on the database
If the user inputs 1 they will be able to create an entry
It will ask them to make an address based of their:
First name
Last name
Telephone
Email 
Address
Once this process is done it will add it to the address book to be search for at a later date
If the user inputs 2 then it will take them to the search engine
It will give the user a list of searching options
The user will input any information about the person and the computer will find anyone in the address book with that information
It will then print to the user all of the people with that information
If there is no valid search, the program will end
The program will then end
```
###Python code for the second task -
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
###Task 3

###Design -
The task was to create a program that will take in a 10 digit number and calculate the correct 11 digit ISBN.

a) the number entered must be the correct length

b) only contains the digits 0 to 9.
###Programming Techniques

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


