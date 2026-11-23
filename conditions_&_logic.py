# תרגיל 1

def age_check():
    age = int(input("Enter age: "))
    if age >= 18:
        print("Adult")
    else:
        print("Minor")


# # # # # # # 

# תרגיל 2

def is_positive():
    number = int(input("Enter number: "))
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    elif number == 0:
        print("Zero")


# # # # # # # 

# תרגיל 3

def is_even():
    number = int(input("Enter number: "))
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")


# # # # # # # #

# תרגיל 4

def bigger_number():
    number1 = int(input("Enter number: "))
    number2 = int(input("Enter number: "))
    if number1 > number2:
        print("Bigger:", number1)
    elif number2 > number1:
        print("Bigger:", number2)
    else:
        print("Numbers are even")


# # # # # # # 

# תרגיל 5

def check_password():
    password = "Python123"
    user_pass = input("Enter your password: ")
    if user_pass == password:
        print("Access Granted")
    else:
        print("Access Denied")


# # # # # # # #

# תרגיל 6

def check_in_range():
    number = int(input("Enter a number"))
    if 1 <= number <= 10:
        print("1-10")
    elif 11 <= number <= 50:
        print("11-50")
    elif 51 <= number <= 100:
        print("51-100")
    else:
        print("Not in range")


# # # # # # # 

# תרגיל 7

def grades_system():
    grade = int(input("Enter grade: "))
    if 90 <= grade <= 100:
        print("Excellent")
    elif 80 <= grade <= 89:
        print("Very Good")
    elif 70 <= grade <= 79:
        print("Good")
    elif 60 <= grade <= 69:
        print("Passed")
    elif 0 <= grade <= 59:
        print("Failed")
    else:
        print("Invalid Grade")


# # # # # # # # #

# תרגיל 8

def check_user_and_password():
    correct_username = "admin"
    correct_password = "123456"
    username = input("Enter username: ")
    user_password = input("Enter password: ")
    if username != correct_username:
        print("Unknown User")
    elif user_password != correct_password:
        print("Wrong Password")
    else:
        print("Login Successfull")


# # # # # # #

def discount_eligible():
    age = int(input("Enter age: "))
    subtotal = float(input("Enter total: "))
    if age > 60:
        return subtotal * (1 - 0.2)
    elif age < 18:
        return subtotal * (1 - 0.1)
    return subtotal


# # # # # # # 

# תרגיל 10

def check_divisions():
    number = int(input("Enter a number: "))
    if number % 3 == 0:
        print("Divides by 3")
    elif number % 5 == 0:
        print("Divides by 5")
    elif (number % 3 == 0) and (number % 5 == 0):
        print("Divides by 3 and by 5")
    else:
        print("not divided by 5 or 3")


# # # # # # # # 

# תרגיל 11

def check_club_age():
    age = int(input("Enter age: "))
    with_adult = bool(int(input("With adult> [1 - True; 2 - False]")))
    if (age >= 18) or ((age >= 16) and with_adult):
        print("OK (but dont drink too much)")
    else:
        print("Not OK")


# # # # # # # # 

# תרגיל 12

def scolarship_sligible():
    grades_average = float(input("Enter grades average: "))
    income = int(input("Enter Income: "))
    if (grades_average >= 90.0) or ((grades_average >= 85.0) and (income < 5000)):
        print("Eligible")
    else:
        print("Not Eligible")


# # # # # # # # 

# תרגיל 13

def check_acount():
    correct_username = "admin"
    correct_password = "123456"
    is_active = True
    username = input("Enter username: ")
    user_password = input("Enter password: ")
    if username != correct_username:
        print("Unknown User")
    elif user_password != correct_password:
        print("Wrong Password")
    elif not is_active:
        print("Acount not active")
    else:
        print("Login Successfull")


# # # # # # # # 

# תרגיל 14

def check_number_in_range():
    number = int(input("Entaer a number: "))
    if (20 <= number) and (number <= 80):
        print("In range - check 1")
    else:
        print("Not in range - 1")    
    
    if not ((number < 20) or (number > 80)):
        print("In range - check 2")
    else:
        print("Not in range - 2")


# # # # # # # #

# תרגיל 15

def ATM():
    balance = 5000
    withdraw = int(input("Enter withdraw amount: "))
    if withdraw <= 0:
        print("Error:Withdraw amount must be positive") 
    elif withdraw > balance:
        print("Error: Not enough money")
    else:
        balance -= withdraw
        print(balance)


# # # # # # # # # # 

# תרגיל 16

def tic_chack():
    age = int(input("Enter age: "))
    has_membership = bool(int(input("Has Membership? [0 - False ; 1 - True] ")))
    if age < 12:
        price = 25
    elif age < 18:
        price = 35
    else:
        price = 50

    if has_membership:
        price = price * (1 - 0.1)

    print(price)


# # # # # # # #

# תרגיל 17

def loan_eligible():
    age = int(input("Enter age: "))
    income = int(input("Enter income: "))
    seniority = float(input("Enter seniority: "))
    if age >= 21:
        if income >= 7000:
            if seniority >= 1.0:
                print("Eligible")
            else:
                print("not enough seniority")
        else:
            print("income too low")
    else:
        print("too young")


# # # # # # # #

# תרגיל 18

def parking_lot():
    pricing = {
        "motorcicle": 10,
        "sedan": 20, 
        "commercial": 30
        }
    car_type = input("Enter car type: ")
    hours = float(input("Enter hours"))
    price = pricing[car_type] * hours
    if hours > 5.0:
        discount_percent = 0.15
    elif hours < 1.0:
        discount_percent = 0.1
    else:
        discount_percent = 0.0
    total = price * (1 - discount_percent)
    print(total)


# # # # # # # # 

# תרגיל 19

def calculator():
    number1 = int(input("Enter number 1"))
    number2 = int(input("Enter number 2"))
    operator = input("Enter operator [ + - * / ]: ")
    if operator == "+":
        total = number1 + number2
    elif operator == "-":
        total = number1 - number2    
    elif operator == "*":
        total = number1 * number2
    elif operator == "/":
        if number2 != 0:
            total = number1 / number2
        else:
            print("cant divide by 0")
            return
    else:
        print("Error: Operator has not been set")
        return
    print(number1, operator, number2, "=", total)


# # # # # # # # # #

# תרגיל 20

def check_leap_year():
    year = int(input("Enter year number: "))
    if year % 400 == 0:
        print("Leap year")
    elif year % 100 == 0:
        print("Not a leap year")
    elif year % 4 == 0:
        print("Leap year")
    else:
        print("Not a leap year")


# # # # # # # # 

# תרגיל 21

def monthly_salary():
    base_pay = 50
    regular = 182.0
    extra = 0.0
    hours = float(input("Enter hours"))
    total = hours * base_pay
    if hours > regular:
        extra = hours - regular
    total += extra * (base_pay * 0.25)
    if extra > 2.0:
        total += (extra - 2.0) * (base_pay * 0.25)
    print(total)


# # # # # # # # 

# פרוייקט יישומי

def refund_eligiblity():
    age = int(input("Enter age: "))
    total = float(input("Enter sale total: "))
    has_membership = bool(int(input("Has Membership? [0 - False ; 1 - True] ")))
    is_open = bool(int(input("Is open? [0 - False ; 1 - True] ")))
    has_recipt = bool(int(input("Has Recipt? [0 - False ; 1 - True] ")))
    days_from_purchase = int(input("Enter number of days since purchase: "))
    validations = 0
    if total <= 0:
        print("total must be positive")
    else:
        validations += 1
    if not has_recipt:
        print("must have a recipt")
    else:
        validations += 1
    if is_open:
        print("cant return open product")
    else:
        validations += 1
    if not ((days_from_purchase <= 14) or (has_membership and (days_from_purchase <= 30))):
        print("too late to return")
    else:
        validations += 1
    if validations == 4:
        print("can return")

