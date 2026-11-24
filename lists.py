# תרגיל 1

numbers = [10, 20, 30, 40, 50]

print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[2])


# # # # # # # # 

# תרגיל 2

students = ["Chaim", "Moshe", "Shlomo", "Yosef"]

print(len(students))
print(students[0], students[-1])
students[1] = "Shmuel"
print(students)


# # # # # # # #

# תרגיל 3

grades = [78, 95, 80, 86, 60]

grades.append(84)
grades.insert(0, 82)
grades[2] = 50
print(grades)


# # # # # # # #

# תרגיל 4

numbers2 = [54, 62, 18, 95, 42, 62, 3, 15, 48, 4]

print(numbers2)
numbers2.pop(0)
print(numbers2)
numbers2.pop()
print(numbers2)
numbers2.pop(3)
print(numbers2)


# # # # # # # #

# תרגיל 5

items = ["milk", "eggs", "meat", "potatoes"]

if "milk" in items:
    print("milk in items list")
if "chicken" not in items:
    print("chicken is not in items list")


# # # # # # # # 

# תרגיל 6

numbers3 = [15, 48, 65, 48, 65, 15, 32, 29, 78, 49]

for number in numbers3:
    print(number)

# תרגיל 7

for number in numbers3:
    if number % 2 == 0:
        print(number)


# # # # # # # # #


# תרגיל 8

grades2 = [15, 26, 15, 48, 95, 39]

total = 0
for grade in grades:
    total += grade
print(total)

# # # # # # # # 

# תרגיל 9

numbers4 = [45, 65, 95, 78, 45, 5]

max = numbers4[0]
for number in numbers4:
    if number > max:
        max = number
print(max)

# # # # # # # # 

# תרגיל 10

names = ["Chaim", "Moshe", "Tzvi", "Yaakov"]

user = input("Enter a name: ")
result = "Not Found"
for name in names:
    if user == name:
        result = "Found"
print(result)

# # # # # # # # 

# תרגיל 11

numbers5 = [51, 6, 5, 98 ,87 ,54 ,78]

user = int(input("Enter a number: "))
for i, number in enumerate(numbers5):
    if user == number:
        print(i)

# # # # # # # # # 

# תרגיל 12

numbers6 = [51, 65, 95, 84, 74, 85]

count = 0
for number in numbers6:
    if number > 50:
        count += 1

# # # # # # # # #

# תרגיל 13

numbers7 = [54, 95, 65, 7, 78, 15, 49, 46, 84, 74]

evens = []
for number in numbers7:
    if number % 2 == 0:
        evens.append(number)

# # # # # # # # #

# תרגיל 14

names = ["Chaim", "Moshe", "Tzvi", "Yaakov"]

index = 0
while i < len(names):
    print(f"{i}: {names[i]}")
    i += 1

# # # # # # # # #

# תרגיל 15

numbers7 = [54, 95, 65, 7, 78, 15, 49, 46, 84, 74]

print(numbers7[:3])
print(numbers7[-3:])
print(numbers7[2:6])
print(numbers7[::-1])

# # # # # # # # # 

# תרגיל 16

names = ["Chaim", "Moshe", "Tzvi", "Yaakov", "Zeev", "Neria", "Nissim", "Nethanel", "Avraham", "Yehuda"]

print(names[::2])
print(names[1::2])
print(names[::-2])

# # # # # # # # #

# תרגיל 17

numbers8 = [51, 62, 84, 95, 45, 78, 98, 65, 32, 15, 15, 59, 48, 26, 78, 49, 54, 75, 65, 94]

first_numbers = numbers8[:10]
last_numbers = numbers8[10:]
select = numbers8[5:15]

# # # # # # # # #

# תרגיל 18

numbers8 = [51, 62, 84, 95, 45, 78, 98, 65, 32, 15, 15, 59, 48, 26, 78, 49, 54, 75, 65, 94]

half = len(numbers8) // 2
first = numbers8[:half]
last = numbers8[half:]

# # # # # # # # # 

# תרגיל 19

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

double = [n * 2 for n in numbers]
square = [n * n for n in numbers]
even = [n for n in numbers if n % 2 == 0]
large = [n for n in numbers if n > 5]

# # # # # # # # #

# תרגיל 20

grades = [55, 90, 67, 100, 45, 82, 73, 30]

passed = [grade for grade in grades if grade > 60]
failed = [grade for grade in grades if grade < 60]
added = [grade + 5 for grade in grades]

# # # # # # # # #

# תרגיל 21

names = ["Moshe", "David", "Dana", "Noa", "Michael", "Avi"]

long = [name for name in names if len(name) > 4]
capital = [name.upper() for name in names]
D_names = [name for name in names if name.startswith("D")]

# # # # # # # # #

# תרגיל 22

numbers = [12, 7, 25, 30, 9, 44, 18, 3]
new = [number for number in numbers if (number > 10) and (number % 3 == 0)]

# # # # # # # # #

# 23
numbers = []
for _ in range(10):
    numbers.append(int(input("Enter a number: ")))

print(number for number in numbers)

max = numbers[0]
min = numbers[0]
total = 0
count = 0
for number in numbers:
    total += number
    count += 1
    if number > max:
        max = number
    elif number < min:
        min = number
print(f"Max: {max}")
print(f"Min: {min}")
print(f"Average: {total / count}")

# # # # # # # # #

# תרגיל 24

names = ["Moshe", "David", "Dana", "Noa", "Michael"]
user = input("Enter a name: ")
if user in names:
    names.remove(user)
else:
    print("Not Found")

print(names)

# # # # # # # # # 

# תרגיל 25

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = [number for number in numbers if number % 2 == 0]
odd = [number for number in numbers if number % 2 == 1]
larg = [number for number in numbers if number > 20]

# # # # # # # # #

# תרגיל 26

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
number = int(input("Enter a number: "))

indexes = [i for i in range(len(numbers)) if numbers[i] == number]
print(len(indexes) if indexes else "Not Found")

# # # # # # # # #

# תרגיל 27

numbers_A = [156, 654 ,95]
numbers_B = [54, 65, 95, 45]
numbers_A_B = numbers_A + numbers_B
print(numbers_A_B)
print(numbers_A_B[:5])
print(numbers_A_B[-5:])
print(numbers_A_B[::-1])


# # # # # # # # # # # 

# תרגיל 28

numbers = [54, 65, 95, 45]
user = int(input("Enter a number: "))
exists = False
for num in numbers:
    if num == user:
        exists = True
        break
if not exists:
    numbers.append(user)

print(numbers)

# # # # # # # # # #

# פרוייקט מסכם - ניהול ציונים

grades = [85, 72, 90, 55, 100, 63, 48, 77]

running = True
while running:

    print(
"""
===== Grades Management =====

1. Show all grades
2. Add a grade
3. Search for a grade
4. Remove a grade
5. Show passing grades
6. Show failing grades
7. Show highest and lowest grade
8. Show average grade
9. Show first 3 grades
10. Show grades in reverse
0. Exit

"""
)


    choice = input("Choose an option: ")
    if choice == "1":
        for grade in grades:
            print(grade)
    elif choice == "2":
        grade = int(input("Enter a grade: "))
        grades.append(grade)
    elif choice == "3":
        grade = int(input("Enter a grade for search: "))
        indexes = []
        for i, g in enumerate(grades):
            if g == grade:
                indexes.append(i)
        if not indexes:
            print("Not Found")
        else:
            print(indexes)
    elif choice == "4":
        grade = int(input("Enter a grade for search: "))
        if grade in grades:
            grades.remove(grade)
    elif choice == "5":
        print([grade for grade in grades if grade > 60])
    elif choice == "6":
        print([grade for grade in grades if grade < 60])
    elif choice == "7":
        max = grades[0]
        min = grades[0]
        for grade in grades:
            if grade > max:
                max = grade
            elif grade < min:
                min = grade
        print(max, min)
    elif choice == "8":
        count = 0
        total = 0
        for grade in grades:
            count += 1
            total += grade
        print(total / grade)
    elif choice == "9":
        print(grades[:3])
    elif choice == "10":
        print(grades[::-1])
    elif choice == "0":
        running = False


# # # # # # # # # # # 