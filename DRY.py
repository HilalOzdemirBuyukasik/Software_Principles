#Do not repeat yourself principle

def calculate_discounted_price(price, discount):
    discounted_price = price - (price * discount)
    return discounted_price

def display_discounted_price(product_name, price, discount):
    discounted_price = calculate_discounted_price(price, discount)
    print(f'Discounted price for {product_name}: {discounted_price}')

display_discounted_price('Product 1', 200, 0.1)
display_discounted_price('Product 2', 300, 0.15)
display_discounted_price('Product 3', 350, 0.2)