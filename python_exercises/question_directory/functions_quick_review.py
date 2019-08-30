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


def hello_world():
    print("hello world")


BLURB = ""
TASKS = [
    [
        "\ndef hello_world():\n     print('hello world')\n\n",  # background info
        "How would you call this function?\n\n",  # question
        ["hello_world()"],  # list of required keywords
        {"hello_world": hello_world},  # dict of variables to set up before question
    ],
    [
        "\ndef hello_world():\n     print('hello world')\n\n",  # background info
        "What is this? \na) function\nb) function call\n",  # question
        ["a"],  # list of required keywords
        {"a": "a", "b": "b"},  # dict of variables to set up before question
    ],
]
