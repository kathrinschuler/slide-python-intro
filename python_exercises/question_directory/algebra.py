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
    "\n\ta. \n\tb. \n\tc. \n\td. \n\t", # question
    [], # list of required keywords
    {"a": "", "b":"", "c": "", "d": ""}, # dict of variables to set up before question
],
"""

BLURB = "\nAlgebra\n"

TASKS = [
    [
        "",  # background info
        "Create a variable called: x\nand assign that variable the value of 5.",  # question
        ["x", "=", "5"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "Create a variable called: y\nand assign that variable the value of 11.",  # question
        ["y", "=", "11"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "Add x and y",  # question
        ["x", "+", "y"],  # list of required keywords
        {"x": 5, "y": 11},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "Create a variable called n\nand assign it the value of x added to y",  # question
        ["n", "=", "x", "+", "y"],  # list of required keywords
        {"x": 5, "y": 11},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "Multiply x by 15",  # question
        ["x", "*", "15"],  # list of required keywords
        {"x": 5},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "Given these assignments:\nx = 5\ny = 11\nn = x + y\nWhat value do you think n has? (Type the number then enter)",  # question
        ["16"],  # list of required keywords
        {"x": 5, "y": 11},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "Reassign x to the value of 17",  # question
        ["x", "=", "17"],  # list of required keywords
        {"x": 5},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "Now you've reassigned x the value of 17, what do you think the value of x + 1 would be?",  # question
        ["18"],  # list of required keywords
        {"x": 17},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "The value of n was 16 before we reassigned x to 17. What do you think the value of n is now?",  # question
        ["16"],  # list of required keywords
        {"n": 16},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "Assign n the value of x added to y again",  # question
        ["n", "=", "x", "+", "y"],  # list of required keywords
        {"x": 17, "y": 11},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "Given these assignments:\nx = 17\ny = 11\nn = x + y\nWhat value do you think n has now?",  # question
        ["28"],  # list of required keywords
        {"x": 17, "y": 11, "n": 28},  # dict of variables to set up before question
    ],
]
