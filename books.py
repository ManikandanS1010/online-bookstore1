books = [
    {"id": 1, "title": "Python Programming", "price": 500},
    {"id": 2, "title": "Java Programming", "price": 600},
    {"id": 3, "title": "Machine Learning", "price": 750}
]

def display_books():
    for book in books:
        print(book["id"], book["title"], book["price"])

display_books()