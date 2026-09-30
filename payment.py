def process_payment(amount, method):
    print("Payment Processing")
    print("Amount: Rs.", amount)
    print("Payment Method:", method)

    if amount > 0:
        print("Payment Successful")
    else:
        print("Invalid Payment Amount")


process_payment(500, "UPI")