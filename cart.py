cart = []

def add_to_cart(book):
    cart.append(book)
    print(book["title"], "added to cart")

def show_cart():
    print("Shopping Cart:")
    for book in cart:
        print(book["title"], book["price"])