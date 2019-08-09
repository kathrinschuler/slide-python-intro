# Slide link: https://kathrinschuler.github.io/slide-python-intro/#/11/4

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
        "Write one line of code using a Boolean operator (and, or, not) which will display True if Google's price is up and Facebook's price is up, and False if not\n",  # question
        ["google", "facebook", "and"],  # list of required keywords
        {"google_up": True, "facebook_up": True},  # dict of variables to set up before question
    ],
    [
        "\ngoogle_up = True\nfacebook_up = True\n",  # background info
        "A client wants to know if the share price of Google or Facebook rises\nHow would you write code to check for this?\nRemember, it *must* include a Boolean operator (and, or, not)\n",  # question
        ["google", "facebook", "or"],  # list of required keywords
        {"google_up": True, "facebook_up": True},  # dict of variables to set up before question
    ],
    [
        "\ngoogle_up = True\nfacebook_up = True\n",  # background info
        "Another client wants to know if Google's share price hasn't risen that day and doesn't mind what Facebook did that day.\n\nSome ways to do this would be to write\ngoogle_up == False\ngoogle_up != True\nCan you find another way?\n",  # question
        ["google", "not"],  # list of required keywords
        {"google_up": True, "facebook_up": True},  # dict of variables to set up before question
    ],
]
