# Slide link: https://kathrinschuler.github.io/slide-python-intro/#/10/3

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

BLURB = "\nLesson 1 - Exercise 1\n\n(Feel free to look back over the slides/use Google if you need help on this)\n Guess what the output of these statements will be (clue, either True or False)\n"

TASKS = [
    [
        "",  # background info
        "42 == 42\n",  # question
        ["True"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "42 == 99\n",  # question
        ["False"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "2 != 3\n",  # question
        ["True"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "2 != 2\n",  # question
        ["False"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "'hello' == 'hello'\n",  # question
        ["True"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "'hello' == 'Hello'\n",  # question
        ["False"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "'dog' != 'cat'\n",  # question
        ["True"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "True != False\n",  # question
        ["True"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "42 == 42.0\n",  # question
        ["True"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "42 == '42'\n",  # question
        ["False"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
]
