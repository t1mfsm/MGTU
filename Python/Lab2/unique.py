import random

class Unique:
    def __init__(self, data, **kwargs):
        self.data = data
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()
        self.iterator = iter(data)

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            try:
                item = next(self.iterator)
            except StopIteration:
                raise StopIteration
            key = item.lower() if self.ignore_case and isinstance(item, str) else item
            if key not in self.seen:
                self.seen.add(key)
                return item

def gen_random(count, minimum, maximum):
    for _ in range(count):
        yield random.randint(minimum, maximum)

data = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
unique_data = Unique(data)
for item in unique_data:
    print(item, end=' ')

print()

random_numbers = gen_random(10, 1, 3)
unique_numbers = Unique(random_numbers)
for number in unique_numbers:
    print(number, end=' ')

print()

data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
unique_data = Unique(data)
for item in unique_data:
    print(item, end=' ')

print()

data = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
unique_data = Unique(data, ignore_case=True)
for item in unique_data:
    print(item, end=' ')
