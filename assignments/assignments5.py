#2.1
coordinates = (40.7128, -74.0060)
print("Original coordinates:", coordinates)
temp = list(coordinates)
temp[0] = 40.8
coordinates = tuple(temp)
print("Updated coordinates:", coordinates)

#2.2
item = {"name": "Laptop", "price": 1200, "stock": 5}
print("Original item:", item)
item["price"] = 1150
item["brand"] = "ProTech"
print("Item keys:", item.keys())
del item["stock"]
print("Final item:", item)

#3.1
def calculate_area(length, width=1):
    area = length * width
    return area
result1 = calculate_area(5, 3)
print("Area with length and width:", result1)
result2 = calculate_area(5)
print("Area with only length:", result2)

#3.2
students = [ {"name": "Alice", "grade": 85}, {"name": "Bob", "grade": 58}, {"name": "Charlie", "grade": 92}, {"name": "Daisy", "grade": 45} ]
def analyze_grades(student_list):
    total = 0
    for student in student_list:
        name = student["name"]
        grade = student["grade"]
        total = total + grade
        if grade >= 60:
            print(name, "Passed")
        else:
            print(name, "Failed")
    average = total / len(student_list)
    return average
avg = analyze_grades(students)
print("Class average:", format(avg, ".2f"))