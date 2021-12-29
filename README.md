# Программа, которая проводит вычисления, связанные с ходами фигуры Конь на шахматной доске
## Создано в рамках практической работы №6 по предмету ВВПД

***

## Функционал скрипта:
- Вычисление минимального количества ходов Коня из одной клетки в другую
- Вычисление минимального количества ходов для встречи двух Коней, находящихся в разных клетках

***

## Установка и использование:<br>
<code>git clone https://github.com/arud3nko/vvpd6.git</code><br>
<code>apt-get install tesseract-ocr</code><br>
<code>pip3 install -r requirements.txt</code><br>
<code>python3 start.py</code><br>
<code>http://localhost:5000/</code><br>
<br>
Загрузить chromedriver для вашей системы: <code>https://chromedriver.chromium.org/downloads</code>

Для корректной работы скрипта необходимо настроить <b>options.py</b>:<br>
<code>pytesseract.pytesseract.tesseract_cmd = 'tesseract'</code> - Команда для вызова Tesseract<br>
<code>path_driver = './chromedriver'</code> - Путь к chromedriver<br>
<code>from_mail = 'noreply@your.mail'</code> - Адрес, с которого будем отправлять документ<br>
<code>from_passwd = 'yourcoolpassword'</code> - Пароль<br>
<code>smtp_server = 'smtp.yandex.ru'</code> - SMTP сервер<br>
<code>smtp_port = '465'</code> - Порт<br>

<br>

У проекта огромный todo-лист, буду им заниматься ;)<br>
Благодарю за уделенное время. Мой Telegram: <i>@arud3nko</i>
