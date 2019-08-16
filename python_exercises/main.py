"""
Press run above to start
"""

from exercises.question_runner import run
from question_directory import (
    boolean_operators,
    equality_and_booleans,
    functions,
    greater_than_less_than_and_booleans,
    inbuilt_functions_and_operators,
    lists,
    variables_equality_and_booleans,
)
from unit_tests.test_instructor_code import *  # noqa

if input("\n\nPress enter to start\n") != "test":
    # LESSON ONE
    # https://kathrinschuler.github.io/slide-python-intro/#/10/3
    run(equality_and_booleans.TASKS, equality_and_booleans.BLURB)
    run(greater_than_less_than_and_booleans.TASKS, greater_than_less_than_and_booleans.BLURB)

    # https://kathrinschuler.github.io/slide-python-intro/#/11/4
    run(variables_equality_and_booleans.TASKS, variables_equality_and_booleans.BLURB)
    run(boolean_operators.TASKS, boolean_operators.BLURB)

    # LESSON TWO
    run(inbuilt_functions_and_operators.TASKS, inbuilt_functions_and_operators.BLURB)

    # LESSON THREE
    # https://kathrinschuler.github.io/slide-python-intro/#/25/4
    run(functions.TASKS, functions.BLURB)

    # LESSON FOUR
    run(lists.TASKS, lists.BLURB)

else:
    if __name__ == "__main__":
        unittest.main()  # noqa
