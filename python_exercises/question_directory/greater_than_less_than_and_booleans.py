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

BLURB = ""
TASKS = [
    [
        "",  # background info
        "42 < 100\n",  # question
        ["True"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "42 > 100\n",  # question
        ["False"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "42 < 42\n",  # question
        ["False"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "my_number = 42",  # background info
        "my_number <= 42\n",  # question
        ["True"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "my_age = 29",  # background info
        "my_age >= 10\n",  # question
        ["True"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
]
