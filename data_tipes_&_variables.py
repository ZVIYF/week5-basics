# תרגיל 1

first_name = "David"
last_name = "Cohen"
age = 25
city = "Tel Aviv"
email = "david@gmail.com"

print("===== User Details =====")
print(f"First Name: {first_name}") 
print(f"Last Name: {last_name}") 
print(f"Age: {age}") 
print(f"City: {city}") 
print(f"Email: {email}") 
print("========================")


# # # # # # # # # # # #

# תרגיל 2

birth_year = 2001
current_year = 2026
print(f"You are approximately {current_year - birth_year} years old.")


# # # # # # # # # # # # 

# תרגיל 3

width = 5
height = 10

print(f"The area of the rectangle is {width * height}")
print(f"The circumference of the rectangle is {(width * 2) + (height * 2)}")


# # # # # # # # # # # #

# תרגיל 4

name = "David"
age = 25
height = 1.78
is_student = True
salary = 8500

print("Name:", name, type(name))
print("Age:", age, type(age))
print("Height:", height, type(height))
print("is_student:", is_student, type(is_student))
print("Salary:", salary, type(salary))


# # # # # # # # # # # # 

#        חלק ב'       #

# # # # # # # # # # # #

# תרגיל 5

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
city = input("Enter your city: ")
age = input("Enter your age: ")

print(f"Welcome {first_name, last_name}, you live in {city} and you are {age} years old.")


# # # # # # # # # # # #


# תרגיל 6

number_1 = int(input("Enter a number: "))
number_2 = int(input("Enter a second number: "))

print(f"{number_1} + {number_2} = {number_1 + number_2}")
print(f"{number_1} - {number_2} = {number_1 - number_2}")
print(f"{number_1} * {number_2} = {number_1 * number_2}")
print(f"{number_1} / {number_2} = {number_1 / number_2}")


# # # # # # # # # # # # 

# תרגיל 7

product_name = input("Enter product name: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))

print("====== Purchase Receipt ======")
print(f"Product: {product_name}")
print(f"Price: {price}")
print(f"Quantity: {quantity}")
print(f"Total: {quantity * price}")
price("==============================")


# # # # # # # # # # # 


# תרגיל 9

employee_name = input("Enter employee name: ")
hours = float(input("Enter hours (monthly): "))
hourly_rate = float(input("Enter hourly rate: "))

print("====== Monthly paycheck ======")
print(f"Employee: {employee_name}")
print(f"hours: {hours}")
print(f"Hourly rate: {hourly_rate}")
print(f"Paycheck: {hours * hourly_rate}")
price("==============================")


# # # # # # # # # # #

# תרגיל 11

subtotal_bill = float(input("Enter bill total: "))
tip_percentage = float(input("Enter tip percentage: "))
number_of_guests = int(input("Enter number of guests: "))

print(f"Tip: {subtotal_bill * (tip_percentage / 100)}")
print(f"total: {subtotal_bill * (1 + (tip_percentage / 100))}")
print(f"total: {(subtotal_bill * (1 + (tip_percentage / 100))) / number_of_guests}")


# # # # # # # # # # # 

# תרגיל 12

a = 10
b = 20
c = a
a = b
b = c


# # # # # # # # # # # 


