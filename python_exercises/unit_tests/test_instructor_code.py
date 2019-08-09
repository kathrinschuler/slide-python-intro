from exercises.helpers import (
    is_correct_answer,
    ennumerate_task_list,
    question_tuple_maker,
    standardise_string,
    create_question_list,
    run_all_questions,
    get_output_for_user,
)
from exercises.question_runner import run, _bonus
from collections import namedtuple
import unittest
from unittest import mock
from question_directory.lesson4ex2 import TASKS as tasks, BLURB as blurb


class Tests(unittest.TestCase):
    # SETUP

    clothes = ["shirt", "trousers", "blouse", "socks", "leggings", "shorts"]

    shoes = ["sneakers", "heels", "flip-flops"]

    raw_task_list = [
        ["", "type a\n\n", ["a"], {"a": 1}],
        ["", 'type "b"\n\n', ["b"], {"b": 2}],
        ["", 'type "c"\n\n', ["c"], {"c": 3}],
    ]

    enumerated_task_list = [
        [1, "instructions", "question", ["a", "b"], {"a": "a", "b": "b"}],
        [2, "instructions", "question", ["c", "d"], {"c": "c", "d": "d"}],
    ]

    Task = namedtuple("Task", ["q_num", "info", "question", "answer", "prerequisites"])

    task_tuple_a = Task(
        q_num=1, info="instructions", question="question", answer=["a", "b"], prerequisites={"a": "a", "b": "b"}
    )

    task_tuple_b = Task(
        q_num=2, info="instructions", question="question", answer=["c", "d"], prerequisites={"c": "c", "d": "d"}
    )

    real_question_1 = Task(
        q_num=1,
        info="instructions",
        question="Can you change the third element to be 'jacket' instead?\n\n",
        answer=["clothes", "2", "'jacket'"],
        prerequisites={"clothes": clothes},
    )

    real_question_2 = Task(
        q_num=1,
        info="instructions",
        question="Can you remove the second element from the list?\n\n",
        answer=["del", "clothes", "[1]"],
        prerequisites={"clothes": clothes},
    )

    real_question_3 = Task(
        q_num=1,
        info="instructions",
        question="Can you mutiply this list by 5?\n",
        answer=["shoes", "*", "5"],
        prerequisites={"shoes": shoes},
    )

    list_of_remaining_questions = [task_tuple_a, task_tuple_b]

    real_list_of_remaining_questions = [real_question_1, real_question_2]

    def test_ennumerate_task_list(self):
        # GIVEN
        task_list = [[], [], [], []]

        # WHEN
        expected = [[1], [2], [3], [4]]
        actual = ennumerate_task_list(task_list)

        # THEN
        self.assertEqual(expected, actual)

    def test_question_tuple_maker(self):
        # GIVEN

        # WHEN
        expected = self.Task(
            q_num=1, info="instructions", question="question", answer=["a", "b"], prerequisites="prerequisites"
        )
        actual = question_tuple_maker(1, "instructions", "question", ["a", "b"], "prerequisites")

        # THEN
        self.assertEqual(expected, actual)

    def test_create_question_list(self):
        # WHEN
        expected = self.list_of_remaining_questions
        actual = create_question_list(self.enumerated_task_list)

        # THEN
        self.assertEqual(expected, actual)

    @mock.patch("exercises.helpers._get_input", side_effect=[0, 1])
    def test_run_all_questions(self, _get_input_mock):
        # GIVEN
        run_all_questions(self.list_of_remaining_questions)

        # THEN
        _get_input_mock.assert_called_with()

    @mock.patch("exercises.helpers._get_input", side_effect=["clothes[2]='jacket'", "del clothes[1]"])
    def test_run_all_questions_with_real_answers_all_correct(self, _get_input_mock):
        # WHEN
        expected = []
        actual = run_all_questions(self.real_list_of_remaining_questions)

        # THEN
        self.assertEqual(expected, actual)

    @mock.patch("exercises.helpers._get_input", side_effect=["z", "del clothes[1]"])
    def test_run_all_questions_with_real_answer_one_right(self, _get_input_mock):
        # WHEN
        expected = [self.real_question_1]
        actual = run_all_questions(self.real_list_of_remaining_questions)

        # THEN
        self.assertEqual(expected, actual)

    @mock.patch("exercises.helpers._get_input", side_effect=[None, "y"])
    def test_run_all_questions_with_real_answer_all_wrong(self, _get_input_mock):
        # WHEN
        expected = self.real_list_of_remaining_questions
        actual = run_all_questions(self.real_list_of_remaining_questions)

        # THEN
        self.assertEqual(expected, actual)

    def test_check_fail(self):
        # WHEN
        answer_to_question = "xyz"

        # THEN
        self.assertFalse(is_correct_answer(self.task_tuple_a, answer_to_question))

    def test_check_pass(self):
        # WHEN
        answer_to_question = "a + b"

        # THEN
        self.assertTrue(is_correct_answer(self.task_tuple_a, answer_to_question))

    def test_check_pass_del(self):
        # GIVEN
        clothes = ["shirt", "trousers", "blouse", "socks", "leggings", "shorts"]
        keywords = ["del", "clothes", "[1]"]
        prerequisites = {"clothes": clothes}

        task_tuple = self.Task(
            q_num=1, info="instructions", question="question", answer=keywords, prerequisites=prerequisites
        )

        # WHEN
        answer_to_question = "del clothes[1]"

        # THEN
        self.assertTrue(is_correct_answer(task_tuple, answer_to_question))

    def test_check_fail_no_answer(self):
        # GIVEN
        clothes = ["shirt", "trousers", "blouse", "socks", "leggings", "shorts"]
        keywords = ["del", "clothes", "[1]"]
        prerequisites = {"clothes": clothes}

        task_tuple = self.Task(
            q_num=1, info="instructions", question="question", answer=keywords, prerequisites=prerequisites
        )

        # WHEN
        answer_to_question = None

        # THEN
        self.assertFalse(is_correct_answer(task_tuple, answer_to_question))

    def test_check_fail_no_answer_no_exception(self):
        # GIVEN
        clothes = ["shirt", "trousers", "blouse", "socks", "leggings", "shorts"]
        keywords = ["del", "clothes", "[1]"]
        prerequisites = {"clothes": clothes}

        # WHEN
        task_tuple = self.Task(
            q_num=1, info="instructions", question="question", answer=keywords, prerequisites=prerequisites
        )

        answer_to_question = None

        # THEN
        try:
            is_correct_answer(task_tuple, answer_to_question)
        except Exception as e:
            print(e)
            self.fail("is_correct_answer() raised exception on answer_to_question = None")

    def test_check_pass_double_quotes(self):
        # GIVEN
        clothes = ["a", "b", "c"]
        keywords = ["clothes", "2", "'jacket'"]
        prerequisites = {"clothes": clothes}

        # WHEN
        task_tuple = self.Task(q_num=1, info="", question="", answer=keywords, prerequisites=prerequisites)

        answer_to_question = 'clothes[2] = "jacket"'

        # THEN
        self.assertTrue(is_correct_answer(task_tuple, answer_to_question))

    def test_standardise_string_quotes(self):
        # GIVEN
        string = "'x'"

        # WHEN
        expected = '"x"'
        actual = standardise_string(string)

        # THEN
        self.assertEqual(expected, actual)

    def test_standardise_string_none(self):
        # GIVEN
        string = None

        # WHEN
        expected = None
        actual = standardise_string(string)

        # THEN
        self.assertEqual(expected, actual)

    def test_get_output_for_user(self):
        # GIVEN
        answer_to_question = "shoes * 5"

        # WHEN
        expected = "['sneakers', 'heels', 'flip-flops', 'sneakers', 'heels', 'flip-flops', 'sneakers', 'heels', 'flip-flops', 'sneakers', 'heels', 'flip-flops', 'sneakers', 'heels', 'flip-flops']"
        actual = get_output_for_user(answer_to_question, self.real_question_3)

        # THEN
        self.assertEqual(expected, actual)

    def test_get_output_for_user_exception(self):
        # GIVEN
        answer_to_question = "z"

        # WHEN
        expected = "Error message: name 'z' is not defined"
        actual = get_output_for_user(answer_to_question, self.real_question_3)

        # THEN
        self.assertEqual(expected, actual)

    def test_get_output_for_user_none(self):
        # GIVEN
        answer_to_question = None

        # WHEN
        expected = None
        actual = get_output_for_user(answer_to_question, self.real_question_3)

        # THEN
        self.assertEqual(expected, actual)

    def test_bonus_looks_okay(self):
        # THEN
        _bonus()
        self.assertTrue(True)  # it's a hack, but replace True with False to see what bonus looks like in the output

    @mock.patch(
        "exercises.helpers._get_input",
        side_effect=[
            "clothes[2] = 'jacket'",
            "clothes[-1] = 'hat'",
            "clothes[-2] = clothes[0]",
            "clothes.append('jumper')",
            "clothes = clothes + shoes",
            "shoes * 5",
            "clothes.remove('socks')",
            "del clothes[1]",
        ],
    )
    @mock.patch("exercises.question_runner._bonus", bonus="")
    def test_run(self, mock_bonus, mock_get_input):
        # GIVEN
        run(tasks, blurb)

        # THEN
        assert mock_bonus.called_once_with()

    @mock.patch("exercises.question_runner._bonus", bonus="")
    @mock.patch("exercises.helpers._get_input", side_effect=["a", "b", "c"])
    def test_run_shorter_tasks(self, mock_get_input, mock_bonus):

        # GIVEN
        tasks = [
            ["", "type a\n\n", ["a"], {"a": 1}],
            ["", 'type "b"\n\n', ["b"], {"b": 2}],
            ["", 'type "c"\n\n', ["c"], {"c": 3}],
        ]
        blurb = "This is a test run"
        run(tasks, blurb)

        # THEN
        assert mock_bonus.called_once_with()
        self.assertTrue(True)  # hacky, but set True to False to see what the output looks like
