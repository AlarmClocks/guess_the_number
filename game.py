"""
Игра угадай число
Компьютер сам загадывает и сам угадывает число

УСЛОВИЯ ЗАДАНИЯ
Компьютер загадывает целое число от 1 до 100, 
и нам его нужно угадать. 
Под «угадать» подразумевается 
«написать программу, которая угадывает число».
Алгоритм учитывает информацию о том, 
больше или меньше случайное число нужного нам числа.

??? Представлен шаблон baseline из скринкаста.

МЕТРИКА КАЧЕСТВА
Результаты оцениваются по среднему кол.попыток при 1000 попыток. 
Необходимо добиться минимального количества попыток.

ЧТО ПРАКТИКУЕМ
Учимся писать хороший код на Python.
Учимся работать с IDE.
Учимся работать с GitHub.

"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """ угадываем число в диапазоне от 1 до 100

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # count = 0 # счетчик попыток поиска
    start_num = 1 # начальное число диапазона поиска
    stop_num = 101 # конечное число диапазона поиска
    for count in range(start_num, stop_num):
        # count += 1
        predict_number = int((start_num + stop_num)/2) 
        # предполагаемое число
        # print(f'        def random_predic({number})     predict_number={predict_number}      start_num={start_num}  stop_num={stop_num}')
        
        if number == predict_number:
            # print(f'    def random_predic({number}) найдено за {count} шагов(попыток)')
            break  # выход из цикла если угадали
        elif number > predict_number:
            # загаданное число БОЛЬШЕ предполагаемого числа
            # будем искать в "верхнем" диапазоне
            start_num = predict_number + 1
        else:
            # загаданное число МЕНЬШЕ предполагаемого числа
            # будем искать в "нижнем" диапазоне
            stop_num = predict_number - 1
  
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # сюда будем сохранять КолПопытокНахождения загаданного числа
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    # print(f'Список из 100 загаданных компом чисел {random_array} ')

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    count = len(count_ls)
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    print(f"Всего загадано {count} числел (до 1 до 100) и среднее количестов попыток на отгадывание = {score}.")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
