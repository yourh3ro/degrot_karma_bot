import random

def random_minus_words():
    randint = random.randint(1,9)

    if randint == 1:
        rand_minus_words_result = ' залил соляры '
    elif randint == 2:
        rand_minus_words_result = ' солярнул '
    elif randint == 3:
        rand_minus_words_result = ' засолил '
    elif randint == 4:
        rand_minus_words_result = ' негодует от '
    elif randint == 5:
        rand_minus_words_result = ' минусанул '
    elif randint == 6:
        rand_minus_words_result = ' попустил '
    elif randint == 7:
        rand_minus_words_result = ' облил мочой '
    elif randint == 8:
        rand_minus_words_result = ' заговнил '
    elif randint == 9:
        rand_minus_words_result = ' потянул на дно '

    return rand_minus_words_result

def random_plus_words():
    randint = random.randint(1,8)

    if randint == 1:
        rand_plus_words_result = ' залил рофлан '
    elif randint == 2:
        rand_plus_words_result = ' рофланул с '
    elif randint == 3:
        rand_plus_words_result = ' зарофланил '
    elif randint == 4:
        rand_plus_words_result = ' одобряет '
    elif randint == 5:
        rand_plus_words_result = ' плюсанул '
    elif randint == 6:
        rand_plus_words_result = ' позитивнул '
    elif randint == 7:
        rand_plus_words_result = ' поддержал '
    elif randint == 8:
        rand_plus_words_result = ' законтачил с '

    return rand_plus_words_result