# Программа, которая проводит вычисления, связанные с ходами фигуры Конь на шахматной доске
## Создано в рамках практической работы №6 по предмету ВВПД

***

## Функционал скрипта:
- Вычисление минимального количества ходов Коня из одной клетки в другую
- Вычисление минимального количества ходов для встречи двух Коней, находящихся в разных клетках
- Реализованы тесты pytest

***

## Установка и использование:<br>
<code>git clone https://github.com/arud3nko/vvpd6.git</code><br>
<code>python3 main.py</code><br>

***

## Примеры использования:

>Введите начальную клетку (например D6): <br>
>A1<br>
>Введите конечную клетку:<br>
>H6<br>
><br>
>Минимальное кол-во ходов коня из точки A1 в точку H6: 4<br>
>Минимальное кол-во ходов для "встречи" коней, находящихся в точке A1 и в точке H6: 2<br>

***

## Пример функции:

```python
    def knights_collision(first: Tuple[int, int], second: Tuple[int, int]) -> int:
        global counter

        first_mid_results = []
        second_mid_results = []

        counter = 0

        while not set(first_mid_results)&set(second_mid_results):
            counter += 1
            first_mid_results += research(first)
            second_mid_results += research(second)

        return counter
```
***

## ПОДРОБНАЯ ДОКУМЕНТАЦИЯ:

> Страница [GITHUB PAGES](https://arud3nko.github.io/vvpd6/)



Благодарю за уделенное время. Связь со мной: [TELEGRAM](https://t.me/arud3nko)
