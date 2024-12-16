# Problem 37: Read JSON File
import json

filename = input("Enter the JSON filename to read: ")
try:
    with open(filename, 'r') as file:
        data = json.load(file)
        print("JSON data:", data)
except FileNotFoundError:
    print("File not found.")
except json.JSONDecodeError:
    print("Error decoding JSON.")

# Problem 38: Write to a JSON File
filename = input("Enter the JSON filename to write to: ")
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}
with open(filename, 'w') as file:
    json.dump(data, file)
print("Data written to", filename)

# Problem 39: Flatten a Nested List
nested_list = input("Enter a nested list (e.g., [[1, 2], [3, 4]]): ")
nested_list = eval(nested_list)  # Use eval carefully; it's better to use ast.literal_eval in production
flat_list = [item for sublist in nested_list for item in sublist]
print("Flattened list:", flat_list)

# Problem 40: Find Common Elements in Two Lists
list1 = input("Enter elements of the first list separated by space: ").split()
list2 = input("Enter elements of the second list separated by space: ").split()
common_elements = set(list1) & set(list2)
print("Common elements:", common_elements)

# Problem 41: Create a Simple Calculator
def calculator():
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))
    
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        result = num1 / num2
    else:
        result = "Invalid operator"
    
    print("Result:", result)

calculator()

# Problem 42: Generate a Random Number
import random

random_number = random.randint(1, 100)
print("Random number between 1 and 100:", random_number)

# Problem 43: Create a Simple To-Do List
todo_list = []
while True:
    task = input("Enter a task (or type 'exit' to finish): ")
    if task.lower() == 'exit':
        break
    todo_list.append(task)

print("Your To-Do List:")
for i, task in enumerate(todo_list, 1):
    print(f"{i}. {task}")

# Problem 44: Count Characters in a String
text = input("Enter a string: ")
char_count = len(text)
print("Number of characters:", char_count)

# Problem 45: Find the Second Largest Number in a List
my_list = list(map(int, input("Enter elements of the list separated by space: ").split()))
unique_list = list(set(my_list))
unique_list.sort()
if len(unique_list) < 2:
    print("Not enough unique elements to find the second largest.")
else:
    print("Second largest number is:", unique_list[-2])

# Problem 46: Check if a String is an Anagram
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if sorted(str1) == sorted(str2):
    print("The strings are anagrams.")
else:
    print("The strings are not anagrams.")

# Problem 47: Find the Most Frequent Element in a List
my_list = input("Enter elements of the list separated by space: ").split()
most_frequent = max(set(my_list), key=my_list.count)
print("Most frequent element:", most_frequent)

# Problem 48: Create a Simple Stopwatch
import time

input("Press Enter to start the stopwatch...")
start_time = time.time()
input("Press Enter to stop the stopwatch...")
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.2f} seconds")

# Problem 49: Generate a List of Squares
n = int(input("Enter a number: "))
squares = [i**2 for i in range(n)]
print("List of squares:", squares)

# Problem 50: Create a Simple Quiz
score = 0
questions = {
    "What is the capital of France? ": "Paris",
    "What is 2 + 2? ": "4",
    "What is the color of the sky? ": "blue"
}

for question, answer in questions.items():
    user_answer = input(question)
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Wrong! The correct answer is:", answer)

print("Your total score is:", score, "out of", len(questions))
