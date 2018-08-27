#7. Write a Python program to count the number 4 in a given list


print('Enter numbers for the list: ')
numbers = list(map(int,input().split(' ')))

four = numbers.count(4)

print('No of 4 in list are : ' + str(four))

print(numbers)
