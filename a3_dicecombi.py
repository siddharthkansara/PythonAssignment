# All Dice Combinations. Write a list comprehension that uses nested for-clauses to create a single list with 
# all 36 different dice combinations from (1,1) to (6,6).


a = [1,2,3,4,5,6]

c = [(n,x) for n in a for x in a]

print(c)