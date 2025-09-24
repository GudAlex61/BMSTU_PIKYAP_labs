
import sys
import math
from typing import NamedTuple

# Алгебраический тип
class SquareRootResult:
    NoRoots = NamedTuple("NoRoots", [])
    OneRoot = NamedTuple("OneRoot", [("root", float)])
    TwoRoots = NamedTuple("TwoRoots", [("root1", float) , ("root2", float)])
    ThreeRoots = NamedTuple("ThreeRoots", [("root1", float) , ("root2", float), ("root3", float)])
    FourRoots = NamedTuple("FourRoots", [("root1", float) , ("root2", float), ("root3", float) , ("root4", float)])


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef

def get_roots_t(a,b,c,t):
    if t==0:
        roots = {0}
        return roots
    elif t<0:
        return {}
    roots = {t**0.5, t**0.5*-1}
    return  roots

def get_roots(a, b, c):
    '''
    Вычисление корней квадратного уравнения

    Args:
        a (float): коэффициент А
        b (float): коэффициент B
        c (float): коэффициент C

    Returns:
        Список корней в виде типа SquareRootResult
    '''
    D = b*b - 4*a*c
    if D == 0.0:
        t = -b / (2.0*a)
        roots = get_roots_t(a,b,c,t)
    elif D > 0.0:
        sqD = math.sqrt(D)
        t1 = (-b+sqD)/(2*a)
        t2 = (-b-sqD)/(2*a)
        roots1 = get_roots_t(a,b,c,t1)
        roots2 = get_roots_t(a,b,c,t2)
        roots = roots1.union(roots2)
    else:
        return SquareRootResult.NoRoots()
    roots_list = list(roots)
    if len(roots_list)==4:
        return SquareRootResult.FourRoots(roots_list[0], roots_list[1], roots_list[2], roots_list[3])
    if len(roots_list)==3:
        return SquareRootResult.ThreeRoots(roots_list[0], roots_list[1], roots_list[2])
    elif len(roots_list)==2:
        return SquareRootResult.TwoRoots(roots_list[0], roots_list[1])
    else:
        return SquareRootResult.OneRoot(roots_list[0])

def print_roots(roots_tuple):
    '''
    Печать корней квадратного уравнения

    Args:
        Список корней в виде типа SquareRootResult
    '''
    match roots_tuple:
        case SquareRootResult.FourRoots(root1, root2, root3, root4):
            print(f'Четыре корня: {root1}, {root2}, {root3} и {root4}')
        case SquareRootResult.ThreeRoots(root1, root2, root3):
            print(f'Три корня: {root1}, {root2} и {root3}')
        case SquareRootResult.TwoRoots(root1, root2):
            print(f'Два корня: {root1} и {root2}')
        case SquareRootResult.OneRoot(root):
            print(f'Один корень: {root}')
        case SquareRootResult.NoRoots():
            print('Нет корней')        


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    roots = get_roots(a,b,c)
    # Вывод корней
    print_roots(roots)


if __name__ == "__main__":
    main()
