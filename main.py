import requests
url = "http://localhost:8080/books"
while True:
    print("1. Add a book")
    print("2. Add books")
    print("3. Exit")
    cmd = input("Enter a command: ")
    if cmd == "1":
        title = input("Enter the title of the book: ")
        author = input("Enter the author of the book: ")
        kind = input("Enter the kind of the book: ")
        book = {"title": title, "author": author, "kind": kind}
        response = requests.post(url, json=book)
    elif cmd == "2":
        titles = input("Enter the titles of the books separated by commas: ").strip().split(",")
        authors = input("Enter the authors of the books separated by commas: ").strip().split(",")
        kinds = input("Enter the kind of the books: ").strip().split(",")
        
        for title, author, kind in zip(titles, authors, kinds):
            book = {"title": title, "author": author, "kind": kind}
            response = requests.post(url, json=book)
    elif cmd == "3":
        print("Exiting")
        break
    else:
        print("Invalid command")