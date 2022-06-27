# Functions go here

# puts series of symbols at start and end of text (for emphasis)
def statement_generator(text, decoration) : 

    # make string with five characters 
    ends = decoration * 5

    # add decoration to start and end of statement
    statement = "{} {} {}". format(ends, text, ends)

    print()
    print(statement)
    print()

    return ""


# displays instructions / infomation
def instructions():

    statement_generator("Instructions / Information", "=")
    print()
    print("please choose a data type (image / text / integer")
    print()
    print("This program assumes that images are being rpresented in 24"
    "bit color(ie: 24 bits per pixel). For text, we assume ascii"
    "encoding is being used (8 bits per chracter).")
    print()
    print("Complete as many calculations as necessary, pressing <enter> at"
    "the end of each calculation or any key to quit.")
    print()
    return ""


# checks input is a number more than a given value
def num_check(question):

    valid = False
    while not valid:

        error = "please enter a number that is more than zero"
        
        try:
    
            # ask user to enter a number
            response = float(input("enter a number: "))

            # checks number is more than 200
            if 1 >= response <= 200:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)


# gets factors, returns a sorted list
def get_factors(to_factor):
     #list to hold factors
    factors = []

    #Square root to factor to find 'half-way'
    limit = int(to_factor**0.5)

    #Find factor pairs and add list
    for item in range(1, limit + 1):

        #checl factor is not 1 (unity)
        if to_factor == 1:
            break

        # Check if number is a factor 
        result = to_factor % item
        factor_1 = int(to_factor // item)

        # add factor to a list if it is not already in there
        if result ==0:
           factors.append(item)
        
        if factor_1 !=item and result == 0:
                factors.append(factor_1)            

    # output
    factors.sort()
    
    return factors

       




# Main Routine goes here

# Head
statement_generator("Factors Calculator", "-")

# Display instructions if user has not used the program before
first_time = input("press <enter> to see the instructions or any key to continue")

if first_time == "": 
    instructions()

# Loop to allow multiple calculations per session
keep_going = ""
while keep_going == "":

    comment = ""

    # ask user for number to be factored...
    var_to_factor = num_check ("Number? ")
    
    if var_to_factor != 1:
        factor_list = get_factors(var_to_factor)
    else:
        factor_list = ""
        comment = "One is UNITY! It only has one factor. Itself :)"

    # comments for squares / primes
    if len(factor_list) == 2:
        comment = "{} is a prime number.".format(var_to_factor)
    elif len(factor_list) % 2 == 1:
        comment = "{} is a perfect square".format(var_to_factor)

    # output factors and comment

    # Generate heading...
    if var_to_factor == 1:
        heading = "One is speacial..."

    else:
        heading = "Factors of {}".format(var_to_factor)

    # Output factors and comment
    statement_generator(heading, "*")
    print()
    print(factor_list)
    print(comment)

    print()
    keep_going = input("press <enter> to continue or any key to quit")
    print()

print()
print("Thank you for using the factors calculator")
print()