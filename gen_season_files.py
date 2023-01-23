import json


def gen_item(ind, s):
    res_item = {}
    cur_gen = generators[ind][s]
    items = cur_gen['items']
    weights = cur_gen['weights']

    for _ in range(len(items)):
        tmp_name = items[_] // 100
        name = gen_names[tmp_name] + str(items[_] % 100 + 1)
        res_item[name] = weights[_]

    return res_item


generators = [
    {1: {'items': [501, 1600], 'weights': [10, 1]}, 2: {'items': [600, 1600], 'weights': [10, 1]},
     3: {'items': [1000, 1600], 'weights': [10, 1]}},
    {1: {'items': [502, 1600], 'weights': [10, 1]}, 2: {'items': [600, 1600], 'weights': [10, 1]},
     3: {'items': [1000, 1600], 'weights': [10, 1]}},
    {1: {'items': [502, 1600], 'weights': [10, 1]}, 2: {'items': [600, 1600], 'weights': [10, 1]},
     3: {'items': [1000, 1600], 'weights': [10, 1]}},
    {1: {'items': [502, 1600], 'weights': [10, 1]}, 2: {'items': [601, 1600], 'weights': [10, 1]},
     3: {'items': [1000, 1600], 'weights': [10, 1]}},
    {1: {'items': [502, 1600], 'weights': [10, 1]}, 2: {'items': [601, 1600], 'weights': [10, 1]},
     3: {'items': [1000, 1600], 'weights': [10, 1]}},
    {1: {'items': [503, 1600], 'weights': [10, 1]}, 2: {'items': [602, 1600], 'weights': [10, 1]},
     3: {'items': [1001, 1600], 'weights': [10, 1]}},
    {1: {'items': [503, 1600], 'weights': [10, 1]}, 2: {'items': [602, 1600], 'weights': [10, 1]},
     3: {'items': [1002, 1600], 'weights': [10, 1]}},
    {1: {'items': [503, 1600], 'weights': [10, 1]}, 2: {'items': [602, 1600], 'weights': [10, 1]},
     3: {'items': [1002, 1600], 'weights': [10, 1]}},
    {1: {'items': [503, 1600], 'weights': [10, 1]}, 2: {'items': [603, 1600], 'weights': [10, 1]},
     3: {'items': [1003, 1600], 'weights': [10, 1]}},
]

level_tasks = [[[1, [502]], [1, [503]], [3, [504]], [4, [503, 504]], [5, [505]]], [[1, [504]], [3, [505]], [4, [504, 505]], [5, [506]], [5, [504, 506]]], [[1, [602]], [3, [603]], [4, [602, 603]], [5, [604]], [5, [603, 604]]], [[2, [504, 603]], [4, [505, 603]], [4, [504, 602, 604]], [5, [506, 603]], [5, [504, 505, 604]]], [[1, [1002]], [3, [1003]], [4, [1002, 1003]], [5, [1004]], [5, [1003, 1004]]], [[4, [603, 1003, 506]], [4, [1004, 505, 603]], [4, [1003, 1004, 604]], [3, [605]], [5, [605, 1004, 505]]], [[4, [506, 604, 1004]], [4, [505, 506, 1003]], [3, [604, 1004, 505]], [4, [1005, 505]], [5, [606]]], [[5, [505, 605, 1004]], [4, [505, 1005]], [5, [506, 605, 1004]], [5, [506, 1005]], [5, [1006]]], [[4, [505, 606, 1005]], [3, [505, 605, 1005]], [4, [605, 606, 1005]], [4, [1005, 1006]], [5, [506, 606, 1006]]]]


level_gifts = [
    [{
        "RewardType": "Toy",
        "Count": 1,
        "Index": 2,
        "Value": "ClawToy",
        "RewardTypeCategory": "null"
    },
        {
            "RewardType": "Coin",
            "Count": 45,
            "Index": 0,
            "Value": "Coins",
            "RewardTypeCategory": "null"
        }],
    [{
        "RewardType": "Toy",
        "Count": 1,
        "Index": 7,
        "Value": "DiskToy",
        "RewardTypeCategory": "null"
    },
        {
            "RewardType": "Coin",
            "Count": 20,
            "Index": 0,
            "Value": "Coins",
            "RewardTypeCategory": "null"
        }],
    [{
        "RewardType": "Beds",
        "Count": 1,
        "Index": 7,
        "Value": "Mint",
        "RewardTypeCategory": "null"
    },
        {
            "RewardType": "Coin",
            "Count": 50,
            "Index": 0,
            "Value": "Coins",
            "RewardTypeCategory": "null"
        }],
    [{
        "RewardType": "HumanEats",
        "Count": 1,
        "Index": 3,
        "Value": "Bananas",
        "RewardTypeCategory": "null"
    }],
    [{
        "RewardType": "Trays",
        "Count": 1,
        "Index": 3,
        "Value": " Flowers",
        "RewardTypeCategory": "null"
    },
        {
            "RewardType": "Coin",
            "Count": 20,
            "Index": 0,
            "Value": "Coins",
            "RewardTypeCategory": "null"
        }],
    [{
        "RewardType": "Beds",
        "Count": 1,
        "Index": 8,
        "Value": " Peas",
        "RewardTypeCategory": "null"
    },
        {
            "RewardType": "Coin",
            "Count": 20,
            "Index": 0,
            "Value": "Coins",
            "RewardTypeCategory": "null"
        }],
    [{
        "RewardType": "HumanEats",
        "Count": 1,
        "Index": 17,
        "Value": "Pears",
        "RewardTypeCategory": "null"
    }, {
        "RewardType": "Coin",
        "Count": 20,
        "Index": 0,
        "Value": "Coins",
        "RewardTypeCategory": "null"
    }],
    [{
        "RewardType": "Trays",
        "Count": 1,
        "Index": 10,
        "Value": "ClosedUfo",
        "RewardTypeCategory": "null"
    }],
    [{
        "RewardType": "Toy",
        "Count": 1,
        "Index": 3,
        "Value": "Box", "RewardTypeCategory": "null"
    }],

]

gen_names = {5: "Fries0",
             6: "Hamburger0",
             10: "Pizza0",
             16: "Coins0"}

"""
Generator type, level open, index in generators
"""
levels_gens = [[[5, 0, 1], [6, 3, 2], [10, 5, 3]],
               [[5, 0, 1], [6, 3, 2], [10, 5, 3]],
               [[5, 0, 1], [6, 3, 2], [10, 5, 3]],
               [[5, 0, 1], [6, 3, 2], [10, 5, 3]],
               [[5, 0, 1], [6, 3, 2], [10, 5, 3]],
               [[5, 0, 1], [6, 3, 2], [10, 5, 3]],
               [[5, 0, 1], [6, 3, 2], [10, 5, 3]],
               [[5, 0, 1], [6, 3, 2], [10, 5, 3]],
               [[5, 0, 1], [6, 3, 2], [10, 5, 3]],
               [[5, 0, 1], [6, 3, 2], [10, 5, 3]]]

for i in range(len(generators)):
    tasks = []
    for j in range(len(level_tasks[i])):
        tmp_json = {"$type": "Appcraft.Puzzles.Game.DestroyCellsTaskData, Assembly-CSharp",
                    "DestroyCellsTaskResult": [],
                    "items_list": level_tasks[i][j][1],
                    "task_reward": level_tasks[i][j][0] - 1
                    }
        tasks.append(tmp_json)

    dictionary = {
        "id": "level_" + str(i),
        "field_rows": 5,
        "field_columns": 5,
        "generators_list": [
            {
                "type": levels_gens[i][0][0],
                "level_open": levels_gens[i][0][1],
                "energy": 2147483647,
                "timer": 0.0,
                "items": gen_item(i, levels_gens[i][0][2])
            },
            {
                "type": levels_gens[i][1][0],
                "level_open": levels_gens[i][1][1],
                "energy": 2147483647,
                "timer": 0.0,
                "items": gen_item(i, levels_gens[i][1][2])
            },
            {
                "type": levels_gens[i][2][0],
                "level_open": levels_gens[i][2][1],
                "energy": 2147483647,
                "timer": 0.0,
                "items": gen_item(i, levels_gens[i][2][2])
            }
        ],
        "start_field": {
            "cells": [
                [
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    }
                ],
                [
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    }
                ],
                [
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    }
                ],
                [
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    }
                ],
                [
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    },
                    {
                        "cell_type": 0
                    }
                ]
            ]
        },
        "level_tasks": tasks,
        "field_reward": level_gifts[i]
    }

    # Serializing json
    json_object = json.dumps(dictionary, indent=4)

    # Writing to levels to folder
    tmp = "Summer/level_" + str(i + 1) + ".json"
    with open(tmp, "w") as outfile:
        outfile.write(json_object)


