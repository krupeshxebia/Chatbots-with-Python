# Define your functions
def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")


def order_latte():
    res = input(
        "And what kind of milk for your latte? \n[a] 2% milk \n[b] Non-fat milk \n[c] Soy milk \n> ")
    output = ''
    if res == 'a':
        output = 'latte'
    elif res == 'b':
        output = 'non-fat latte'
    elif res == 'c':
        output = 'soy latte'
    else:
        print_message()
        output = order_latte()
    return output


def get_drink_type():
    res = input(
        "What type of drink would you like? \n[a] Brewed Coffee \n[b] Mocha \n[c] Latte \n> ")
    output = ''
    if res == 'a':
        output = 'brewed coffee'
    elif res == 'b':
        output = 'mocha'
    elif res == 'c':
        output = order_latte()
    else:
        print_message()
        output = get_drink_type()
    return output


def get_size():
    res = input(
        'What size drink can I get for you? \n[a] Small \n[b] Medium \n[c] Large \n> ')
    output = ''
    if res == 'a':
        output = 'small'
    elif res == 'b':
        output = 'medium'
    elif res == 'c':
        output = 'large'
    else:
        print_message()
        output = get_size()
    return output


def coffee_bot():
    print("Welcome to the cafe!")
    size = get_size()
    drink_type = get_drink_type()
    print(f"Alright, that's a {size} {drink_type}!")
    name = input("Can I get your name please? \n> ")
    print(f"Thanks, {name}! Your drink will be ready shortly.")


# Call coffee_bot()!
coffee_bot()
