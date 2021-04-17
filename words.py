import random

def random_minus_words():
    randint = random.randint(1,5)

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

    return rand_minus_words_result

def random_plus_words():
    randint = random.randint(1,5)

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

    return rand_plus_words_result