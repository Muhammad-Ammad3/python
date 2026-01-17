#


# \""
# \'
# \\
# \n
# course_name = "Python \nProgramming"
# print(course_name)

# first_name = "Muhammad"
# last_name = "Ammad"
# full_name = f"{first_name} {last_name}"
# print(full_name)

# course = "python programming    "
# print(course.upper())
# print(course.lower())
# print(course.title())
# print(course.strip())
# print(course.find("pro"))
# print(course.replace("p", "j"))
# print("prg" in course)
# print("prg" not in course)


# print(10 + 3)
# print(10 - 3)
# print(10 * 3)
# print(10 / 3)
# print(10 // 3)
# print(10 % 3)
# print(10 ** 3)

# import math

# print(round(2.9))
# print(abs(-2.9))
# print(math.ceil(3.1))

# x = input("x:")
# print(type(x))
# y = int(x) + 1
# print(f"x: {x}, y: {y}")

# temperature = input("Temperature: ")
# temp = int(temperature)
# if temp > 30:
#     print("It's a hot day")
#     print("Drink plenty of water")
# elif temp > 20:
#     print("It's a nice day")
# else:
#     print("It's cold day")
# print("Done")

# age = 21
# if age > 18:
#     message = "eligible"
# else:
#     message = "not eligible"

# message = "eligible" if age >= 18 else "not eligible"

# print(message)

# high_income = True
# good_credit = True
# student = True
# if (high_income and good_credit) and not student:
#     print("Eligible for loan")
# else:
#     print("Not eligible for loan")

# age should be between 18 and 65 to work
# age = 18
# if age >=18 and age <=65:
# if 18 <= age < 65:
# print("Eligible to work")

# if 10 == "10":
#     print("a")
# elif "bag" > "apple" and "bag" > "cat":
#     print("b")
# else:
#     print("c")

# for number in range(1, 10, 2):
#     print("Attempt", number, number * ".")

# successful = True
# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")

# for x in range(1, 5):
#     for y in range(1,3):
#         print(f"({x} , {y})")

# number = 100
# while number > 0:
#     print(number)
#     number //=  2

# command = ""
# while command.lower() != "quit":
#     command = input(">")
#     print("ECHO", command)

# while True:
#     command = input(">")
#     print("ECHO", command)
#     if command.lower() == "quit":
#         break

count = 0
for number in range(1, 10):
    if number % 2 == 0:
        count += 1
        print(number)
print(f"we have {count} even numbers")