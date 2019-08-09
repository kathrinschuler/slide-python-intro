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

BLURB = "\nOperators\nIn this excercise you'll get to see how much you know about how to do simple maths using python\nThe following questions are all multiple choice, only one answer will be correct.\nAnswer using the letter (a, b, c or d)."


TASKS = [
    [
        "Which symbol do we use to add numbers?",  # background info
        "\n\ta. +\n\tb. \\\n\tc. /\n\td. %\n\t",  # question
        ["a"],  # list of required keywords
        {"a": "", "b": "", "c": "", "d": ""},  # dict of variables to set up before question
    ],
    [
        "Which symbol do we use to subtract numbers?",  # background info
        "\n\ta. +\n\tb. -\n\tc. /\n\td. %\n\t",  # question
        ["b"],  # list of required keywords
        {"a": "", "b": "", "c": "", "d": ""},  # dict of variables to set up before question
    ],
    [
        "Which symbol do we use to multiply two numbers together?",  # background info
        "\n\ta. *\n\tb. x\n\tc. ^\n\td. !\n\t",  # question
        ["a"],  # list of required keywords
        {"a": "", "b": "", "c": "", "d": ""},  # dict of variables to set up before question
    ],
    [
        "Which symbol do we use to divide numbers?",  # background info
        "\n\ta. ÷\n\tb. /\n\tc. ^\n\td. \\\n\t",  # question
        ["b"],  # list of required keywords
        {"a": "", "b": "", "c": "", "d": ""},  # dict of variables to set up before question
    ],
    [
        "If you divide 11 by 4 you would get a remainder of 3, which symbol do we use in python to get the remainder when one number is divided by another?",  # background info
        "\n\ta. ÷\n\tb. /\n\tc. ^\n\td. %\n\t",  # question
        ["d"],  # list of required keywords
        {"a": "", "b": "", "c": "", "d": ""},  # dict of variables to set up before question
    ],
    [
        "Which code would give the answer 25?",  # background info
        "\n\ta. 5^\n\tb. 5**2\n\tc. 5²\n\td. 5*2\n\t",  # question
        ["b"],  # list of required keywords
        {"a": "", "b": "", "c": "", "d": ""},  # dict of variables to set up before question
    ],
    [
        "Which is correct code?",  # background info
        "\n\ta. '1' + '2'\n\tb. 1 '+' 2\n\tc. 1 + 2\n\td. '1 + 2'\n\t",  # question
        ["c"],  # list of required keywords
        {"a": "", "b": "", "c": "", "d": ""},  # dict of variables to set up before question
    ],
]
