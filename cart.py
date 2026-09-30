cart = []

def add_to_cart(book):
    cart.append(book)
    print(book["title"], "added to cart")

def show_cart():
    print("Shopping Cart:")

    if not cart:
        print("Cart is empty")
    else:
        for book in cart:
            print(book["title"], "Rs.", book["price"])

book = {
    "title": "Python Programming",
    "price": 500
}

add_to_cart(book)
show_cart()