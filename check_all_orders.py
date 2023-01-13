import random
from random import choices
from itertools import combinations
import matplotlib.pyplot as plt
import copy


items_id = [500, 501, 502, 503, 504, 505, 506,
            600, 601, 602, 603, 604, 605, 606,
            1000, 1001, 1002, 1003, 1004, 1005, 1006]

orders_items_id = [505, 506, 605, 606, 1005, 1006]


def merges(field, tap, order):
    if len(field) == 0:
        return [field, tap, order]
    field.sort()
    if len(order) != 0:
        for i in range(len(order[0])):
            for j in range(len(field)):
                if order[0][i] == field[j]:
                    del order[0][i]
                    if len(order[0]) == 0:
                        del order[0]
                    del field[j]
                    return merges(field, tap, order)
    cur = field[0]
    for i in range(1, len(field)):
        if cur < field[i]:
            cur = field[i]
        else:
            tmp_id = (cur // 100) * 100 + (cur % 10 + 1)
            if tmp_id in items_id:
                f = field
                f.remove(cur)
                f.remove(cur)
                f.append(tmp_id)
                return merges(f, tap + 1, order)
    return [field, tap, order]


def choose_generator(gens, order):
    values = list(gens.values())
    ans = 0
    for v in range(len(values)):
        for j in values[v]["items"]:
            if j // 100 == order // 100:
                ans = values[v]

    return ans


def checker(init_field, orders, generators, iterations):
    average_merge = 0
    average_taps_gens = 0

    start_field, start_merges, start_orders = merges(init_field, 0, orders)

    for i in range(iterations):
        cur_field = copy.deepcopy(start_field)
        cur_merges = start_merges
        cur_orders = copy.deepcopy(start_orders)
        taps_gens = 0
        while len(cur_orders) != 0:
            cur_generator = choose_generator(generators, cur_orders[0][0])
            new_item = choices(cur_generator['items'], cur_generator['weights'])[0]
            taps_gens += 1
            cur_field.append(new_item)
            cur_field, cur_merges, cur_orders = merges(cur_field, cur_merges, cur_orders)

        average_merge += cur_merges
        average_taps_gens += taps_gens

    return (average_merge + average_taps_gens) / iterations


def sort_func(e):
    return e[1]


def r(e):
    return e[0]


def choice_order(prev_orders, possible_orders):
    if len(prev_orders) == 0:
        return random.choice(possible_orders)
    else:
        t = ()
        for _ in range(len(possible_orders)):
            # t = possible_orders[_]
            t = random.choice(possible_orders)
            if len(list(set(t) & set(prev_orders[-1]))) > 0 or (t == prev_orders[-1]):
                continue
            else:
                break
        return t


temp = list(combinations(orders_items_id, 1))
temp += list(combinations(orders_items_id, 2))
temp += list(combinations(orders_items_id, 3))

list_orders = []

for i in range(len(temp)):
    main_field = []
    main_orders = [list(temp[i])]

    main_generators = {1: {'items': [503], 'weights': [10]},2: {'items': [603], 'weights': [10]}, 3: {'items': [1002], 'weights': [10]} }

    iterations = 1000

    list_orders.append([temp[i], round(checker(main_field, main_orders, main_generators, iterations))])

dict_orders = dict(list_orders)
d = {}

for k, v in dict_orders.items():
    if v in d:
        d[v].append(k)
    else:
        d[v] = [k]

result = []

print("All orders")
for k, v in d.items():
    result.append([k, v])

result.sort(key=r)

for i in range(len(result)):
    print(result[i])