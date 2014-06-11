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
    print ("this is where we search")
    searchcriteria = raw_input("Enter your search Criteria, name? phone number etc ")
    print searchcriteria
    temp1 = open("addressbookdata","r")
    for line in temp1:
        if searchcriteria in line:
        print line


# USER DID NOT PICK CREATE OR SEARCH 

else :
    print ("Incorrect Answer")
    exit()
