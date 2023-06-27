# Write a lambda function that takes two arguments and returns their sum.

sum=lambda x,y: x+y
print(sum(2,3))

# Create a lambda function that calculates the square of a given number.

square=lambda x:x*x
print(square(2))

# Write a lambda function to check if a number is even or odd.

even_odd = lambda x: 'even' if x % 2 == 0 else 'odd'
print(even_odd(3))

# Create a lambda function to convert a string to uppercase.

upper=lambda x: x.upper()
print(upper('animal'))

# Write a lambda function that sorts a list of strings in alphabetical order.

sort_list=lambda x: sorted(x)
print(sort_list(['z','A','B','a']))

# Create a lambda function that filters out all the numbers divisible by 3 from a given list.

filter_list=lambda x: [num for i,num in enumerate(x) if not num % 3 == 0]
print(filter_list([1,2,3,6,9]))

# Write a lambda function to compute the product of two numbers.

prod=lambda x,y: x*y
print(prod(5,6))


# Create a lambda function that finds the maximum value in a list of integers.

max_val=lambda x:max(x)
print(max_val([1,2,3,4]))

# Write a lambda function that concatenates two strings with a space in between.

concatenate=lambda x,y: x + " " + y
print(concatenate('Python','Everyday'))

# Create a lambda function that counts the number of characters in a string.

string_len =lambda x:len([*x])
print(string_len('Hello'))