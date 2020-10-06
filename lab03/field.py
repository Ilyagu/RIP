def field(items, *args):
    try:
        assert len(args) > 0
    except AssertionError:
        print("Нет второго рагумента")
    if len(args)==1:
        for i in range(len(goods)):
            if args[0] in goods[i] and goods[i].get(args[0])!=None:
                if i==len(goods)-1:
                    print(goods[i].get(args[0]),end="\n")
                else:
                    print(goods[i].get(args[0]),end=', ')
    else:
        for i in range(len(goods)):
            s={}
            for j in range(len(args)):
                if args[j] in goods[i] and goods[i].get(args[j]) != None:
                    s.update({args[j]: goods[i].get(args[j])})
            if i == len(goods) - 1:
                print(s,end="\n")
            else:
                print(s, end=', ')

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'blue'}
]
field(goods,'title', 'price')
field(goods,'title')