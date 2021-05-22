import random

def random_minus_words():

    minus_words_list = [' залил соляры ', ' солярнул ', ' засолил ', ' негодует от ', ' минусанул ', ' попустил ', ' облил мочой ', ' заговнил ', ' потянул на дно ']

    rand_minus_words_result = random.choice(minus_words_list)

    return rand_minus_words_result

def random_plus_words():

    plus_words_list = [' залил рофлан ', ' рофланул с ', ' зарофланил ', ' одобряет ', ' плюсанул ', ' дал рофлан ', ' поддержал ', ' дал рофл ']

    rand_plus_words_result = random.choice(plus_words_list)

    return rand_plus_words_result