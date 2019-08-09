# TASKS is a list of lists. Each sublist follows this structure:
# [
#   <string of background information to print>,
#   <string of question text>,
#   <list of answer keywords>,
#   <dictionary of prerequisite conditions>
# ]

"""
empty object for copy-paste:
[
    "", # background info
    "", # question
    [], # list of required keywords
    {}, # dict of variables to set up before question
],
"""

CLOTHES = ["shirt", "trousers", "blouse", "socks", "leggings", "shorts"]
SHOES = ["sneakers", "heels", "flip-flops"]

PRINT_CLOTHES = "clothes = {}".format(CLOTHES)
PRINT_SHOES = "shoes = {}".format(SHOES)

BLURB = "\n\nFor the following questions remember that lists are zero-indexed. Meaning the first element will be at index 0, the second element at index 1 etc.\n\n"

TASKS = [
    [
        PRINT_CLOTHES,
        "Can you change the third element to be 'jacket' instead?\n\n",
        ["clothes", "2", "'jacket'"],
        {"clothes": CLOTHES},
    ],
    [
        PRINT_CLOTHES,
        "Can you change the last element to be 'hat' insted?\n\n",
        ["clothes", "-1", "'hat'"],
        {"clothes": CLOTHES},
    ],
    [
        PRINT_CLOTHES,
        "Can you change the second-to-last element to be the same as the first element?\n\n",
        ["clothes", "-2", "0"],
        {"clothes": CLOTHES},
    ],
    [
        PRINT_CLOTHES,
        "Can you append 'jumper' to the list?\n\n",
        ["clothes", "append", ".", "('jumper')"],
        {"clothes": CLOTHES},
    ],
    [
        "You have another list, " + PRINT_SHOES,
        "Can you add all the items from shoes to clothes and re-assign to clothes?\n\n",
        ["clothes", "=", "+", "shoes"],
        {"clothes": CLOTHES, "shoes": SHOES},
    ],
    [PRINT_SHOES, "Can you mutiply this list by 5?\n", ["shoes", "*", "5"], {"shoes": SHOES}],
    [
        PRINT_CLOTHES,
        "Can you remove the element 'socks' from the list without knowing its index?\n\n",
        ["clothes", "('socks')", ".", "remove"],
        {"clothes": CLOTHES},
    ],
    [
        PRINT_CLOTHES,
        "Can you remove the second element from the list?\n\n",
        ["del", "clothes", "[1]"],
        {"clothes": CLOTHES},
    ],
]
