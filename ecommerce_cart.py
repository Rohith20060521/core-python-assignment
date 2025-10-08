def calculate_cart_total(cart_items):
    if not cart_items:
        return 0
    total_price = sum(cart_items.values())
    item_count = len(cart_items)
    if item_count > 5:
        discount_rate = 0.10
        discount_amount = total_price * discount_rate
        final_price = total_price - discount_amount
        return final_price
    else:
        return total_price
cart_items = {'Laptop': 50000, 'Headphones': 2000, 'Mouse': 500, 'Keyboard': 1500}
total = calculate_cart_total(cart_items)
print(f"Total Price: {total}")
cart_with_discount = {
    'Laptop': 50000, 
    'Headphones': 2000, 
    'Mouse': 500, 
    'Keyboard': 1500, 
    'Monitor': 10000, 
    'Webcam': 1000
}
discounted_total = calculate_cart_total(cart_with_discount)