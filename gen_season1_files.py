import json


def gen_item(ind, s):
    res_item = {}
    if ind in generators[i].keys():
        for k in range(len(generators[i][ind]["items"])):
            tmp_s = s + str(generators[i][ind]["items"][k] % 10 + 1)
            w = generators[i][ind]["weights"][k]
            res_item[tmp_s] = float(w)
    return res_item


num_levels = 9

generators = [
    {1: {'items': [501], 'weights': [10]}, 2: {'items': [600], 'weights': [10]}, 3: {'items': [1000], 'weights': [10]}},
]

level_tasks = [[[1, [502]], [1, [503]], [3, [504]], [5, [503, 504]], [5, [505]]],]

level_gifts = [
    [{
        "RewardType": "Beds",
        "Count": 1,
        "Index": 8,
        "Value": "Peas",
        "RewardTypeCategory": "null"
    },
        {
            "RewardType": "Coin",
            "Count": 40,
            "Index": 0,
            "Value": "Coins",
            "RewardTypeCategory": "null"
        }],

]

levels_gens = [
    [["Fries0", 5, 1], ["Hamburger0", 6, 2], ["Pizza0", 10, 3]],]

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
                "type": levels_gens[i][0][1],
                "level_open": 0,
                "energy": 2147483647,
                "timer": 0.0,
                "items": gen_item(levels_gens[i][0][2], levels_gens[i][0][0])
            },
            {
                "type": levels_gens[i][1][1],
                "level_open": 3,
                "energy": 2147483647,
                "timer": 0.0,
                "items": gen_item(levels_gens[i][1][2], levels_gens[i][1][0])
            },
            {
                "type": levels_gens[i][2][1],
                "level_open": 5,
                "energy": 2147483647,
                "timer": 0.0,
                "items": gen_item(levels_gens[i][2][2], levels_gens[i][2][0])
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
