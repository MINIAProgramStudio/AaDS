from text_handler import *
from copy import copy
import time
import sys

"""
Слова тексту із малих латинських літер записані не менше, ніж через один пробіл; текст закінчується крапкою.

Надрукувати всі слова, які відрізняються від першого слова і співпадають з початковим відрізком алфавіту (a, ab, abc тощо).
Видалити останню літеру в цих словах. 
До кожного слова дописати крапку.
"""
alphabet = "abcdefghijklmnopqrstuvwxyz ."
def get_input():
    print("Будь ласка введіть текст.")
    print("Текст має містити лише маленькі латинські літери, пробіли та крапки і закінчуватись на крапку")
    raw_text = ""
    while True:
        raw_text = input(">>>")
        if raw_text == "":
            print("Ви не ввели текст")
            continue
        symbol_not_in_alphabet = False
        all_good = True
        for symbol in raw_text:
            if symbol not in alphabet:
                symbol_not_in_alphabet = True
                all_good = False
        if symbol_not_in_alphabet:
            print("Введено недопустимий символ")
            all_good = False
        if raw_text[-1] != ".":
            print("Текст має закінчуватись на крапку")
            all_good = False
            continue
        if all_good:
            break
    return raw_text

def task_2(input_text_class):
    text_class = copy(input_text_class)

    # видаляємо усі слова що не співпадають з початковим відрізком алфавіту
    counter = 0 # лічильник алфавітного порядку
    cursor_position = 0 # позиція каретки обробника даних
    while cursor_position < len(text_class.contains):
        if str(text_class.contains[cursor_position]) == str(" ") or str(text_class.contains[cursor_position]) == str("."):
            # якщо пробіл або крапка -- скинути лічильник ал. пор. та пересунутись на 1 вправо
            cursor_position+=1
            counter = 0
            continue
        if str(text_class.contains[cursor_position]) == str(alphabet[counter]):
            # якщо символ співпадає з ал. пор. -- пересунутись на 1 вправо і збільшити лічильник ал. пор. на 1
            cursor_position += 1
            counter += 1
            continue
        else:
            counter = 0
            #переміщення до початку слова
            while not (str(text_class.contains[cursor_position]) == str(" ") or str(text_class.contains[cursor_position]) == str(".") or cursor_position <= 0):
                cursor_position -= 1
            while str(text_class.contains[cursor_position]) == str(" ") or str(text_class.contains[cursor_position]) == str("."):
                cursor_position += 1

            #видалення слова

            deleted = False
            while not deleted:
                if str(text_class.contains[cursor_position]) == str(" ") or str(text_class.contains[cursor_position]) == str("."):
                    deleted = True
                else:
                    text_class.contains.pop(cursor_position)
            continue

    # беремо перше слово з тексту
    first_word = Text("", input_text_class.contains.__class__)
    cursor_position = 0
    while str(input_text_class.contains[cursor_position]) == str(" ") or str(input_text_class.contains[cursor_position]) == str("."):
        cursor_position += 1
    while not(str(input_text_class.contains[cursor_position]) == str(" ") or str(input_text_class.contains[cursor_position]) == str(".") or cursor_position > len(input_text_class.contains)):
        first_word.contains.append(input_text_class.contains[cursor_position])
        cursor_position += 1

    # видаляємо усі слова що співпадають з першим
    cursor_position = 0
    while cursor_position < len(text_class.contains):
        if str(text_class.contains[cursor_position]) == str(" ") or str(
                text_class.contains[cursor_position]) == str("."):
            # якщо пробіл або крапка -- скинути лічильник та пересунутись на 1 вправо
            cursor_position += 1
            counter = 0
            continue
        if counter >= len(first_word.contains):
            # якщо довжина слова більше ніж довжина першого слова -- рухатись вправо
            cursor_position += 1
            continue

        if str(text_class.contains[cursor_position]) == str(first_word.contains[counter]):
            # якщо символ співпадає з першим словом -- пересунутись на 1 вправо і збільшити лічильник ал. пор. на 1
            cursor_position += 1
            counter += 1

            if str(text_class.contains[cursor_position]) == str(" ") or str(
                    text_class.contains[cursor_position]) == str("."):
                # якщо досягнуто кінця слова у цій гілці, значить слово співпадає з першим і його потрібно видалити
                # переміщення до початку слова
                cursor_position -= 1
                while not (str(text_class.contains[cursor_position]) == str(" ") or str(
                        text_class.contains[cursor_position]) == str(".") or cursor_position <= 0):
                    cursor_position -= 1
                while str(text_class.contains[cursor_position]) == str(" ") or str(
                        text_class.contains[cursor_position]) == str("."):
                    cursor_position += 1

                # видалення слова

                deleted = False
                while not deleted:
                    if not (str(text_class.contains[cursor_position]) == str(" ") or str(
                            text_class.contains[cursor_position]) == str(".")):
                        text_class.contains.pop(cursor_position)
                    else:
                        deleted = True
                continue
            continue
        else:
            #якщо символ не співпав з символо першого слова -- зашкалити лічильник, тим самим змусивши перехід на наступне слово.
            counter = len(first_word.contains)
            continue

    # видалення останньої букви та дописання точки після усіх слів:
    cursor_position = 0
    was_in_word = False
    while cursor_position < len(text_class.contains):
        if str(text_class.contains[cursor_position]) == str(" ") or str(text_class.contains[cursor_position]) == str("."):
            if was_in_word:
                if isinstance(text_class.contains, list):
                    text_class.contains[cursor_position - 1] = "."
                elif isinstance(text_class.contains, DoubleLinkedList):
                    text_class.contains[cursor_position-1].contains = "."

            was_in_word = False
        else:
            was_in_word = True
        cursor_position += 1
    return text_class

print("Вас вітає програма обробки латинського тексту №2")
print("Ця програма залишить лише слова що не співпадають з першим словом і співпадають з початковим відрізком алфавіту.")
print("Також останні літери слів будуть видалені і до усіх слів буде дописано крапку")
while True:
    text = get_input()
    start = time.time()
    text_c = Text(text,DoubleLinkedList)

    result_DDL = str(task_2(text_c))
    end = time.time()
    DDL_time = end-start
    DDL_memory = sys.getsizeof(text_c)

    start = time.time()
    text_c_l = Text(text, list)
    result_list = str(task_2(text_c_l))
    end = time.time()
    list_time = end - start
    list_memory = sys.getsizeof(text_c_l)
    print("Результат:")
    print(str(result_DDL))
    print("Час роботи двозв'язного списку: "+str(DDL_time))
    print("Пам'ять використана двозв'язним списком: "+str(DDL_memory))
    print("Час роботи динамічного масиву: " + str(list_time))
    print("Пам'ять використана динамічним масивом: " + str(list_memory))
    print()