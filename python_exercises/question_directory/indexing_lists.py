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


def dictify(my_list, my_list_name):
    my_dict = {item: item for item in my_list}
    my_dict[my_list_name] = my_list
    my_dict["y"] = "y"
    my_dict["n"] = "n"
    return my_dict


spam = ["cat", "bat", "rat", "elephant"]
background_spam = f"spam = {spam}"
dict_spam = dictify(spam, "spam")

company_hqs = [["IBM", "Facebook", "Google"], ["Armonk, NY", "Menlo Park, CA", "Mountain View, CA"]]
background_company_hqs = f"company_hqs = {company_hqs}"
dict_company_hqs = dictify(company_hqs[0] + company_hqs[1], "company_hqs")
dict_company_hqs["company_hqs"] = company_hqs

letters = ["a", "b", "c", "x", "y", "z"]
background_letters = f"letters = {letters}"
dict_letters = dictify(letters, "letters")

BLURB = ""
TASKS = [
    [
        background_spam,  # background info
        "What would you expect this to give back?\nspam[0]?\n\n",  # question
        ["cat"],  # list of required keywords
        dict_spam,  # dict of variables to set up before question
    ],
    [
        background_spam,  # background info
        "How would you get 'rat' back from spam? \n\n",  # question
        ["spam[2]"],  # list of required keywords
        dict_spam,  # dict of variables to set up before question
    ],
    [
        background_spam,  # background info
        "Does this work? (y/n)\nspam[1.0] \n\n",  # question
        ["n"],  # list of required keywords
        dict_spam,  # dict of variables to set up before question
    ],
    [
        background_company_hqs,  # background info
        "How would you get 'Menlo Park, CA' back from this list of lists? \n\n",  # question
        ["company_hqs[1][1]"],  # list of required keywords
        dict_company_hqs,  # dict of variables to set up before question
    ],
    [
        background_letters,  # background info
        "How would you find out the length of this list? \n\n",  # question
        ["len(letters)"],  # list of required keywords
        dict_letters,  # dict of variables to set up before question
    ],
    [
        background_letters,  # background info
        "How would you slice this list to get back just ['b','c']? \n\n",  # question
        ["letters[1:3]"],  # list of required keywords
        dict_letters,  # dict of variables to set up before question
    ],
    [
        background_letters,  # background info
        "If you don't want to count all the elements in this list, how would you get back the letter 'z'? \n(Clue: it's the last letter in the list and there's a special way to do this) \n\n",  # question
        ["letters[-1]"],  # list of required keywords
        dict_letters,  # dict of variables to set up before question
    ],
]
