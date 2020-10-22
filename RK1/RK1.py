# вариант запроса Д
# вариант предметной области 12 : язык программирования - средство разработки
from operator import itemgetter


class ProgramLanguage:
    # язык программирования
    def __init__(self, id, name, users, DT_id):
        self.id = id
        self.name = name
        self.users = users
        self.DT_id = DT_id


class DevelopmentTool:
    # средство разарботки
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PL_DT:
    # язык программирования средства разработки для реализации связи
    # многие-ко-многим
    def __init__(self,  DT_id, PL_id):
        self.DT_id = DT_id
        self.PL_id = PL_id

# средства разработки
DT = [
    DevelopmentTool(1, "Microsoft Visual Studio"),
    DevelopmentTool(2, "NetBeans"),
    DevelopmentTool(3, "PyCharm"),

    DevelopmentTool(4, "IntelliJ IDEA"),
    DevelopmentTool(5, "Eclipse"),
    DevelopmentTool(6, "Aptana Studio 3")
]

# языки программирования
PL = [
    ProgramLanguage(1, "JavaScript", 1604219, 1),
    ProgramLanguage(2, "C#", 229995, 1),
    ProgramLanguage(3, "C++", 330259, 1),
    ProgramLanguage(4, "C", 202295, 2),
    ProgramLanguage(5, "Java", 763783, 2),
    ProgramLanguage(6, "Python", 744045, 3),
    ProgramLanguage(7, "CSS", 271782, 3),
    ProgramLanguage(8, "Ruby", 740610, 3),
    ProgramLanguage(9, "TypeScript", 55587, 3),
    ProgramLanguage(10, "PHP", 478153, 4),
    ProgramLanguage(11, "HTML", 120451, 4),
]

PL_DT_v = [
    PL_DT(1, 1),
    PL_DT(1, 2),
    PL_DT(1, 3),
    PL_DT(2, 4),
    PL_DT(2, 5),
    PL_DT(3, 6),
    PL_DT(3, 7),
    PL_DT(3, 8),
    PL_DT(3, 9),
    PL_DT(4, 10),
    PL_DT(4, 11),
    PL_DT(5, 3),
    PL_DT(5, 4),
    PL_DT(5, 5),
    PL_DT(5, 9),
    PL_DT(6, 1),
    PL_DT(6, 6),
]

def main():
    # соединение данных один-ко-многим
    one_to_many = [(p.name, p.users, d.name)
                   for d in DT
                   for p in PL
                   if p.DT_id == d.id]

    # соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, pd.DT_id, pd.PL_id)
                         for d in DT
                         for pd in PL_DT_v
                         if d.id == pd.DT_id]

    many_to_many = [(p.name, p.users, DT_name)
                    for DT_name, DT_id, PL_id in many_to_many_temp
                    for p in PL if p.id == PL_id]

    print('Задание Д1')
    res1 = []
    for i in one_to_many:
        if i[0][-2:] == "pt":
            res1.append(i[0:3:2])
    print(res1)

    print('\nЗадание Д2')
    res2_unsorted = []
    for d in DT:
        DT_ProL = list(filter(lambda i: i[2] == d.name, one_to_many))
        if len(DT_ProL) > 0:
            d_users = [users for _, users, _ in DT_ProL]
            d_users_sum = sum(d_users)
            d_users_count = len(d_users)
            d_users_count_average = d_users_sum / d_users_count
            res2_unsorted.append((d.name, int(d_users_count_average)))
    res2 = sorted(res2_unsorted, key=itemgetter(1), reverse=True)
    print(res2)

    print('\nЗадание Д3')
    res3 = {}
    for d in DT:
        if d.name[0] == "M":
            DT_ProL = list(filter(lambda i: i[2] == d.name, many_to_many))
            DT_ProL_names = [x for x, _, _ in DT_ProL]
            res3[d.name] = DT_ProL_names
    print(res3)


if __name__ == '__main__':
    main()
