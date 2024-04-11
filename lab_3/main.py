from text_handler import *
from copy import copy

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
        symbol_not_in_alphabet = False
        all_good = True
        for symbol in raw_text:
            if symbol not in alphabet:
                symbol_not_in_alphabet = True
                all_good = False
                break
        if symbol_not_in_alphabet:
            print("Введено не допустимий символ")
            all_good = False
        if raw_text[-1] != ".":
            print("Текст має закінчуватись на крапку")
            all_good = False
        if all_good:
            break
    return raw_text

def task_2(input_text_class):
    text_class = copy(input_text_class)

    # видаляємо усі слова що не співпадають з початковим відрізком алфавіту
    counter = 0 # лічильник алфавітного порядку
    cursor_position = 0 # позиція каретки обробника даних
    while cursor_position < len(text_class.contains):
        # debug print([cursor_position,str(text_class.contains)])
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
                if not (str(text_class.contains[cursor_position]) == str(" ") or str(text_class.contains[cursor_position]) == str(".")):
                    text_class.contains.pop(cursor_position)
                else:
                    deleted = True
            continue
    return text_class


while True:
    text_c = Text(get_input(),DoubleLinkedList)
    print("отриманий текст")
    print(str(text_c.contains))
    print("текст з слів що співпадають з початковим відрізком алфавіту")
    print(str(task_2(text_c).contains))