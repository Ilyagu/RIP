def field(items, *args):
    try:
        assert len(args) > 0
    except AssertionError:
        print("Нет второго рагумента")
    if len(args) == 1:
        for i in range(len(items)):
            if args[0] in items[i] and items[i].get(args[0])!=None:
                yield items[i].get(args[0])
    else:
        for i in range(len(items)):
            s={}
            for j in range(len(args)):
                if args[j] in items[i] and items[i].get(args[j]) != None:
                    s.update({args[j]: items[i].get(args[j])})
            yield s


goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'blue'}
]
f=field(goods,'title', 'price')
for i in f:
    print(i, end=', ')
f = field(goods,'title')
for i in f:
    print(i, end=', ')