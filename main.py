from module.con import count


def main():
    start = input('Введите начальную клетку (например D6):\n')
    final = input('Введите конечную клетку:\n')
    count(start, final)


if __name__ == '__main__':
    main()