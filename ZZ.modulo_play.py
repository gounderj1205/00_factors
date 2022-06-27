# Modulo example
keep_going = ""
while keep_going == "":

    num_lollies = int(input("How many lollies? "))
    num_students = int(input("how many students? "))

    # Lollies per student (divide)
    lollies_per_student = num_lollies // num_students
    lollies_left = num_lollies % num_students

    # output fixer (lolly vs lollies)
    if lollies_left == 1:
        lolly_pl = "lolly"
    else:
        lolly_pl = "lollies"

    # output...
    print()
    print("you have {} lollies and {} students"
        .format(num_lollies, num_students))
    print("Each student gets {} lollies".format(lollies_per_student))
    print("you have {} {} left".format(lollies_left, lolly_pl))
    print()

    keep_going = input("again <enter>? ")
    print()

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