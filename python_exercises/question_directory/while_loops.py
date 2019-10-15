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

BLURB = "While loops"
TASKS = [
    [
        "",  # background info
        """How many times will the following loop print 'spam':
        count = 1
        while count <= 5:
            count = count + 1
            print("spam")""",  # question
        ["5"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        """What word is missing if you want spam to be written only twice?
        count = 1
        while count <= 5:
            count = count + 1
            print("spam")
            if count == 3:
            __________""",  # question
        ["break"],  # list of required keywords
        {"no_eval": True, "no_exec": True},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        """What word is missing if you want to skip 'spam 3' ?
        count = 1
        while count <= 5:
            count = count + 1
            if count == 3:
            __________
        print("spam " + str(count))""",  # question
        ["continue"],  # list of required keywords
        {"no_eval": True, "no_exec": True},  # dict of variables to set up before question
    ],
    [
        "",  # background info
        """What does the user need to type to make the code exit this loop?
        while True:
            password = input()
            if password != 'hacking':
                continue
            if password == 'swordfish':
                break""",  # question
        ["swordfish"],  # list of required keywords
        {"no_eval": True, "no_exec": True},  # dict of variables to set up before question
    ],
]
