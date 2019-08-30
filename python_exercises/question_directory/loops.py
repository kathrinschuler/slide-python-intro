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
        """How many times will the following loop print 'spam'?

            for i in range(5):
            \tprint('spam')

        """,  # question
        ["5"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        """
            What does this loop print (provide a list of values separated by spaces)?

            for i in range(5):
            \tprint(i*2)

        """,  # question
        ["0, 2, 4, 6, 8"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        """
            What does this loop print (provide a list of values separated by spaces)?

            for i in range(20, 28, 2):
            \tprint(i)

        """,  # question
        ["20, 22, 24, 26"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        """
            What does this loop print (provide a list of values separated by spaces)?

            for i in range(5, 1, -1):
            \tprint(i)

        """,  # question
        ["5, 4, 3, 2"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
]
