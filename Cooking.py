import json
import pprint

with open('recipes.txt', 'r', encoding='UTF-8') as file:
    cook_book = {}
    for eat in file:
        count_ = int(file.readline())
        list_ = []
        for i in range(count_):
            a, b, c = file.readline().strip().split(' | ')
            list_.append({'ingredient_name': a, 'quantity': b, 'measure': c,})
        file.readline()
        cook_book[eat.strip()] = list_
    # pprint.pprint(cook_book['Омлет'])


def get_shop_list_dishes(dishes, person_count):
    shop_list = {}
    for dish in cook_book:
        if dish in cook_book.keys():
            res = cook_book.get(dish)
            for el in res:
                if el['ingredient_name'] not in shop_list.keys():
                    shop_list.update({el['ingredient_name'] : {'measure': el['measure'], 'quantity': int(el['quantity']) * person_count}})
    return shop_list

# pprint.pprint(get_shop_list_dishes(['Омлет', 'Фахитос'], 2))

with open('1.txt', encoding='utf-8') as f1, open('2.txt', encoding='utf-8') as f2, open('3.txt', encoding='utf-8') as f3, open('5.txt', 'w') as f5:
    txt_ = [f1.readlines(), f2.readlines(), f3.readlines()]
    a = {'1.txt': [len(txt_[0]), txt_[0]]}
    b = {'2.txt': [len(txt_[1]), txt_[1]]}
    c = {'3.txt': [len(txt_[2]), txt_[2]]}
    d = a | b | c
    d_dict = {}
    sorted_key = sorted(d, key=d.get)

    for w in sorted_key:
        d_dict[w] = d[w]

    for k, v in d_dict.items():
        x = f"{k}\n {v[0]}\n {''.join(v[1])}"
        f5.write(x)