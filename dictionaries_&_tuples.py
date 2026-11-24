# תרגיל 1

numbers = 10, 20, 30, 40, 50
print(numbers)
print(numbers[0], numbers[-1])
print(len(numbers))
print(numbers[2])

# # # # # # # # 

# תרגיל 2

names = "Chaim", "Pini", "Dani", "Moshe", "Nethanel"
for name in names:
    print(name)

user = input("Enter name: ")
print("exist" if user in names else "Not Found")

# # # # # # # # 

# תרגיל 3

numbers = 10, 20, 30, 40, 50

print(numbers[:3])
print(numbers[-3:])
print(numbers[::-1])

# # # # # # # #

# תרגיל 4

product = "milk", 5.5, 30, "dairy"

# תרגיל 5

print(product[0])
print(product[1])
print(product[2])
print(product[3])

# # # # # # # # 

# תרגיל 6

numbers = 10, 20, 30, 40, 50
total = 0
max = numbers[0]
even_counter = 0
for number in numbers:
    total += number
    if number > max:
        max = number
    if number % 2 == 0:
        even_counter += 1

# # # # # # # # 

# תרגיל 7

products = ("Laptop", "Mouse", "Keyboard", "Screen", "Printer")
first = products[:3]
last = products[-2:]
new = first + last
print(new)

# # # # # # # # 

# Dictionaries

# תרגיל 8

car = {"brand": "Toyota", "model": "Corolla", "year": 2006, "price": 8000}
car["price"] = 7500
car["year"] = 2007
car["color"] = "gray"
print(car)

# # # # # # # # 

# תרגיל 9

salaries = {
    "David": 12000,
    "Moshe": 15000,
    "Dana": 13500
    }
for employee in salaries:
    print(salaries[employee])
salaries["Dani"] = 10000
print(salaries)

# # # # # # # # 

# תרגיל 10

products = {
    "Laptop": 3000,
    "Mouse": 50,
    "Keyboard": 60,
    "Screen": 950,
    "Printer": 600
    }
user = input("Enter product name: ")
if user in products:
    print(products["user"])
else:
    print("Not Found")

# # # # # # # #

# תרגיל 11

students = {
    "Chaim": 80,
    "Pini": 90,
    "Dani": 35,
    "Moshe": 100,
    "Nethanel": 50
    }
for student, grade in students.items():
    print(f"Student: {student.title()} | Grade: {grade}\n")

# # # # # # # # 

# תרגיל 12

grades = {
    "David": 90,
    "Moshe": 75,
    "Dana": 100,
    "Noa": 55,
    "Avi": 82
    }
total = 0
count = 0

for s, g in grades.items():
    total += g
    count += 1
    failed = 0
    max = None
    if g >= 80:
        print(s)
    if (max is None) or (g > max[1]):
        max = s, g
    if g < 60:
        failed += 1

# # # # # # # # 

# תרגיל 13

products = {
    "Laptop": 3000,
    "Mouse": 50,
    "Keyboard": 60,
    "Screen": 950,
    "Printer": 600
    }
user = input("Enter product name: ")
price = int(input("Enter new price: "))
products[user] = price
for product, price in products.items():
    print(f"Product: {product} | Price: {price}")

# # # # # # # # #

# תרגיל 14
max = None
students = [
    {"name": "David", "age": 20, "grade": 90},
    {"name": "Moshe", "age": 22, "grade": 75},
    {"name": "Dana", "age": 21, "grade": 100},
    {"name": "Noa", "age": 19, "grade": 55},
    {"name": "Avi", "age": 23, "grade": 82}
    ]
total = 0
count = 0
for s in students:
    print(s["name"])
    print(s["grade"])
    total += s["grade"]
    count += 1
    if (max is None) or (s["grade"] > max):
        max = s

for s in students:
    if s["grade"] >= 80:
        print(s)

print(total / count)
print(max)

# תרגיל 15
new = {"name": "Chaim", "age": 22, "grade": 75}
students.append(new)
students[3]["grade"] = 83
for s in students.copy():
    if s["name"] == "David":
        students.remove(s)
print(students)

# # # # # # # # 

# תרגיל 16

classroom = {
    "Class A": ["David", "Moshe", "Dana"],
    "Class B": ["Noa", "Avi", "Michael"],
    "Class C": ["Daniel", "Shir", "Yossi"]
    }

for c in classroom:
    print(c)
for s in classroom["Class A"]:
    print(s)

classroom["Class B"].append("Koby")
classroom["Class B"].pop()
for c, students in classroom.items():
    print(f"{c}: {len(students)}")

# # # # # # # # 

# תרגיל 17

products = {
        "Laptop": {"price": 4500, "stock": 10},
        "Mouse": {"price": 80, "stock": 50},
        "Keyboard": {"price": 150, "stock": 20}
        }
for product in products:
    print(product["price"])
    price(product["stock"])

products["Laptop"]["stock"] = 15
products["Printer"] = {"price": 950, "stock": 7}
for p in products:
    if p["price"] > 100:
        print(p)


# # # # # # # # #

# תרגיל 18

employees = [
        ("David", "Development", 15000),
        ("Moshe", "Marketing", 12000),
        ("Dana", "Development", 18000),
        ("Noa", "HR", 11000)
        ]
max = None
total = 0
count = 0
for e in employees:
    count += 1
    total += e[2]
    print(e[0])
    if (max is None) or (e[3] > max):
        max = e

for e in employees:
    if e[1] == "Development":
        print(e[0])

print(max)
print(total / count)

# # # # # # # # 

# תרגיל 19

inventory = {
    "Laptop": 10,
    "Mouse": 50,
    "Keyboard": 20
    }
product = input("Enter product name: ")
quantity = int(input("Enter quantity: "))
if product in inventory:
    if quantity <=  inventory[product]:
        inventory[product] -= quantity
        print(inventory[product])
    else:
        print("Not enough in stock")
else:
    print("Product doesnt exist")

# # # # # # # # #

# תרגיל 20

votes = {
    "David": 0,
    "Moshe": 0,
    "Dana": 0
    }
running = True
while running:
    name = input("Enter name: ").title()
    if name == "Stop":
        running = False
        continue
    elif name in votes:
        votes[name] += 1
    else:
        print("Invalid choice")

print(votes)
max = None
for candidate, vote in votes.items():
    if (max is None) or (vote > max[1]):
        max = candidate, vote

print(max)

# # # # # # # # 

# תרגיל 21

contacts = {
    "Eli": "053456789",
    "Chaim": "0545698786",
    "Tzvika": "0574859635"
}
running = True
while running:
    print(
"""
1. Add contact
2. Search contact
3. Update contact
4. Delete contact
5. Show all contacts
6. Exit

"""
)
    choice = input("Choose option: ")
    if choice == "1":
        name = input("Enter name: ").title()
        phone = input("Enter phone number: ")
        contacts[name] = phone
    elif choice == "2":
        name = input("Enter name: ").title()
        result = contacts.get(name)
        if result is None:
            print("Not Found")
        else:
            print(contacts[result])
    elif choice == "3":
        name = input("Enter name: ").title()
        result = contacts.get(name)
        if result is None:
            print("Not Found")
        else:
            phone = input("Enter phone number: ")
            contacts[name] = phone
    elif choice == "4":
        name = input("Enter name: ").title()
        result = contacts.get(name)
        if result is None:
            print("Not Found")
        else:
            contacts.pop(result)
    elif choice == "5":
        for c, p in contacts.items():
            print(f"{c}: {p}")
    elif choice == "6":
        running = False
    else:
        print("Invalid choice")

# # # # # # # # #

# פרוייקט מסכם - ניהול חנות

products = [
    {"name": "Laptop", "price": 4500, "stock": 10},
    {"name": "Mouse", "price": 80, "stock": 50},
    {"name": "Keyboard", "price": 150, "stock": 20},
    {"name": "Screen", "price": 900, "stock": 15}
    ]

running = True
while running:
    print(
"""
===== Store Management =====

1. Show all products
2. Add product
3. Search product
4. Update product price
5. Update product stock
6. Sell product
7. Show products by price
8. Show products with low stock
9. Show total inventory value
0. Exit

"""
)
    choice = input("Choose option: ")
    if choice == "1":
        for p in products:
            print(f"Name: {p["name"]} | Price: {p["stock"]} | Stock: {p["stock"]}")
    elif choice == "2":
        new_product = {"name": input("Enter name: "), "price": int(input("Enter price: ")), "stock": int(input("Enterquantity in stock: "))}
        products.append(new_product)
    elif choice == "3":
        user = input("Enter name for search: ")
        result = [p for p in products if p == user]
        if not result:
            print("Not Found")
        else:
            for p in result:
                print(f"Name: {p["name"]} | Price: {p["stock"]} | Stock: {p["stock"]}")
    elif choice == "4":
        user = input("Enter name for search: ")
        result = None
        for p in products:
            if p == user:
                result = p
                break
        if result is None:
            print("Not Found")
        else:
            result["price"] = int(input("Enter price: "))
    elif choice == "5":
        user = input("Enter name for search: ")
        result = None
        for p in products:
            if p == user:
                result = p
                break
        if result is None:
            print("Not Found")
        else:
            result["stock"] = int(input("Enter new quantity in stock: "))
    elif choice == "6":
        user = input("Enter name for search: ")
        result = None
        for p in products:
            if p == user:
                result = p
                break
        if result is None:
            print("Not Found")
        else:
            quantity = int(input("Enter quantity: "))
            if quantity > result["stock"]:
                price("Not Enough in stock")
            else:
                result["stock"] -= quantity
    elif choice == "7":
        price = int(input("Enter price: "))
        for p in products:
            if p["price"] >= price:
                print(f"Name: {p["name"]} | Price: {p["stock"]} | Stock: {p["stock"]}")
    elif choice == "8":
        # for p in products:
        #     if p["stock"] < 10:
        print(f"Name: {p["name"]} | Price: {p["stock"]} | Stock: {p["stock"]}" for p in products if p["stock"] < 10)
    elif choice == "9":
        total = 0
        for p in products:
            total += p["price"] * p["stock"]
        print("Total:", total)
    elif choice == "0":
        running = False
    else:
        print("Invalid choice")

