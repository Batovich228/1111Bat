# try:
#     a = int(input())
#     b = int(input())
#     c = a + b
#     print(c)
#     k = 1/0
# except ArithmeticError:
#     print("Знайдена помилка")
#     k = 0
#
# print(k)
#
# def first_function():
#     hello = "Hello Word"
#     print(hello)
#
# first_function()

# try:
#     print("Start code")
#    # print(error)
#     print(10/0)
#     print("No errors")
#
# # except NameError:
# #     print("We have an error")
# #
# # except ZeroDivisionError:
# #     print("We have an ZeroDivisionError")
#
# except(NameError,ZeroDivisionError) as error:
#     print(error)
# print("Code after capsule")

# try:
#     try:
#         error = None
#         print('Start Code')
#         print(error)
#         print('No error')
#     except SyntaxError:
#         print('Wrong syntax')
# except NameError as error:
#     print(error)
#
# try:
#     print('Hello')
# except:
#     print('We have problems')
# else:
#     print('No problems')

# try:
#     print('Hello World!')
#     print('No problem')
# except NameError as error:
#     print(error)
# else:
#     print('No problems')
# finally:
#     print('Finally code')

# def checker(var_1):
#     if type(var_1) != str:
#         raise TypeError(f"Sorry, we can't convert {type(var_1)}, we need class str")
#     else:
#         return var_1
#
# first_var = 5.6
# checker(first_var)

# class BuildingEror(Exception):
#     def __str__(self):
#         return f"With so much material the house cannot be built!"
# def check_material(amount_of_material, limit_value):
#     if amount_of_material > limit_value:
#         return "Enough material"
#     else:
#         raise BuildingEror(amount_of_material)
# material = 300
# check_material(material, 300)

# try:
#     a = int(input("Введіть чисельник"))
#     b = int(input("Введіть знаменик"))
#     result = a/b
#     print (int(result))
# except ZeroDivisionError:
#     print("Помилка: Ділення на нуль неможливе.")
# except ValueError:
#     print("Помилка: Введені дані не є числом")
#
# words = ["apple", "banana", "cherry", "data",]
# try:
#     index = int(input("Введіть індекс: "))
#     word = words[index]
#     print("Слово за індексом", index, ':', word)
# except IndexError:
#     print("Помилка: Вказаний індекс перевищує довжину списку.")
# except ValueError:
#     print("Помилка: Введені дані не є числом")

# import warnings
# warnings.simplefilter("ignore", SyntaxWarning)
# warnings.simplefilter('always', ImportWarning)
#
# warnings.warn("Warning, no code here", SyntaxWarning)
# try:
#     warnings.warn("Warning, no code here", ImportWarning)
# except:
#     print("Warning, no code here")

# age = -1
# while age <= 5:
#     try:
#         age = int(input("Enter your age: "))
#     except ValueError:
#         print("Invalid")

try:
    # some_value = 7
    age = some_value
except NameError:
    print("Invalid: Такої зміної не існує!")
else:
    print("Invalid: Все ок")

try:
    deg ()
except NameError:
    print("Invalid: Такої функції не існує!")
else:
    print("Invalid: Все ок")