#3. Write a Python program to accept a filename from the user and print the extension of that.

filename = input('Enter filename with the extension: ')

Fe = filename.split('.')

print(Fe[1])