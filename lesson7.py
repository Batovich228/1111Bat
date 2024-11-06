# # Ітератор
# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# iterator = iter(my_list)
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
# # print(next(iterator))
#
# #  Ітератори дозволяють ефективно працювати з великими наборами даних. Замість того, щоб зберігати всі елементи в пам'яті,
# #  можна перебирати їх по одному, економлячи ресурси. Це важливо в сучасних додатках, де обсяги даних можуть бути дуже великими.
#
# # Застосування
# # Ітератори використовуються скрізь, де треба обробляти дані послідовно. Наприклад, у веб-скрапінгу, обробці потоків даних, у великих базах даних тощо.
#
# # Генератори
#
# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#
# for value in my_generator():
#     print(value)
# # Застосування
# #Генератори часто використовують для роботи з потоками даних, обробки великих файлів та потокового відео,
# # де немає потреби завантажувати весь файл одразу. Також зручно використовувати генератори для створення нескінченних послідовностей чисел,
# # наприклад, у математичних задачах.
#
# # Замикання
# def outer_function(x):
#     def inner_function(y):
#         return x + y
#     return inner_function
# closure_example = outer_function(10)
# print(closure_example(5))
#
# #Декоратори
# def decorator(func):
#     def wrapper():
#         print("Перед виконаням функції")
#         func()
#         print("Після виконання функції")
#         func()
#     return wrapper
# @decorator
# def say_hello():
#     print("hello")
#
# say_hello()

# import time
# def timeit(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         work_time= end-start
#         print(f"Час виконання '{func.__name__}': {work_time:.4f} секунд")
#         return result
#     return wrapper
# @timeit
# def func1():
#   time.sleep(10)
# func1()

def even_numbers(limit):
    number = 0
    while number < limit:
        yield number
        number += 2

for i in even_numbers(100):
    print(i)