allowables = ["pounds", "dollars", "euro", "yen"]
rates = [1,2,3,4]
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

ammount = var3/rates[var1] *rates[var2]
print(' your converted ammount is {0} {1}'.format(ammount,allowables[var2]))

#[GBP]


# if var1 == pounds and var2 == dollars:
#     sumusd1 = var3 * 1.64
#     print("You will recieve, ", sumusd)
# elif something != somethingelse: 
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == pounds and var2 == euro:
#     sumeuro = var3 * 1.22
#     print("You will recieve, ", sumeuro)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == pounds and var2 == yen:
#     sumyen = var3 * 171.53
#     print("You will recieve, ", sumyen)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# #[USD]
# if var1 == dollars and var2 == pounds:
#     sumpounds = var3 * 0.61
#     print("You will recieve, ", sumpounds)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == dollars and var2 == euro:
#     sumeuro = var3 * 0.74
#     print("You will recieve, ", sumeuro)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == dollars and var2 == yen:
#     sumyen = var3 * 104.16
#     print("You will recieve, ", sumyen)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# #[EURO]
# if var1 == euro and var2 == dollars:
#     sumusd2 = var3 * 1.64
#     print("You will recieve, ", sumusd)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == euro and var2 == pounds:
#     sumpounds = var3 * 0.82
#     print("You will recieve, ", sumpounds)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == euro and var2 == yen:
#     sumyen = var3 * 141.24
#     print("You will recieve, ", sumyen)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# #[YEN]
#     if var1 == yen and var2 == dollars:
#         sumusd3 = var3 * 0.0096
#     print("You will recieve, ", sumusd3)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == yen and var2 == euro:
#     sumeuro = var3 * 0.0071
#     print("You will recieve, ", sumeuro)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
# if var1 == yen and var2 == pounds:
#     sumpounds = var3 * 0.0058
#     print("You will recieve, ", sumpounds)
# elif something != somethingelse:
#     print("Sorry, an error has occurred, please input a currency")
#     print(var1)
