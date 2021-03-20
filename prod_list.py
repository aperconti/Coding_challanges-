#imports
import numpy as np

#list to be multiplied
num_list = [1, 2, 3, 4, 5]
prod_list=[]

# using numpy.prod() to get the multiplications
prod_total= np.prod(num_list)

#print prod to double check it is correct
print(prod_total)

# for loop to divide prod_total by the ints in list. Append these ints to new list (prod_list) and print the list.
for i in num_list:
    new_addition = prod_total / i
    prod_list.append(new_addition)
print(prod_list)


