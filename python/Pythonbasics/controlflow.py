# if statement
# age = 16
# if age >=18:
#     print("You are an adult")
# else:
#     print("You are a minor")

# marks =75

# if marks >= 80:
#     print("Grade A")
# elif marks >= 60:
#  print("Grade B")
# else:
#  print("Grade C")

# age = 22
# is_student = True

# if age >=18 and is_student:
#     print("You are an adult student")
# elif age >=18 and not is_student:
#     print("You are an adult")
# else:
#     print("You are a minor")

# password = "admin123"

# if password == "admin123":
#     print("Access granted")
# else:
#     print("Access denied")

# numbers = [10,20,30]

# for num in numbers:
#     print(num)

# word = "Date"

# for letter in word:
#     print(letter)

# products = ["Apple", "Banana", "Cherry"]

# for product in products:
#     print(product)

student = {
    "name": "John",
    "age": 25,
    "grade": "A"
}

# # for key in student:
# #     print(key)

# for value in student.values():
#     print(value)

# for key, value in student.items():
#     print(key, ":", value)

# for i in range(5):
#     print(i)

# for i in range(2, 10):
#     print(i)

# for i in range(2, 10, 2):
#     print(i)

# names = ["Alice", "Bob", "Charlie"]
# for name in names:
#     print("Hello", name)

# count =1

# while count <= 5:
#     print(count)
#     count += 1

# for i in range(1,6):
#     print(i * 2)

# x = 3

# while x > 0:
#     print(x)
#     x -= 1

# numbers = [10,25,40,55,60]

# for num in numbers:
#     if num > 30:
#         print(num)

# marks = [45 , 78 , 32, 90, 60]

# for mark in marks:
#     if mark >= 50:
#         print(mark , "pass")
#     else:
#         print(mark , "fail")

customers = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False},
    {"name": "Charlie", "active": True}
]

for customer in customers:
    if customer["active"]:
        print(customer["name"], "is active")
    else:
        print(customer["name"], "is not active")