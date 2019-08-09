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

BLURB = (
    "\nLesson 2 - Warm Up Exercise\n\n(Feel free to look back over the slides/use Google if you need help on this)\n"
)

TASKS = [
    [
        "",  # background info
        "Subtract one number from another\n\n",  # question
        ["-"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "Divide one number by the other\n\n",  # question
        ["/"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "Write a line of code which will display a string to the terminal\n\n",  # question
        ["print"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "Write a line of code which will display a string to the terminal\n\n",  # question
        ["print"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "Find out how many characters there are in your first name\n\n",  # question
        ["len"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        "Check if two values are equal to each other\n\n",  # question
        ["=="],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
]
