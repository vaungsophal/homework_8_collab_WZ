
# Define the function
def replace_last(numbers):   
    
    # if the list is blank return nothing
    if not numbers:
        return numbers
    
    # Grab the last number with pop(-1) and store it as last number
    last_number = numbers.pop(-1)

    # insert last_number we stored into position 0 of list numbers
    numbers.insert(0, last_number)

    # send it!
    return numbers

## Quick interface to test ##
# creating an empty list
numbers = []

# getting the user to inut numbers
num = input("Enter some numbers with a space between them ")

#break the input up into parts and add them to a list
numbers = num.split() 

#convert the strings from above into int
for y in range(len(numbers)): 
    numbers[y] = int(numbers[y]) 

# run the function and output results
output=replace_last(numbers)

# display stuff
print(output)
