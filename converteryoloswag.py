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
