# Problem 20: Remove Duplicates from a List
my_list = input("Enter elements of the list separated by space: ").split()
unique_list = list(set(my_list))
print("List after removing duplicates:", unique_list)

# Problem 21: Sort a List
my_list = input("Enter elements of the list separated by space: ").split()
my_list.sort()
print("Sorted list:", my_list)

# Problem 22: Find Minimum and Maximum in a List
my_list = list(map(int, input("Enter elements of the list separated by space: ").split()))
minimum = min(my_list)
maximum = max(my_list)
print("Minimum:", minimum)
print("Maximum:", maximum)

# Problem 23: Merge Two Lists
list1 = input("Enter elements of the first list separated by space: ").split()
list2 = input("Enter elements of the second list separated by space: ").split()
merged_list = list1 + list2
print("Merged list:", merged_list)

# Problem 24: Count Occurrences of an Element in a List
my_list = input("Enter elements of the list separated by space: ").split()
element = input("Enter the element to count: ")
count = my_list.count(element)
print("Occurrences of", element, ":", count)

# Problem 25: Create a Dictionary from Two Lists
keys = input("Enter keys separated by space: ").split()
values = input("Enter values separated by space: ").split()
my_dict = dict(zip(keys, values))
print("Dictionary:", my_dict)

# Problem 26: Print Keys and Values of a Dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
for key, value in my_dict.items():
    print(key + ":", value)

# Problem 27: Check if a Key Exists in a Dictionary
key = input("Enter a key to check: ")
if key in my_dict:
    print("Key exists in the dictionary.")
else:
    print("Key does not exist in the dictionary.")

# Problem 28: Get Values from a Dictionary
key = input("Enter a key to get its value: ")
value = my_dict.get(key, "Key not found")
print("Value:", value)

# Problem 29: Find the Length of a Dictionary
print("Length of the dictionary:", len(my_dict))

# Problem 30: Reverse a Dictionary
reversed_dict = {value: key for key, value in my_dict.items()}
print("Reversed dictionary:", reversed_dict)

# Problem 31: Read from a File
filename = input("Enter the filename to read from: ")
try:
    with open(filename, 'r') as file:
        content = file.read()
        print("File content:\n", content)
except FileNotFoundError:
    print("File not found.")

# Problem 32: Write to a File
filename = input("Enter the filename to write to: ")
content = input("Enter content to write to the file: ")
with open(filename, 'w') as file:
    file.write(content)
print("Content written to", filename)

# Problem 33: Append to a File
filename = input("Enter the filename to append to: ")
content = input("Enter content to append to the file: ")
with open(filename, 'a') as file:
    file.write(content + "\n")
print("Content appended to", filename)

# Problem 34: Count Lines in a File
filename = input("Enter the filename to count lines: ")
try:
    with open(filename, 'r') as file:
        line_count = sum(1 for line in file)
        print("Number of lines in the file:", line_count)
except FileNotFoundError:
    print("File not found.")

# Problem 35: Read a CSV File
import csv

filename = input("Enter the CSV filename to read: ")
try:
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print("File not found.")

# Problem 36: Write to a CSV File
filename = input("Enter the CSV filename to write to: ")
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles']
]
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
print("Data written to", filename)
