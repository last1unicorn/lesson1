def format_price(price):
    price = int(price)
    price = f'Цена: {price} руб.'
    return price


if __name__ == '__main__':
    example_variable = format_price(56.24)
    print(example_variable)
