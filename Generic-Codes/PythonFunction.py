# Global variables
total_price_mobile = 0
total_price_shoe = 0
mobile_brand_global = ""  # To store brand for return

def purchase_mobile(price, brand):
    global total_price_mobile, mobile_brand_global
    mobile_brand_global = brand
    if brand == "Apple":
        discount = 10
    else:
        discount = 5
    total_price_mobile = price - price * discount / 100
    print(f"Total price of Mobile ({brand}) after {discount}% discount: {total_price_mobile:.2f}")

def purchase_shoe(price, material):
    global total_price_shoe
    if material == "Leather":
        tax = 5
    else:
        tax = 2
    total_price_shoe = price + price * tax / 100
    print(f"Total price of Shoe after {tax}% Tax: {total_price_shoe:.2f}")

def return_mobile():
    global mobile_brand_global
    print(f"Total Return Price of Mobile ({mobile_brand_global}) Is: {total_price_mobile:.2f}")

def return_shoe():
    print(f"Total Return Price of Shoe Is: {total_price_shoe:.2f}")

# Function calls
purchase_mobile(20000, "Apple")
purchase_shoe(200, "Leather")
return_mobile()
return_shoe()