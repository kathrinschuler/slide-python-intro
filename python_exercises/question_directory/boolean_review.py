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
        "Write a statement to check if two numbers are equal to each other?\n\n",  # question
        ["=="],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "\nwifi_available = False\nmobile_data_available = False",  # background info
        "What would the output of this statement be?\nwifi_available and mobile_data_available\n",  # question
        ["False"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "\nwifi_available = False\nmobile_data_available = True",  # background info
        "What would the output of this statement be?\nwifi_available or mobile_data_available\n\n",  # question
        ["True"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "\nmobile_data_available = True",  # background info
        "What would the output of this statement be?\nnot mobile_data_available\n\n",  # question
        ["False"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
    [
        "\nwifi_available = False\nmobile_data_available = True",  # background info
        "What would the output of this be\n\nif wifi_available or mobile_data_available:\n     print(True)\n",  # question
        ["True"],  # list of required keywords
        {},  # dict of variables to set up before question
    ],
]
