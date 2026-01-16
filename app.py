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

high_income = True
good_credit = True
student = True
if (high_income and good_credit) and not student:
    print("Eligible for loan")
else:
    print("Not eligible for loan")
