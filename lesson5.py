# import requests
# def first_function():
#     pass

# class Human:
#     pass

# rq = requests
# first_f = first_function
# nick = Human

# # print(requests.__name__)
# # print(rq.__name__)
# # print(first_function.__name__)
# # print(first_f.__name__)
# # print(Human.__name__)
# # print(nick.__name__)
# # print(__name__)

# # intro_list = []
# # for method in dir(intro_list):
# #     print(method)
# a = "1.5"
# # print(dir(a))
# # type() — дозволяє дізнатись тип об'єкта.
# # dir() — дозволяє дізнатись всі атрибути та методи.

# # hasattr() — дозволяє дізнатись наявність атрибуту чи методу
# # data = "text"

# # print(hasattr(data, 'reverse'))
# # print(hasattr(data, 'index'))

# # getattr() — дозволяє отримати атрибути. Вона приймає три параметри: перший
# # — об'єкт, з якого й мають братися дані, другий — рядок із назвою методу, третій
# # — дані, які треба повернути, якщо шуканого імені немає.

# # data = "text"

# # print(getattr(data, 'startswith'))
# # print(getattr(data, 'startswith', None))
# # print(getattr(data, 'reverse', "MIsha"))

# # callable() — дозволяє дізнатись, чи можна викликати об'єкт
# # data = "text"

# # def first_func():
# #     pass

# # print(callable(data))
# # print(callable(first_func))

# # issubclass() —дозволяє дізнатись, чи спадкується клас від іншого:
# # class First_class:
# #     pass

# # class Second_class(First_class):
# #     pass

# # print(issubclass(First_class, Second_class))
# # print(issubclass(Second_class, First_class))


# # isinstance() — дозволяє отримати інформацію про те, чи належить об'єкт певному класу.Якщо клас об'єкта породжений від іншого класу, то об'єкт так само буде належати йому.
# class First_class:
#     pass

# class Second_class(First_class):
#     pass

# obj_from_class_2 = Second_class()

# print(isinstance(obj_from_class_2, Second_class))
# print(isinstance(obj_from_class_2, First_class))

import inspect
import requests
#print(inspect.ismodule(requests))
# print(inspect.isclass(requests))
# print(inspect.isfunction(requests))
# print(inspect.getmodule(requests.get))
# print(inspect.getmodule(list))

class Human:
    def __init__(self, age=29, height=167, name="John"):
        self.age = age
        self.height = height
        self.secondname = "Wich"

sig = inspect.signature(Human)
for param in sig.parameters.values():
    print(param.name, param.default)

