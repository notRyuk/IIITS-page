"""
Instructions
1. name the pdf to book1, book2....
2. run this python code and upload the .txt file generated to the folder 
"""

import os

books = []
for file in os.listdir():
    if file.endswith(".pdf"):
        is_valid = input(f"Is this pdf file a valid book {file} [y/n]: ")
        if is_valid not in ("y", "Y"):
            continue
        authors = input("Enter the author names[separated by ,]: ")
        book = input("Enter the name of the book: ")
        version = input("Enter the version of the book: ")
        books.append(f"{file[:-4]}!~{book}!~{authors}!~{version}")

with open("info.txt", "w") as f:
    f.write("\n".join(books))

