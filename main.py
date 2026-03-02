
# Project Name: Week 6 Lab
# Course: SP 2026 CS 125 Programming for Everyone II
# Name: Kevin Pavione
# Date: Feb 26, 2026

# Import Statements
import json
import xml.etree.ElementTree as ET

# Exercise 1 - JSON Basics

# Creation of dictionary represents a student record
student_dict = {
    "id": 101,
    "name": "Zach Wilson",
    "email": "zwilson@oak.edu",
    "major": "Computer science",
    "gpa": 3.96,
    "courses": ["Computing I", "Computing II", "Web Development"]
}
print("--- Newly Created Student Dictionary ---")
print(student_dict)

# Convert to JSON String
json_string = json.dumps(student_dict, indent=2)
print("--- Pretty Printed JSON String ---")
print(json_string)

# Write JSON to File
with open("student.json", "w") as f:
    json.dump(student_dict, f, indent=2)

# Parse JSON string back to dictionary / JSON obj
parsed_dict = json.loads(json_string)

# Read from file and access specific key
with open("student.json", "r") as f:
    data_from_file = json.load(f)
    print(f"\nExtracted Major: {data_from_file['major']}")


# Exercise 3 - XML Parsing

# Parse the XML file using ElementTree (ET)
tree = ET.parse("student.xml")
root = tree.getroot()

# Vars for calculations
total_price = 0
book_count = 0
books_2024 = []

# Display books in a formatted table
print(f"{'ID':<5} | {'Title':<20} | {'Year':<6} | {'Price':<8}")
print("-"* 30)

for book in root.findall('book'):
    # Extract some elements such as attributes and child elements
    book_id = book.get('id')
    title = book.find('title').text
    year = book.find('year').text
    price = float(book.find('price').text)

    # Calculate average logic
    total_price += price
    book_count += 1

    # Filter for 2024 books
    if year == "2024":
        books_2024.append(book)

    # Print table row
    print(f"{book_id:<5} | {title:<20} | {year:<6} | {price:8.2f}")

# Print Exercise 3 Requirements
print(f"\nBooks Published in 2024: {', ' .join(books_2024)}")
print(f"Average Book Price: ${total_price / book_count:.2f}")


# Exercise 4 - Data Transformation (JSON to XML)

# Read the products JSON file
with open("books.json", "w") as f:
    json_data = json.load(f)

# Create XML Structure using ElementTree (ET)
xml_root = ET.Element("inventory")

for p in json_data['products']:
    # Convert each product to an XML element
    # Use str() because XML values must be strings
    pass

# Write to products.xml with indentation for readability
new_tree = ET.ElementTree(xml_root)
ET.indent(new_tree, space=" ")
new_tree.write("products.xml", encoding="utf-8", xml_declaration=True)

# Verify by reading XML and printing product names
print("Verification of Product Names in new XML file")
verify_tree = ET.parse("products.xml")
for prod in verify_tree.findall('product'):
    print(f" - {prod.find('name').text}")
