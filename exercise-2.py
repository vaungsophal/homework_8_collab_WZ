def index_power(numbers, n):
    if len(numbers) > n:
        return numbers[n] ** n
    else:
        return -1

# # Testing
# numbers_1 = [1, 2, 3, 4]
# numbers_2 = [1, 3, 10, 100]
# numbers_3 = [0, 1]
# numbers_4 = [1, 2]

# print(index_power(numbers_1, 2))
# print(index_power(numbers_2, 3)) 
# print(index_power(numbers_3, 0)) 
# print(index_power(numbers_4, 3))
