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

    x0, y0 = list(entry)
    x0 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}[x0]
    y0 = int(y0)

    move(x0, y0)  # (x0, y0) - исходная позиция

    points = ['ABCDEFGH'[int(point[1]) - 1] + point[0] for point in sorted(set(points), key=lambda point: int(point))]

    return points


# def knight_move (start: Tuple[int, int], finish: Tuple[int, int]) -> int:
#

def main():
    global counter

    start_point = 'D6'
    final_point = 'F2'
    mid_results = []
    counter = 0
    while final_point not in mid_results:
        counter += 1
        mid_results = research(start_point)

    print(counter)


if __name__ == '__main__':
    main()