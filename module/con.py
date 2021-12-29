from typing import Tuple


def move(x, y, step=0):
    """
    Вычисляет возможные ходы фигуры из начальной клетки.
    Принимает аргументы:
        x (int): координата X
        y (int): координата Y
    Необязательный аргумент:
        step (int): количество шагов
    Возвращает:
        points (list): список координат клеток, в которые фигура может попасть из клетки X,Y за step шагов.
    """
    if step == counter:
        points.append(str(y) + str(x))

    else:
        if x > 1 and y > 2: move(x - 1, y - 2, step + 1)
        if x > 2 and y > 1: move(x - 2, y - 1, step + 1)

        if x < 8 and y > 2: move(x + 1, y - 2, step + 1)
        if x < 7 and y > 1: move(x + 2, y - 1, step + 1)

        if x < 7 and y < 8: move(x + 2, y + 1, step + 1)
        if x < 8 and y < 7: move(x + 1, y + 2, step + 1)

        if x > 1 and y < 7: move(x - 1, y + 2, step + 1)
        if x > 2 and y < 8: move(x - 2, y + 1, step + 1)

    return points


def research(entry):
    """
    Запускает функцию move(), получает отформатированный список клеток в которые можно сходить.
    Принимает аргументы:
        entry (Tuple): координаты начальной клетки
    Возвращает:
        points (list): список клеток, в которые фигура может попасть из клетки X,Y.
    """
    global points
    points = []

    x0 = entry[0]
    y0 = entry[1]

    move(x0, y0)  # (x0, y0) - исходная позиция

    points = ['ABCDEFGH'[int(point[1]) - 1] + point[0] for point in sorted(set(points), key=lambda point: int(point))]

    return points


def knight_move(start: Tuple[int, int], finish: str) -> int:
    """
    Запускает функцию research(), пока в списке возможных ходов не появляется конечная клетка.
    Принимает аргументы:
        start (Tuple): кортеж, содержащий координаты начальной клетки X,Y
        finish (str): конечная клетка
    Возвращает:
        counter (int): минимальное количество шагов, через которые фигура окажется в конечной клетке.
    """
    global counter

    mid_results = []
    counter = 0
    while finish not in mid_results:
        counter += 1
        mid_results = research(start)

    return counter


def knights_collision(first: Tuple[int, int], second: Tuple[int, int]) -> int:
    """
    Запускает функцию research(), пока в списках возможных ходов не появляются совпадающие клетки.
    Принимает аргументы:
        first (Tuple): кортеж, содержащий координаты X,Y первой фигуры
        second (Tuple): кортеж, содержащий координаты X,Y второй фигуры
    Возвращает:
        counter (int): минимальное количество шагов, через которые две фигуры окажутся в одной клетке.
    """
    global counter

    first_mid_results = []
    second_mid_results = []

    counter = 0

    while not set(first_mid_results)&set(second_mid_results):
        counter += 1
        first_mid_results += research(first)
        second_mid_results += research(second)

    return counter


def count(start, final):
    """
    Форматирует название клетки в координаты X,Y и запускает функции knight_move(), knights_collision()
    Принимает аргументы:
        start (str): начальная клетка
        final (str): конечная клетка
    Возвращает:
        print(res1, res2):
            res1 (str): мин. кол-во ходов из начальной точки в конечную
            res2 (str): мин. кол-во ходов для встречи двух фигур.
    """

    x0, y0 = list(start)
    x0 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}[x0]
    y0 = int(y0)

    x_f, y_f = list(final)
    x_f = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}[x_f]
    y_f = int(y_f)

    res1 = f'\nМинимальное кол-во ходов коня из точки {start} в точку {final}: {knight_move((x0, y0), final)}\n'
    res2 = f'Минимальное кол-во ходов для "встречи" коней, находящихся ' \
           f'в точке {start} и в точке {final}: {knights_collision((x0, y0), (x_f, y_f))}'

    return print(res1, res2)


def additional():
    """
    Дополнителньая функция, необходимая для корректной работы тестов pytest
    Возвращает:
        counter (int): 1
        points (list): []
    """
    global counter
    global points
    counter = 1
    points = []
    return counter, points
