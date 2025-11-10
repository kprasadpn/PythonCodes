total_price_mobile = 0
total_price_shoe = 0 
def purchase_mobile(price,brand):
    global total_price_mobile
    if brand == "Mobile":
        discount = 10
    else:
        discount = 5
    total_price_mobile = price - price * discount / 100
    print(f"Total price of Mobile after {discount}% discount: {total_price_mobile:.2f}")

def purchase_shoe(price,material):
    global total_price_shoe
    if material == "Leather":
        tax = 5
    else:
        tax = 2
    total_price_shoe = price + price * tax / 100
    print(f"Total price of Mobile after {tax}% Tax: {total_price_shoe:.2f}")
def return_mobile():
    print(f"Total Return Price of Mobile Is: {total_price_mobile:.2f}")
def return_shoe():
    print(f"Total Return Price of shoe Is: {total_price_shoe:.2f}")
purchase_mobile(20000,"Apple")
purchase_shoe(200,"Leather")
return_mobile()
return_shoe()
