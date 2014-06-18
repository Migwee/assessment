#Controlled Assessment Report

##Task 1 -

###Design
The task was to create a currency converter that -

a) Has exchange rates that can be regularly changed by the user. 

b) User should be able to enter an amount, select chosen currency, and the currency to convert it into. 

c) Figure shown should be to two decimal places.

The Currencies required to convert are: GBP (£) Euro (€) USD ($) and JPY (¥).

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
