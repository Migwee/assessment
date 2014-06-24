#Controlled Assessment Report

##Task 1 -

###Design
The task was to create a currency converter that -

a) Has exchange rates that can be regularly changed by the user. 

b) User should be able to enter an amount, select chosen currency, and the currency to convert it into. 

c) Figure shown should be to two decimal places.

The Currencies required to convert are: GBP (£) Euro (€) USD ($) and JPY (¥).
###Possible Problems
There are a few problems that I have thought may occur. One of these would be what would happen if I entered a letter instead of a number when converting. After testing my code, when I enter a letter, the program simply stops, and gives an error. Another problem I thought of is where the currency changes over time. This may cause incorrect currency rates. However this can be edited in the code itself on the second line. If I had more time I would have tried to link the rates to a automatically updating currency converting website, and get the rates directly from there. However, I did not have enough time to do this. I would also make a whiel loop in the code. This would make it so that after you have converted an amount of money, you could then convert something else, instead of the program stopping
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
rates = [1,1.68,1.23,171.61] #this is where the user can change the conversion rates if they do change
pounds = 'pounds'
dollars = 'dollars'
yen = 'yen'
euro = 'euro'
print("Welcome to the currency converter") #this line welcomes the user

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

def rate(c_type1, c_type2):
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

numb1 = float(raw_input("How much %s do you wish to convert? " %c_type1))

def conversion(w, x, y):
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
```
###Task 2 -

###Design
The task was to create a database that -

1) A system that stores: a) Surname and First name. b) Two lines of address and postcode. c) A telephone number. d) date of birth. e) email address.

2) A search feature which iterates through the entries.

3) Can search through the surname entries and displays a contact.

4) Can search through the date of birth entries by month and display entries within this month.
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
###Python code for the second task
```
answer = raw_input("Are You Creating An Entry [Press 1] \nOr Are You Searching An Entry [Press 2] ")

# IF we are creating 

if answer == "1" : 
    #print ("This is where we create")
    # collect information

    lastname = raw_input("What is the persons last name? ")
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
    temp1 = open("addressbookdata","r")
    for line in temp1:
        if searchcriteria in line:
            print line 
        else:
            print ("No results found")


# USER DID NOT PICK CREATE OR SEARCH 

else:
    print ("Incorrect Answer")
    exit()
```
