from module.con import count


def main():
    """
    Принимает аргументы:
            start (str): начальная клетка
            final (str): конечная клетка
    Возвращает:
        Вызов функции count, которая находится в пакете module в модуле con.py.
    """
    start = input('Введите начальную клетку (например D6):\n')
    final = input('Введите конечную клетку:\n')
    count(start, final)


if __name__ == '__main__':
    main()