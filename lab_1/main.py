import PyTaCo
import os
import time

#1.4.3
"""
Числа Фібоначчі f n обчислюються за формулами f 0 =f 1 =1;
f n =f n-1 +f n-2 при n=2,3,... Реалізувати функцію, яка за заданим номером n
обчислюватиме значення f n.
"""
def fib(n):
    match(n):
        case 0: return 1
        case 1: return 1
        case _: return fib(n-1)+fib(n-2)

print(fib(int(input("Знайти число фібоначі з порядковим номером: >>>"))))

#1.4.14
"""
Реалізувати алгоритм для розв’язання задачі «Ханойські вежі».
Виписати послідовність ходів для перекладання n дисків вежі (n = 2;
3; 4; 5 дисків, використати онлайн гру).
"""

initial_Height = int(input("Введіть висоту початкової вежі: >>>"))
Towers = PyTaCo.PyTableConsole([["Башта А"],["Башта В"],["Башта С"]])
for i in range(1,initial_Height+1):
    Towers.contains[0].append("="*i)

def draw_Towers(Towers):
    os.system('cls')
    print(Towers)
    print("Хід №" + str(move_n))
    time.sleep(min(1,1/(initial_Height**2)))

def find_last_occurrence(lst, element):
    for i in reversed(range(len(lst))):
        if lst[i] == element:
            return i
    return -1

move_n = 1
def move_piece(Towers, start, stop):
    global move_n
    piece = ""
    if "" in Towers.contains[start]:
        piece = Towers.contains[start][find_last_occurrence(Towers.contains[start],"")+1]
        Towers.contains[start][Towers.contains[start].index(piece)] = ""
    else:
        piece = Towers.contains[start][1]
        Towers.contains[start][1] = ""
    Towers.contains[stop][find_last_occurrence(Towers.contains[stop],"")] = piece
    draw_Towers(Towers)
    move_n+=1

    return Towers

def iterate_Towers(Towers, start, stop, height):
    middle = [0,1,2]
    middle.remove(start)
    middle.remove(stop)
    middle = middle[0]
    if height == 1:
        move_piece(Towers, start, stop)
    if height == 2:
        move_piece(Towers, start, middle)

        move_piece(Towers, start, stop)

        move_piece(Towers, middle, stop)
    else:
        Towers = iterate_Towers(Towers, start, middle, height-1)
        move_piece(Towers, start, stop)
        Towers = iterate_Towers(Towers, middle, stop, height-1)
    return Towers

draw_Towers(Towers)
iterate_Towers(Towers,0,2,Towers.height()-1)
print("The End")
time.sleep(10)