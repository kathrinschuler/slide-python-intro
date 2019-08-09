# Slide link: https://kathrinschuler.github.io/slide-python-intro/#/11/4
# Current repl: https://repl.it/@kathrinschuler/Lesson1ExBooleanOperators - question text varies a little

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

BLURB = "\nLesson 2 - Exercise 2\n\
\nImagine you've got clients who are interested in the share prices of Google and Facebook.\nThe variables we're using for these questions will be:\ngoogle_up\nfacebook_up\nFor each question the respective values of google_up and facebook_up will either be True or False. Keep an eye on their values (set before each question is asked) in order to get the right anwers."

TASKS = [
    [
        "\ngoogle_up = False\nfacebook_up = False\n",  # background info
        "What would the output of this statement be now?\n\ngoogle_up and facebook_up\n",  # question
        ["False"],  # list of required keywords
        {"google_up": False, "facebook_up": False},  # dict of variables to set up before question
    ],
    [
        "\ngoogle_up = False\nfacebook_up = False\n",  # background info
        "How about this statement now?\n\ngoogle_up or facebook_up\n",  # question
        ["False"],  # list of required keywords
        {"google_up": False, "facebook_up": False},  # dict of variables to set up before question
    ],
    [
        "\ngoogle_up = False\nfacebook_up = False\n",  # background info
        "And this one?\n\nnot google_up\n",  # question
        ["True"],  # list of required keywords
        {"google_up": False, "facebook_up": False},  # dict of variables to set up before question
    ],
    [
        "\ngoogle_up = False\nfacebook_up = True\n",  # background info
        "What result do you expect from this statement? \ngoogle_up and facebook_up\n (Note that we've changed the values assigned to google_up and facebook_up above)\n",  # question
        ["False"],  # list of required keywords
        {"google_up": False, "facebook_up": True},  # dict of variables to set up before question
    ],
    [
        "\ngoogle_up = False\nfacebook_up = True\n",  # background info
        "What result do you expect from this statement? \ngoogle_up or facebook_up\n",  # question
        ["True"],  # list of required keywords
        {"google_up": False, "facebook_up": True},  # dict of variables to set up before question
    ],
    [
        "\ngoogle_up = False\nfacebook_up = True\n",  # background info
        "not facebook_up\n",  # question
        ["False"],  # list of required keywords
        {"google_up": False, "facebook_up": True},  # dict of variables to set up before question
    ],
]
