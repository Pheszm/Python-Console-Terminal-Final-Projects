import csv

print("Search for a Book by Title:")
title = input("Enter the book title: ")

with open('Book List.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    data = list(reader)

found_books = []
for row in data:
    if title.lower() in row[0].lower():  # Case-insensitive search
        found_books.append(row)

if found_books:
    print("\nFound Books:")
    for book in found_books:
        print(f"Title: {book[0]}, Copies: {book[1]}, Available: {book[2]}")
else:
    print(f"No books found with the title: {title}")
