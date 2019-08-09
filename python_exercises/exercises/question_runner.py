from time import sleep
from exercises.helpers import run_all_questions, create_question_list, ennumerate_task_list


def run(tasks, blurb):
    print(blurb)
    word_num = len(blurb)
    fraction_of_second_to_read_each_word = 0.025
    sleep_len = word_num * fraction_of_second_to_read_each_word
    sleep(sleep_len)
    list_of_remaining_questions = run_all_questions(create_question_list(ennumerate_task_list(tasks)))

    while list_of_remaining_questions:
        print(f"You got {len(tasks) - len(list_of_remaining_questions)}/{len(tasks)} questions right\n")
        if not _user_wants_to_retry_quiz():
            print("\nGame Over\n\n")
            exit()
        else:
            list_of_remaining_questions = run_all_questions(list_of_remaining_questions)

    print(f"You got {len(tasks)}/{len(tasks)} questions right\n")
    _bonus()


def _bonus():
    print("Congratulations on passsing the quiz!!!")
    print(
        """
                                    .''.
        .''.      .        *''*    :_\\/_:     .
       :_\\/_:   _\\(/_  .:.*_\\/_*   : /\\:  .'.:.'.
   .''.: /\\ :   ./)\\   ':'* /\\ * :  '..'.  -=:o:=-
  :_\\/_:'.:::.    ' *''*    * '.\\'/.' _\\(/_'.':'.'
  : /\\ : :::::     *_\\/_*     -= o =-  /)\\    '  *
   '..'  ':::'     * /\\ *     .'/.\\'.   '
       *            *..*         :
    """
    )
    print("\n\n")


def _user_wants_to_retry_quiz():
    ans = input("Do you want to try the questions you got wrong again? (y/n)\n")
    retry = _answer_only_y_or_n(ans)
    if not retry:
        sure = input("Are you sure you want to quit the quiz? (y/n)\n")
        retry = not _answer_only_y_or_n(sure)
    return retry


def _answer_only_y_or_n(y_n_answer):
    y_n = {"Y": True, "N": False}
    while y_n_answer.upper() != "Y" and y_n_answer.upper() != "N":
        y_n_answer = input("Please enter y or n\n")
    return y_n[y_n_answer.upper()]
