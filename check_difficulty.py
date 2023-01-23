from random import choices
from itertools import combinations_with_replacement
import matplotlib.pyplot as plt
import copy

items_id = [500, 501, 502, 503, 504, 505, 506,
            600, 601, 602, 603, 604, 605, 606,
            700, 701, 702, 703, 704, 705, 706,
            800, 801, 802, 803, 804, 805, 806,
            900, 901, 902, 903, 904, 905, 906,
            300, 301, 302, 303, 304, 305, 306,
            400, 401, 402, 403, 404, 405, 406,
            1000, 1001, 1002, 1003, 1004, 1005, 1006,
            1100, 1101, 1102, 1103, 1104, 1105, 1106,
            1600, 1601, 1602, 1603
            ]

coins = {
    1600: 1,
    1601: 2,
    1602: 4,
    1603: 8
}


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

    # print(list(generators.keys())[list(generators.values()).index(ans)])
    return ans


def checker(init_field, orders, generators, iterations):
    average_merge = 0
    average_taps_gens = 0
    average_coins = 0

    start_field, start_merges, start_orders = merges(init_field, 0, orders)
    # start_field, start_merges, start_orders = init_field, 0, orders
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

        for c in range(len(cur_field)):
            if cur_field[c] in coins.keys():
                average_coins += coins[cur_field[c]]

        average_merge += cur_merges
        average_taps_gens += taps_gens

    # print("Average merges amount", average_merge / iterations)
    # print("Average generator taps amount", average_taps_gens / iterations)
    # print("Average difficulty", (average_merge + average_taps_gens) / iterations)

    return (average_merge + average_taps_gens) / iterations, average_coins/iterations


def sort_func(e):
    return e[1]


iterations = 100
main_field = [603, 603, 603, 603, 503, 503, 503, 503, 1003, 1003, 1003, 1003, 1003, 1003, 603, 603, 503, 503]
main_orders = [
    [505, 606, 1005],
    [505, 605, 1005],
    [605, 606, 1005],
    [1005, 1006],
    [506, 606, 1006],
]
# generators properties
main_generators = {1: {'items': [503,  1600], 'weights': [10, 1]},2: {'items': [603,  1600], 'weights': [10, 1]}, 3: {'items': [1003,  1600], 'weights': [10, 1]} }

for i in main_orders:
    k, collected_coins = checker([], [i], main_generators, iterations)
    # Order difficulty on the empty field
    print(round(k))

# Orders difficulty with init field, collected coins
total_diff, avr_coins =  checker(main_field, main_orders, main_generators, iterations)
print("Average total difficulty with init field", total_diff)
print("Average collected coins", avr_coins)
