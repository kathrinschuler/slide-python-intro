# Slide link: https://kathrinschuler.github.io/slide-python-intro/#/25/4

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

BLURB = "For the following questions answer by typing the letter a, b or c. These will correspond to the multiple choice answers you'll see below.\n"
TASKS = [
    [
        "\ndef hello(name)\n    print('hello ' + name)\n    return\n",  # background info
        "What's missing?\n a. :\n b. def\n c. '\n",  # question
        ["a"],  # list of required keywords
        {"a": "", "b": "", "c": ""},  # dict of variables to set up before question
    ],
    [
        "\nhello(name):\n    print('hello ' + name)\n    return\n",  # background info
        "What's missing?\n a. :\n b. def\n c. '\n",  # question
        ["b"],  # list of required keywords
        {"a": "", "b": "", "c": ""},  # dict of variables to set up before question
    ],
    [
        "\ndef hello(name):\n    print(hello' + name)\n    return\n",  # background info
        "What's missing?\n a. :\n b. def\n c. '\n",  # question
        ["c"],  # list of required keywords
        {"a": "", "b": "", "c": ""},  # dict of variables to set up before question
    ],
]
