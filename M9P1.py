# Kirill M9P1 10/07/2026

# Define a function
def compute(quantity, price):
    total = quantity * price
# If statement for total
    if total > 10000:
        discount = 0.1
    else: 
        discount = 0
    extended_price = total + (total * discount)
    return total, extended_price

# Asking to continue program 
start = input("Do you want to continue? (Y/N)")

# Variable which contain all total variables
grand_total = 0

# Beginning of the loop 
while start == "Y":
    quantity = int(input("Enter quantities: "))
    price = float(input("Enter price: "))

# Calling for function   
    total, extended_price = compute(quantity, price)
    grand_total += extended_price

# Printing 4 conditions    
    print(f"Quantity: {quantity}")
    print(f"Price: ${price}")
    print(f"Total: ${total:,.2f}")
    print(f"Extended price: ${extended_price:,.2f}") 

# Asking to continue program
    start = input("Do you want to continue? (Y/N)")

# Printing final statement
print(f"Total extended price: ${grand_total:,.2f}")