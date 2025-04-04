def field(items, *args):
    assert len(args) > 0

    if len(args) == 1:
        result = (item[args[0]] for item in items if args[0] in item and item[args[0]] is not None)
        yield ', '.join(result)
    else:
        for item in items:
            filtered_item = {}
            include_item = False
            for field_name in args:
                if field_name in item and item[field_name] is not None:
                    filtered_item[field_name] = item[field_name]
                    include_item = True
            if include_item:
                yield filtered_item

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]

gen = field(goods, 'title')
while True:
    try:
        result = next(gen)
        print(result)
    except StopIteration:
        break

print()

gen = field(goods, 'title', 'price')
while True:
    try:
        result = next(gen)
        print(result)
    except StopIteration:
        break

print()

gen = field(goods, 'title', 'color')
while True:
    try:
        result = next(gen)
        print(result)
    except StopIteration:
        break

print()

gen = field(goods, 'title', 'price', 'color')
while True:
    try:
        result = next(gen)
        print(result)
    except StopIteration:
        break
