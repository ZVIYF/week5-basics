#  תרגיל 1

def exercise_1():
    index = 0
    while index < 10:
        index += 1
        print(index)

# # # # # # # # 

# תרגיל 2

def exercise_2():
    index = 10
    while index > 0:
        print(index)
        index -= 1
    print("START!")

# # # # # # # # 

# תרגיל 3

def exercise_3():
    index = 0
    while index <= 50:
        index += 1
        if index % 2 == 0:
            print(index)

# # # # # # #

# תרגיל 4

def exercise_4():
    number = int(input("Enter a number: "))
    index = 1
    while index <= 5:
        print(number * index)
        index += 1

# # # # # # # #

# תרגיל 5

def exercise_5():
    total = 0
    index = 0
    while index <= 100:
        total += index
    print(total)


# # # # # # # # 

# תרגיל 6

def exercise_6():
    password = "Python123"
    valid_password = False
    while not valid_password:
        user_input = input("Enter password: ")
        if user_input == password:
            valid_password = True
    print("Welcome!")

# # # # # # # #

# תרגיל 7

def exercise_7():
    secret_number = 27
    user_is_correct = False
    while not user_is_correct:
        guess = int(input("Enter your guess: "))
        if guess == secret_number:
            user_is_correct = True
    print("Success!")


# # # # # # # # # #

# תרגיל 8

def exercise_8():
    total = 0
    input_is_0 = False
    while not input_is_0:
        number = int(input("Enter a number: "))
        if number == 0:
            input_is_0 = True
        total += number
    print(total)


# # # # # # # # #

# תרגיל 9

def exercise_9():
    total = 0
    counter = 0
    running = True
    while running:
        number = int(input("Enter a number: "))
        if number == 999:
            running = False
            continue
        total += number
        counter += 1
    print("sum of grades:", total)
    print("number of grades:", counter)
    print("Average of all grades:", total / counter)


# # # # # # # # #

# תרגיל 10

def exercise_10():
    total = 0
    count = 0
    is_negativ_number = False
    while not is_negativ_number:
        number = int(input("Enter a number: "))
        if number < 0:
            is_negativ_number = True
            continue
        total += number
        count += 1
    print("Total:", total)
    print("count", count)

# # # # # # # # 

# תרגיל 11

def multyplication():
    number = int(input("Enter a number: "))
    index = 0
    while index < 10:
        index += 1
        print(number, "X", index, "=", number * index)


# # # # # # # # # # 

# תרגיל 12

def count_digids():
    number = int(input("Enter a number: "))
    print("Input:", number)
    counter = 0
    while number > 0:
        number //= 10
        counter += 1
    print("Output:", counter, "digits")


# # # # # # # # 

# תרגיל 13

def reverse_digits():
    number = int(input("Enter a number: "))
    print("Input:", number)
    reversed = 0
    while number > 0:
        temp = number % 10
        number //= 10
        reversed *= 10
        reversed += temp
    print("Output:", reversed)


# # # # # # # # 

# תרגיל 14

def check_if_prime():
    number = int(input("Enter a number: "))
    square_root = int(number ** 1/2) + 1
    i = 2
    is_prime = True
    while (i <= square_root) and is_prime:
        if number % i == 0:
            is_prime = False
            continue
        i += 1
    print("Result:", number, "is prime:", is_prime)


# # # # # # # # 

# תרגיל 15

def ATM_system():
    balance = 5000
    running = True
    while running:
        choice = input("MENU:\n1. check balance\n2. deposit\n3. withdraw\n4. Exit\n")
        if choice == "1":
            print(balance)
        elif choice == "2":
            amount = int(input("Amount to deposit: "))
            if amount < 0:
                print("amount must be positive")
                continue
            else:
                balance += amount
        elif choice == "3":
            amount = int(input("Amount to withdraw: "))
            if amount < 0:
                print("amount must be positive")
                continue
            elif amount > balance:
                print("amout is bigger then balance")
                continue
            else:
                balance -= amount
        elif choice == "4":
            running = False
        else:
            print("Invalid choice")


# # # # # # # # 

# תרגיל 16

def exercise_16():
    index = 1
    while True:
        if index == 15:
            break
        print(index)
        index += 1


# # # # # # # # #

# תרגיל 17

def exercise_17():
    index = 0
    while index <= 30:
        index += 1
        if index % 3 == 0:
            continue
        print(index)


# # # # # # # # 

# תרגיל 18

def exercise_18():
    while True:
        number = int(input("Enter a number: "))
        if number == 100:
            print("Success!")
            break

# # # # # # # # #

# תרגיל 19

def exercise_19():
    for i in range(20):
        print(i + 1)

# # # # # # # # # 

# תרגיל 20

def exercise_20():
    for i in range(0, 100, 5):
        print(i)
    else:
        print(i + 5)


# # # # # # # # # 

# תרגיל 21

def exercise_21():
    total = 0
    for i in range(101):
        total += i


# # # # # # # # # 

# תרגיל 22

def exercise_22():
    number = int(input("Enter a number: "))    
    for i in range(1, 11):
        print(number * i)

# # # # # # # # #

# תרגיל 23

def exercise_23():
    number1 = int(input("Enter a low number: "))    
    number2 = int(input("Enter a higher number: "))    
    print("Start:", number1)
    print("End:", number2)
    total = 0    
    for i in range(number1, number2 + 1):
        total += i
    print("Result:", total)


# # # # # # # # #

# תרגיל 24

def exercise_24():
    for i in range(1, 100):
        if (i % 3 == 0) and (i % 5 == 0):
            print(i)


# # # # # # # # #

# תרגיל 25

def exercise_25():
    rows = int(input("Enter number of rows: "))    
    columns = int(input("Enter number of columns: "))    
    for i in range(rows):
        print("*" * columns)


# # # # # # # # #

# תרגיל 26

def exercise_26():
    for i in range(1, 7):
        for j in range(i):
            print("*", end="")
        print()


# # # # # # # # 

# תרגיל 27

def exercise_27():
    for i in range(1, 11):
        for j in range(1, 11):
            print(str(i * j).ljust(2), end=" ")
        print()

# # # # # # # # 

# תרגיל 28

def exercise_28():
    for i in range(1, 6):
        for j in range(1, 6):
            print(i, j)


# # # # # # # # # 

# פרוייקט יישומי - משחק טריוויה 

def trivia_game():
    questions = [
        ("5 X 2 = ", "10"),
        ("9 / 3 = ", "3"),
        ("6 + 7 = ", "13"),
        ("8 X 3 = ", "24"),
        ("24 / 6 = ", "4"),
        ("99 - 55 = ", "44"),
        ("150 / 30 = ", "5"),
        ("70 X 2 = ", "140"), 
        ("15 X 3 = ", "45"),
        ("45 X 2 = ", "90")
        ]    
    
    running = True
    while running:
        print(
"""
===== MATH GAME =====

1. Start Game
2. View Instructions
3. Exit

"""
)
        choice = input("Choose: ")
        if choice == "1":
            score = 0
            for q, a in questions:
                ansure = input(q)
                if ansure == a:
                    score += 1
            print("Score:", score, "out of 10")

        elif choice == "2":
            print("When choosing a game:")
            print("The program will show 10 math questions.")
            print("In each one the user will type his ansuer.")
            print("The program will check the ansuers.")
            print("for every correct ansuer the user will get one point.")
            print("In the end the program will display the results.")

        elif choice == "3":
            running = False

        else:
            print("Invalid Choice")

