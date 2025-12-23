# functions
# def greet():
#     print("Hello")

# greet()

# functions with input (parameters)

# def greet(name):
#     print("Hello", name)

# greet("John")
# greet("Alice")

# functions with multiple parameters

# def greet(first_name, last_name):
#     print("Hello", first_name, last_name)

# greet("John", "Doe")

# functions with default parameters

# def greet(first_name, last_name="Doe"):
#     print("Hello", first_name, last_name)

# greet("John")
# greet("John", "Doe")

# functions with return values

# def add(a, b):
#     return a + b

# result = add(3, 5)
# print(result)

# functions with variable number of arguments

# def add(*args):
#     return sum(args)

# result = add(1, 2, 3, 4)
# print(result)

# function + if logic

# def check_price(price):
#     if price > 1000:
#         return "Expensive"
#     else:
#         return "Cheap"

# print(check_price(1500))
# print(check_price(500))

# function + loop

# def print_pass_marks(marks):
#     for mark in marks:
#         if mark >= 50:
#             print(mark, "pass")
#         else:
#             print(mark, "fail")

# scores = [45, 78, 32, 90, 60]
# print_pass_marks(scores)

# function + dictionary
# def print_student_info(student):
#     for key, value in student.items():
#         print(key, ":", value)

# student = {
#     "name": "John",
#     "age": 25,
#     "grade": "A"
# }
# print_student_info(student)

# # practice 1
# def square(number):
#     return number * number

# print(square(5))
# print(square(10))    

# # practice 2
# def max_num(num1, num2, num3):
#     if num1 >= num2 and num1 >= num3:
#         return num1
#     elif num2 >= num1 and num2 >= num3:
#         return num2
#     else:
#         return num3

# print(max_num(10, 20, 30))
# print(max_num(30, 20, 10))
# print(max_num(20, 30, 10))    

# practice 3
# def is_adult(age):
#     if age >= 18:
#         return True
#     else:
#         return False

# print(is_adult(20))
# print(is_adult(15))

# def total_sales(sales):
#     return sum(sales)

# print(total_sales([100, 200, 300]))    

# Mini project : Simple Business Sales Analysis

# sales_data = [
#     {"day": "Monday", "sales": 1200},
#     {"day": "Tuesday", "sales": 800},
#     {"day": "Wednesday", "sales": 1500},
#     {"day": "Thursday", "sales": 600},
#     {"day": "Friday", "sales": 2000},
#     {"day": "Saturday", "sales": 1800},
#     {"day": "Sunday", "sales": 1600},
#     ]
# # calculate total weekly sales
# total = 0

# for record in sales_data:
#     total += record["sales"]

# print("Total weekly sales:", total)

# # find highest sales day

# for record in sales_data:
#     if record["sales"] >= 1500:
#         print(record["day"], "was a high sales day")

# # Classify each day (perfomance)

# for record in sales_data:
#     if record["sales"] >= 1500:
#         status = "Excellent"
#     elif record["sales"] >= 1000:
#         status = "Good"
#     else:
#         status = "poor"
#     print(record["day"], ":", status)

# # use a function 
# def classify_sales(amount):
#     if amount >= 1500:
#         return "Excellent"
#     elif amount >= 1000:
#         return "Good"
#     else:
#         return "poor"

# for record in sales_data:
#     result = classify_sales(record["sales"])
#     print(record["day"], ":", result)

# import calendar

# year = int(input("Enter a year: ")) 
# month = int(input("Enter a month: "))
 
# cal = calendar.month(year, month)
# print(cal)

customers = [
    {"name": "Alice" , "total_spent": 45000, "visits": 12},
    {"name": "Bob" , "total_spent": 8000, "visits": 3},
    {"name": "Chris" , "total_spent": 22000, "visits": 8},
    {"name": "Diana" , "total_spent": 60000, "visits": 3},
    {"name": "Evan" , "total_spent": 12000, "visits": 4}
]

# Identifying High-value customers
# high-value = total_spent > 30000

# for customer in customers:
#     if customer["total_spent"] > 30000:
#         print(customer["name"] , "is a high-value customer")

# #Customer segmentation
# def segment_customer(amount):
#     if amount >= 50000:
#         return "VIP"
#     elif amount >= 20000:
#         return "Regular"
#     else:
#         return "Low-value" 

# for customer in customers:
#     result = segment_customer(customer["total_spent"])
#     print(customer["name"] , ":" , result)

# Marketing descision Logic

for customer in customers:
    if  customer["visits"] >=10:
        status = "loyal customer"
    else:
        status = "Needs engament"

    print(customer["name"] , ":" , status)    