# תרגיל 1

num1 = 25
num2 = 7

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)


# # # # # # # # # #


# תרגיל 2

balance = 1000
print(balance)
balance += 250
print(balance)
balance -= 100
print(balance)
balance *= 2
print(balance)
balance /= 4
print(balance)


# # # # # # # # # #

# תרגיל 3

base_price = float(input("Enter item price: "))
discount_percentage = float(input("Enter discount percentage: "))
print(base_price)
print(base_price * (discount_percentage / 100))
print(base_price * (1 - (discount_percentage / 100)))


# # # # # # # # # #

# תרגיל 4

current_balance = int(input("Enter current balance: "))
interest_rate = float(input("Enter yearly interest rate: "))
yearly_interest = current_balance * (1 - (interest_rate / 100))
with_interest = current_balance + yearly_interest


# # # # # # # # # #

# תרגיל 5

grade_1 = float(input("Enter grade:"))
grade_2 = float(input("Enter grade:"))
grade_3 = float(input("Enter grade:"))

average = (grade_1 + grade_2 + grade_3) / 3
print(average)


# # # # # # # # # #

# תרגיל 6

first_name = "David"
last_name = "Cohen"
city = "Tel Aviv"

print("Hello, my name is " + first_name + " " + last_name + " and I live in " + city + ".")
print(f"Hello, my name is {first_name} {last_name} and I live in {city}.")


# # # # # # # # # # 


# תרגיל 7

full_name = input("Enter your full name: ")
print(full_name)
print(len(full_name))
print(full_name.upper())
print(full_name.lower())


# # # # # # # # # # 

# תרגיל 8

sentence = input("Type a sentence: ")
print(sentence.upper())
print(sentence.lower())
print(sentence.capitalize())
print(sentence.title())


# # # # # # # # # # #

# תרגיל 9

some_name = input("Enter a name: ")
clean_name = some_name.strip()
print(some_name)
print(clean_name)
print(len(some_name))
print(len(clean_name))


# # # # # # # # # # # 

# תרגיל 10

sentence = "I love Java programming"
new_sentence = sentence.replace("Java", "Python")
print(sentence)
print(new_sentence)
print(sentence.count("love"))
print(sentence.startswith("I"))
print(sentence.endswith("programming"))


# # # # # # # # # # # 

# תרגיל 11

word = "Programming"
print(word[0])
print(word[-1])
print(word[2])
print(word[:3])
print(word[-4:])
print(word[::-1])


# # # # # # # # # # # # #

# המרות טיפוסי נתונים  #

# # # # # # # # # # # # #

# תרגיל 12

a = "100"
b = "25"
c = 10
d = 5.5

a_new = int(a)
b_new = float(b)
c_new = str(c)
d_new = int(d)


# # # # # # # # # 

# תרגיל 13

age = input("Enter your age: ")
try:
    print(age + 10)
except:
    print("can't add integer to string")

print(int(age) + 10)


# # # # # # # # # 

# תרגיל 14

price_without_VAT = float(input("Enter price before VAT: "))
total_price = price_without_VAT * (1 + 0.18)
print(total_price)


# # # # # # # # #

# חלק ד' - תרגילים משולבים

# # # # # # # # #


# תרגיל 15

user_first_name = input("Enter first name: ")
user_last_name = input("Enter last name: ")
user_age = float(input("Enter age: "))
monthly_pay = int(input("Enter monthly pay: "))
seniority = int(input("Enter seniority: "))

print("======== EMPLOYEE INFO ========")
print(f"Employee name: {user_first_name, user_last_name}")
print(f"Age: {user_age}")
print(f"Monthly pay: {monthly_pay}")
print(f"Seniority: {seniority}")

print(f"Anual salary: {monthly_pay * 12}")
print(f"Anual salary with bonus: {(monthly_pay * 12) * (1 + 0.05)}")
print(len(user_first_name) + len(user_last_name))


# # # # # # # # #

# תרגיל 16

usd_rate = 3.25
nis = float(input("Enter amount: "))
print(f"Dollars: {nis / usd_rate}")
print(f"Euros: {nis / 3.75}")
print(f"With 2% fee: \nDollars: {(nis / usd_rate) * (1 - 0.02)}\nEuros: {(nis / 3.75) * (1 - 0.02)}")


# # # # # # # # #

# תרגיל 17

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
birth_year = int(input("Enter year of birth: "))

print(f"{first_name.lower()}.{last_name.lower()}.{birth_year}@gmail.com")


# # # # # # # # # # # # #

# חלק ה' - משימת סיכום

# # # # # # # # # # # # #

customer_name = input("Enter customer name: ")
product_name = input("Enter product name: ")
product_price = float(input("Enter product price: "))
quantity = int(input("Enter quantity: "))
discount_percentage = float(input("Enter discount percentage: "))
VAT = float(input("Enter VAT rate: "))
subtotal = product_price * quantity
discount = subtotal * (1 - (discount_percentage))
VAT_amount = (subtotal - discount) * (VAT / 100)

print(
"""
================================
          PURCHASE INVOICE
================================

"""
)

print(f"Customer: {customer_name}")
print(f"Product: {product_name}\n")

print(f"Unit Price: {product_price}")
print(f"Quantity: {quantity}\n")

print(f"Subtotal: {subtotal}")
print(f"Discount: {discount}")
print(f"After Discount: {subtotal - discount}\n")

print(f"VAT: {VAT}%")
print(f"VAT Amount: {VAT_amount}\n")

print(f"TOTAL: {subtotal - discount + VAT_amount}")
print(
"""
================================
       THANK YOU FOR SHOPPING
================================
"""
)