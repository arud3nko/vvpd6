points = []  # список целевых клеток
entry = 1


def move(x, y, step=0):
    if step == 1:
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


# Ввод исходной позиции коня на шахматной доске
x0, y0 = list(input('Введите позицию коня: ').upper())
x0 = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}[x0]
y0 = int(y0)

# Получение списка целевых клеток с цифрой вместо буквы
# Координаты клеток изначально реверсированы в целях упрощенной сортировки
move(x0, y0)  # (x0, y0) - исходная позиция

# Удаление дубликатов в списке, сортировка и замена первой цифры буквой от A до H
points = ['ABCDEFGH'[int(point[1]) - 1] + point[0] for point in sorted(set(points), key=lambda point: int(point))]

# Вывод отсортированного списка из целевых клеток
print(*points)

