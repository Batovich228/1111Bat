import logging

# logging.basicConfig(level=logging.DEBUG)
#
# logging.debug("debug")
# logging.info("debug")
# logging.warning("debug")
# logging.error("debug")
# logging.critical("debug")

# DEBUG	 Найнижчий рівень налаштування. Найчастіше використовується розробниками бібліотек.
# INFO  Рівень інформування. Він створений для надання повідомлень про коректну роботу складників програми.
# WARNING Рівень застережень, які повідомляють користувачу про можливу неправильну роботу програми або надають важливу інформацію.
# ERROR Рівень помилок, які сповіщають про неправильну роботу функції або частини коду програми.
# CRITICAL Рівень критичних помилок, що інформує про серйозний збій роботи програми, через який її виконання зупинене.

#filename — рядок зі шляхом до файлу, у який записується інформація.
#Зауважте, логи заведено записувати до спеціальних текстових файлів, які мають розширення .log.
#filemode — режим відкриття файлу, за замовчанням a, тобто відкриття на дозаписування (використовується найчастіше). В іншому випадку можна встановити значення w, тобто на записування.
#format — відповідає за форматування запису, а як аргумент приймає рядок із вказаним форматом. Крім самого тексту, до нього можна додати різні аргументи.

# logging.basicConfig(level=logging.DEBUG, filename="logs.log", filemode="w", format="We have logging massage:%(asctime)s:%(levelname)s - %(message)s")
# logging.debug('debug')
# logging.info("info")
# try:
#     print(10/0)
# except Exception:
#     logging.exception("Exception")

# logging.basicConfig(level=logging.INFO, filename="logs.log", filemode="w", format="%(asctime)s:%(levelname)s - %(message)s")
# logging.info("Program start")

# logging.basicConfig(level=logging.ERROR, filename="logs.log", filemode="w", format="%(asctime)s:%(levelname)s - %(message)s")
#
# def divide(num1, num2):
#     try:
#         result = num1 / num2
#         return result
#     except ZeroDivisionError as e:
#         logging.error(f'Division error: {e}')
#
# divide(10, 0)

# if 2+2 == 4:
#     print('In fact, 2 + 2 = 4')

# """
# >>> 2+2
# 5
# """
#
# if __name__ == '__main__':
#     import doctest
#     doctest.testmod()

def adder(*args, **kwargs):
    result = 0
    for i in args:
        result += i
    for i in kwargs.values():
        result += i
        return result