from typing import Tuple


def move(x, y, step=0):
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


def research(entry):
    global points
    points = []

    x0 = entry[0]
    y0 = entry[1]

    move(x0, y0)  # (x0, y0) - исходная позиция

    points = ['ABCDEFGH'[int(point[1]) - 1] + point[0] for point in sorted(set(points), key=lambda point: int(point))]

    return points


def knight_move(start: Tuple[int, int], finish: str) -> int:
    global counter

    mid_results = []
    counter = 0
    while finish not in mid_results:
        counter += 1
        mid_results = research(start)

    return counter


def knights_collision (first: Tuple[int, int], second: Tuple[int, int]) -> int:
    global counter

    first_mid_results = []
    second_mid_results = []

    counter = 0

    while not set(first_mid_results)&set(second_mid_results):
        counter += 1
        first_mid_results += research(first)
        second_mid_results += research(second)

    # print(f'Совпадение в клетке{set(first_mid_results)&set(second_mid_results)}')

    return counter


def main():

    start = input('Введите начальную клетку (например D6):\n')
    final = input('Введите конечную клетку:\n')

    x0, y0 = list(start)
    x0 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}[x0]
    y0 = int(y0)

    x_f, y_f = list(final)
    x_f = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}[x_f]
    y_f = int(y_f)

    print(f'Минимальное кол-во ходов коня из точки {start} в точку {final}: {knight_move((x0, y0), final)}\n')
    print(f'Минимальное кол-во ходов для "встречи" коней, находящихся '
          f'в точке {start} и в точке {final}: {knights_collision((x0, y0), (x_f, y_f))}')


if __name__ == '__main__':
    main()
