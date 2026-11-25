# תרגיל 1

def say_hello():
    print("Hello!")

say_hello()
say_hello()
say_hello()

# # # # # # # # 

# תרגיל 2

def show_welcome():
    print("Welcome!")

# תרגיל 3

def show_menu():
    print(
"""
===== Main Menu =====
1. Start
2. Settings
3. Exit

"""
)

# תרגיל 4

def show_numbers():
    for i in range(10):
        print(i + 1)

# תרגיל 5

def show_even_numbers():
    for i in range(1, 100):
        if i % 2 == 0:
            print(i)

# תרגיל 6

def show_stars():
    for _ in range(5):
        print("**********")

# תרגיל 7

def greet(name):
    print("Hello", name)

# תרגיל 8

def show_age(age):
    print(f"You are {age} years old.")

# תרגיל 9

def calculate_sum(number_1, number_2):
    print(number_1 + number_2)

# תרגיל 10

def calculate_average(grade_A, grade_B, grade_C):
    print((grade_A + grade_B + grade_C) / 3)

# תרגיל 11

def check_even(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

# תרגיל 12

def check_password(password):
    if password == "123456":
        print("Access Granted")
    else:
        print("Access Denied")

# תרגיל 13

def calculate_discount(price, discount_percent):
    print(price * (1 - (discount_percent / 100)))

# תרגיל 14

def show_range(number_1, number_2):
    for i in range(number_1, number_2 + 1):
        print(i)

# תרגיל 15

def print_rectangle(height, width):
    for i in range(height):
        print("*" * width)

# תרגיל 16

def multiply(number_1, number_2):
    return number_1 * number_2

# תרגיל 17

def get_full_name(first_name, last_name):
    return first_name + " " + last_name

# תרגיל 18

def get_max(number_1, number_2):
    if number_1 > number_2:
        return number_1
    return number_2

# תרגיל 19

def is_positive(number):
    if number >= 0:
        return True
    return False

# תרגיל 20

def calculate_max(price, VAT):
    return price * (1 + (VAT / 100))

# תרגיל 21

def get_grade_Status(grade):
    if grade >= 90:
        return "Excelent"
    if grade >= 75:
        return "Good"
    if grade >= 60:
        return "Average"
    return "Failed"

# תרגיל 22

def count_digits(number):
    digits = 0
    while number > 0:
        digits += 1
        number //= 10
    return digits

# תרגיל 23

def calculate_power(number, power):
    total = 1
    for i in range(power):
        total *= number
    return total

# תרגיל 24

def print_list(arr):
    for item in arr:
        print(item)

# תרגיל 25

def get_list_sum(arr):
    total = 0
    for number in arr:
        total += number
    return total

# תרגיל 26

def get_list_average(arr):
    if not arr:
        return 0
    return get_list_sum(arr) / len(arr)

# תרגיל 27

def find_number(arr, number):
    for n in arr:
        if n == number:
            return True
    return False

# תרגיל 28

def find_max(arr):
    max = arr[0]
    for item in arr:
        if item > max:
            max = item
    return max

# תרגיל 29

def get_even_numbers(arr):
    return [n for n in arr if n % 2 == 0]

# תרגיל 30

def get_long_names(arr):
    return [name for name in arr if len(name) > 4]

# תרגיל 31

def reverse_list(arr):
    return arr[::-1]

# תרגיל 32

def count_occurrences(arr, number):
    counter = 0
    for n in arr:
        if n == number:
            counter += 1
    return counter

# תרגיל 33

def remove_duplicates(arr):
    new = []
    for item in arr:
        if item not in new:
            new.append(item)
    return new
    
# תרגיל 34

def calculate_final_price(price, discount_percent):
    subtotal = price * (1 - (discount_percent / 100))
    if subtotal <= 500:
        return subtotal
    return subtotal * (1 - 0.05)

# תרגיל 35

def check_list(arr):
    even = 0
    odd = 0
    count = 0
    for number in arr:
        count += 1
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd, count

# תרגיל 36

def analyze_grades(arr):
    passed = 0
    max = arr[0]
    min = arr[0]
    total = 0
    count = 0
    for grade in arr:
        count += 1
        total += grade
        if grade >= 60:
            passed += 1
        if grade > max:
            max = grade
        elif grade < min:
            min = grade
    return total / count, max, min, passed

# תרגיל 37

def valifate_user(user_name, password):
    if not user_name:
        return False
    if len(password) < 6:
        return False
    return False

# תרגיל 38
students = [
    {"name": "David", "grade": 90},
    {"name": "Moshe", "grade": 75},
    {"name": "Dana", "grade": 100}
    ]


def search_students(arr, name):
    for s in arr:
        if s["name"] == name:
            return s

# תרגיל 39

cart = [
    {"name": "Laptop", "price": 4500, "quantity": 1},
    {"name": "Mouse", "price": 80, "quantity": 2},
    {"name": "Keyboard", "price": 150, "quantity": 1}
    ]

def calculate_cart_total(cart:list[dict]):
    subtotal = 0
    for item in cart:
        subtotal += item["price"] * item["quantity"]
    return subtotal

# תרגיל 40

def get_fibonacci(number):
    sequence = [0, 1]
    if number < 2:
        return sequence[:number]
    for i in range(2, number):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

# תרגיל 41

name = "David"
def show_name():
    name = "Moshe"
print(name)

show_name()
print(name)

# תרגיל 42

counter = 10
def increase():
    counter = 20
    print(counter)
increase()
print(counter)

# המונה הוא מחוץ לטווח של הפונקציה, ןלכן היא לא יכולה לבצע השמה עליו
# רק בתוך הפונקציה עצמה המשתנה מראה את הערך שהוגדר בתוך הפונקציה
# למעט מצב שבו המשתנה עבר השמה לאחר שהוצהר כגלובלי

# תרגיל 43

number = 45

def decrease(number):
    number = number + 10
    return number

decrease(number)
print(number)

# תרגיל 44

numbers = [4, 5, 6, 7 ,8]

def add_number(arr:list, number):
    arr.append(number)

add_number(numbers, 9)
print(numbers)

#  תרגיל 45

numbers = [4, 5, 6, 7 ,8]

def add_number_to_slicing_list(arr:list, number):
    return arr[:].append(number)

print(numbers)
add_number_to_slicing_list(numbers, 9)
print(numbers)

# # # # # # # # # # # # #

# פרוייקט מסכם - ניהול תלמידים

students = [
    {"name": "David", "age": 20, "grade": 90},
    {"name": "Moshe", "age": 22, "grade": 75},
    {"name": "Dana", "age": 21, "grade": 100},
    {"name": "Noa", "age": 19, "grade": 55},
    {"name": "Avi", "age": 23, "grade": 82}
    ]

def show_menu():
    print(
"""
===== Student Management =====

1. Show all students
2. Add student
3. Search student
4. Update student grade
5. Remove student
6. Show passing students
7. Show class statistics
8. Show students above average
0. Exit

"""
)

def show_students(students):
    for s in students:
        print(f"Name: {s["name"]} | Age: {s["age"]} | Grade: {s["grade"]}")


def add_student(students:list):
    name = input("Enter name: ").title()
    age = int(input("Enter age:"))
    grade = int(input("Enter grade:"))
    students.append({"name": name, "age": age, "grade": grade})


def search_student(students, name):
    for s in students:
        if s["name"] == name:
            return s


def update_student_grade(students, name, grade):
    student = search_student(students, name)
    if not student:
        return False
    student["grade"] = grade
    return True


def remove_student(students:list, name):
    student = search_student(students, name)
    if not student:
        return False
    students.remove(student)
    return True


def get_passing_students(students:list, passing_grade = 60):
    return [s for s in students if float(s["grade"]) > passing_grade]


def get_average(students):
    if not students:
        return 0.0
    total = 0
    count = 0
    for s in students:
        count += 1
        total += s["grade"]
    return total / count


def get_highest_grade(students:list):
    max = None
    for s in students:
        if (max is None) or (s["grade"] > max):
            max = s["grade"]
    return max


def show_statistics(students):
    print("==== STATISTICS ====")
    print("Students average:", get_average(students))
    print("Highest grade:", get_highest_grade(students))


def get_name():
    return input("Enter name: ")    


def search_student_by_name():
    name = get_name()
    search_student(students, name)
    

def main_menu():
    running = True
    while running:
        show_menu()
        choice = input("Choose option: ")
        match choice:
            case "1":
                show_students(students)
            case "2":
                add_student(students)
            case "3":
                search_student_by_name()
            case "4":
                name = get_name()
                update_student_grade(students, name)
            case "5":
                name = get_name()
                remove_student(students, name)
            case "6":
                filtered = get_passing_students(students)
                show_students(filtered)
            case "7":
                show_statistics(students)
            case "8":
                average = get_average(students)
                filtered = get_passing_students(students, passing_grade=average)
                show_students(filtered)
            case "0":
                running = False
            case _:
                print("Invalid choice")

main_menu()