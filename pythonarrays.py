import numpy as numpy

# Initializing the array to include random integers from 0-10 (excluding 10)
# and be dimensions 5x5 with only integers
homework_array = numpy.random.randint(0,10, size=(5,5), dtype=int)

# Printing the array
print(homework_array)

# Printing the random number from the 2nd row, 3rd column
print(f'\nThe element in the 2nd row 3rd column is: {homework_array[1][2]}')

# Print the sum of all elements in the array
sum = numpy.sum(homework_array)
print(f'\nThe sum of all elements in the array is: {sum}\n')

# Printing the mean of each row and max number of each row
# Creating an array of the mean of each row using numpy
mean = numpy.mean(homework_array, axis=1)

# Creating an array of max numbers from each row
max_number = numpy.amax(homework_array, axis=1)

i = 0
row_num = 1
# Creating a while loop to print a clear statement showing the mean and max number for each specific row
while i < 5:
    print(f'The mean on row {row_num} is {mean[i]} and the max number is {max_number[i]}')
    i += 1
    row_num += 1
