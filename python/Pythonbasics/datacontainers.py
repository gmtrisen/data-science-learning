# list
# couarses = ['math', 'science', 'history', 'english']

# nums = [1, 2, 3, 4, 5]
# couarses_2 = ['art', 'music']

# couarses.extend(couarses_2)
# couarses.insert(0, couarses_2)
# couarses.append('art')
# couarses.remove('history')
# couarses.pop()
# couarses.pop(0)
# couarses.sort()
#nums.sort()
# couarses.reverse()
#nums.reverse()  
# couarses.copy()
# couarses.clear()
# print(couarses)
#print(min(nums))
#print(couarses.index('english'))

# for item in couarses:
#     print(item)
# for index, couarase in enumerate(couarses):
#     print(index, couarase)

#Tuples
# tuple_1 = ('math', 'science', 'history', 'english')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

#Sets
# cs_courses = {'math', 'science', 'history', 'english', 'math'}

# # print(cs_courses)
# print('math' in cs_courses)

# cs_courses = {'math', 'science', 'history', 'english'}
# art_courses = {'art', 'design', 'history', 'english'}

# print(cs_courses.intersection(art_courses))
# print(cs_courses.difference(art_courses))
# print(cs_courses.union(art_courses))

#Dictionary
# student = {'name': 'John', 
#            'age': 25, 
#            'courses': ['math', 'science']}
# del student['age']
#print(student['name'])
#print(student.get('age'))

# print(len(student))
# print(student.keys())
# print(student.values())
# print(student.items())

# products = ["Laptop", "Phone", "Tablet"]
# prices = [80000,45000,30000]

# inventory = {
#     "Laptop":10,
#     "Phone": 20,
#     "Tablet": 15
# }
# for product in products:
#     print(products, "price:" , prices[products.index(product)])

# student_names = ['Alice', 'Bob', 'Carol' , 'David']
# student_scores = [85.5 , 92.0 , 78.5 , 88.0]
# student_info = {
#     'Alice': 85.5,
#     'Bob': 92.0,
#     'Carol': 78.5,
#     'David': 88.0
# }
# average_score = sum(student_scores) / len(student_scores)
# print("Average score:", average_score)

# highest_score = max(student_scores)
# print("Highest score:", highest_score)

# new_student = {'Eve': 90.0}
# student_info.update(new_student)
# print(student_info)

# cart_items = ["Bread","Milk","Eggs","Bread"]
# prices = [50,120,180,50]

# product_catalog = {
#     "Bread": 50,
#     "Milk": 120,
#     "Eggs": 180,

#     "Bread": 50
# }

# total_price = 0
# for item in cart_items:
#     total_price += product_catalog[item]
# print("Total price:", total_price)

# set1 = {"Bread", "Milk", "Eggs","Bread"}
# set2 = {"Bread","Bread", "Milk", "Eggs"}

# common = set1.intersection(set2)
# print(common)

# unique = set1.difference(set2)
# print(unique)

# all_items = set1.union(set2)
# print(all_items)

# sales = [1200, 1500, 900, 1800]

# print(sales[0])   # first item
# print(sales[2])   # third item

# sales[1] = 1600
# print(sales)
# sales.append(2000)
# print(sales)
# for amount in sales:
#     print(amount)
# total_sales = sum(sales)
# print("Total sales:", total_sales)

# customers = ["Alice", "Bob", "Alice", "John", "Bob"]

# unique_customers = set(customers)

# print("Total unique customers:", len(unique_customers))
# print(unique_customers)

daily_temps = [22.5, 24.0, 23.8, 25.1, 26.3, 24.5, 23.0]
days = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

weather_log = {
    "Monday": {"temp": 22.5, "condition": "Sunny"},
    "Tuesday": {"temp": 24.0, "condition": "Cloudy"},
    "Wednesday": {"temp": 23.8, "condition": "Rainy"}
}

# Practice: Find hottest day
hottest_day = max(weather_log.items(), key=lambda x: x[1]['temp'])
print(hottest_day)
# Practice: Count rainy days
# Practice: Calculate weekly average
