"""
Press run above to start
"""

if input("\n\nPress enter to start\n") != "test":
    from exercises.question_runner import run

    # LESSON ONE
    # https://kathrinschuler.github.io/slide-python-intro/#/10/3
    from question_directory.equality_and_booleans import TASKS, BLURB
    from question_directory.greater_than_less_than_and_booleans import TASKS, BLURB

    # https://kathrinschuler.github.io/slide-python-intro/#/11/4
    from question_directory.variables_equality_and_booleans import TASKS, BLURB
    from question_directory.boolean_operators import TASKS, BLURB

    # LESSON TWO
    # No repl exercises for lesson 2

    # LESSON THREE
    # https://kathrinschuler.github.io/slide-python-intro/#/25/4
    from question_directory.functions import TASKS, BLURB

    run(TASKS, BLURB)

else:
    from unit_tests.test_instructor_code import *  # noqa

    if __name__ == "__main__":
        unittest.main()  # noqa
