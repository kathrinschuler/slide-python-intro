from collections import namedtuple
from time import sleep

def ennumerate_task_list(task_list):
    for i, value in enumerate(task_list, 0):
        task_list[i].insert(0, i + 1)
    return task_list


def question_tuple_maker(q_num, info, question, answer, prerequisites):
    Task = namedtuple("Task", ["q_num", "info", "question", "answer", "prerequisites"])
    task = Task(q_num, info, question, answer, prerequisites)
    return task


def create_question_list(ennumerated_tasks):
    list_of_remaining_questions = []
    for task_data in ennumerated_tasks:
        task_tuple = question_tuple_maker(task_data[0], task_data[1], task_data[2], task_data[3], task_data[4])
        list_of_remaining_questions.append(task_tuple)
    return list_of_remaining_questions


def _get_input():
    return input()


def run_all_questions(list_of_remaining_questions):
    remove_list = []
    for task_tuple in list_of_remaining_questions:
        print(task_tuple.info)
        print(f"{task_tuple.q_num}. {task_tuple.question}")
        answer_to_question = _get_input()
        user_output = get_output_for_user(answer_to_question, task_tuple)
        was_correct_answer = is_correct_answer(task_tuple, answer_to_question, user_output)
        if was_correct_answer:
            remove_list.append(task_tuple)
        print(_print_correct_or_incorrect(user_output, was_correct_answer))
        sleep(.5)
    for i in remove_list:
        list_of_remaining_questions.remove(i)
    return list_of_remaining_questions


def is_correct_answer(task_tuple, answer_to_question, user_output=None):
    keywords = task_tuple.answer
    keywords = [standardise_string(keyword) for keyword in keywords]
    was_correct_answer = False
    if answer_to_question and (not user_output or not "Error" in user_output):
        answer_to_question = standardise_string(answer_to_question)
        was_correct_answer = all(keyword in answer_to_question for keyword in keywords)
    return was_correct_answer


def standardise_string(string):
    if not string:
        return string
    return string.replace("'", '"')


def get_output_for_user(answer_to_question, task_tuple):
    user_output = None
    try:
        user_output = (
            exec(answer_to_question, task_tuple.prerequisites)
            if _run_exec(answer_to_question)
            else eval(answer_to_question, task_tuple.prerequisites)
        )
        user_output = str(user_output)
    except Exception as e:
        user_output = f"Error message: {e}"
    if not answer_to_question:
        user_output = None
    return user_output


def _print_correct_or_incorrect(user_output, was_correct_answer):
    print_this = ""
    if user_output and user_output != "None":
        print_this += f"=> {user_output}"
    if was_correct_answer:
        print_this += "\nCorrect\n"
    else:
        print_this += "\nIncorrect\n"
    return print_this


def _run_exec(answer_to_question):
    return ("=" in answer_to_question) or ("del" in answer_to_question)
