import string
import random

characters = string.ascii_letters + string.digits

def generate_item_no(length = 8):
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

def generate_deal_no(length = 6):
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

    

