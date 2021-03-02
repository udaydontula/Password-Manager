import random


def password_generator():

    a = []
    letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    symbols = ['@','#','$','&','*','?']
    p = random.randint(8, 10)
    n = random.randint(2, 6)
    m = random.randint(2, 4)
    s = random.randint(2, 4)

    password_letter = [random.choice(letters) for _ in range(n)]
    password_numbers = [random.choice(numbers) for _ in range(m)]
    password_symbols = [random.choice(symbols) for _ in range(s)]

    password_list = password_letter + password_numbers + password_symbols
    random.shuffle(password_list)

    password = "".join(password_list)

    return password
