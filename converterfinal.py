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
