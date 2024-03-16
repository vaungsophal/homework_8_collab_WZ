def index_power(numbers, n):
    # Check if list has enough elements for index n
    if len(numbers) > n:
        # Calculate and return the result
        return numbers[n] ** n
    else:
        # Return -1 if index n is out of range
        return -1

# Get user input for list of numbers separated by commas
user_input = input("Enter a list of numbers separated by commas: ").split(",")
numbers_list = []
# Add user input elements to numbers_list as integers
for num in user_input:
    numbers_list.append(int(num))

# Get user input for value of n
n = int(input("Enter the value of n: "))

# Calculate and print the result
result = index_power(numbers_list, n)
print(result)
