# print("Hello, World!")

# a = 5
# b = 6
# c = 7

# s = (a + b + c) / 2

# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# print('The area of the triangle is %0.2f' %area)
# x= 15
# x = x% 3
# print(x)

# a = 7
# b = 2

# print ('Sum: ', a + b)  

# print ('Subtraction: ', a - b)   

# print ('Multiplication: ', a * b)  

# print ('Division: ', a / b) 

# print ('Floor Division: ', a // b)

# print ('Modulo: ', a % b)  

# print ('Power: ', a ** b) 

# a = 10

# b = 5 

# a += b      # a = a + b

# print(a)


# a = 5

# b = 2

# print('a == b =', a == b)

# print('a != b =', a != b)

# print('a > b =', a > b)

# print('a < b =', a < b)

# print('a >= b =', a >= b)

# print('a <= b =', a <= b)


# second class



# first function 
def add_numbers(a, b):
    sum = a + b
    print('Sum:', sum)

add_numbers(2, 3)



# second function 
def add_numbers( a = 7,  b = 8):
    sum = a + b
    print('Sum:', sum)
# function call with two arguments
add_numbers(2, 3)
#  function call with one argument
add_numbers(a = 2)
# function call with no arguments
add_numbers()



# third Function 
def display_info(first_name, last_name):
    print('First Name:', first_name)
    print('Last Name:', last_name)

display_info(last_name = 'Muhammad', first_name = 'Ammad')



# fifth function 
# program to find sum of multiple numbers 

def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)




