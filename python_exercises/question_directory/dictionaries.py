from pprint import pformat

company_hqs = {
    "IBM": "Armonk, NY",
    "Facebook": "Menlo Park, CA",
    "Google": "Mountain View, CA",
    "Twitter": "San Francisco, CA",
    "Hewlett Packard": "Palo Alto, CA",
}
company_hqs_background = f"company_hqs = {pformat(company_hqs)}"

BLURB = ""
TASKS = [
    [
        company_hqs_background,  # background info
        "How would you get the location of Google's offices from this dictionary?\n\n",  # question
        ["company_hqs[", "Google", "]"],  # list of required keywords
        {"company_hqs": company_hqs},  # dict of variables to set up before question
    ],
    [
        company_hqs_background,  # background info
        "How would you get just the keys from this dictionary?\n\n",  # question
        [".keys()"],  # list of required keywords
        {"company_hqs": company_hqs},  # dict of variables to set up before question
    ],
    [
        company_hqs_background,  # background info
        "Can you add Amazon to the dictionary? It's based in Seattle, WA\n\n",  # question
        ["company_hqs[", "Amazon", "]", "=", "Seattle, WA'"],  # list of required keywords
        {"company_hqs": company_hqs},  # dict of variables to set up before question
    ],
]
