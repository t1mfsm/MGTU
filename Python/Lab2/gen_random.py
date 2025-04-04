import random

def gen_random(count, minimum, maximum):
    for _ in range(count):
        yield random.randint(minimum, maximum)

random_numbers = gen_random(6, 1, 50)
for number in random_numbers:
    print(number, end=' ')
