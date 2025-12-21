# rk2.py
from operator import itemgetter


class Syntax:
    """Синтаксическая конструкция"""

    def __init__(self, id, name, complexity, lang_id):
        self.id = id
        self.name = name
        self.complexity = complexity
        self.lang_id = lang_id


class Language:
    """Язык программирования"""

    def __init__(self, id, name):
        self.id = id
        self.name = name


class SyntaxLanguage:
    """Для связи многие-ко-многим"""

    def __init__(self, lang_id, syntax_id):
        self.lang_id = lang_id
        self.syntax_id = syntax_id


# === РЕФАКТОРИНГ: Выносим логику в отдельные функции ===

def get_one_to_many(languages, syntaxes):
    """Соединение один-ко-многим"""
    return [(s.name, s.complexity, l.name)
            for l in languages
            for s in syntaxes
            if s.lang_id == l.id]


def get_many_to_many(languages, syntaxes, syntaxes_languages):
    """Соединение многие-ко-многим"""
    many_to_many_temp = [(l.name, sl.lang_id, sl.syntax_id)
                         for l in languages
                         for sl in syntaxes_languages
                         if l.id == sl.lang_id]

    return [(s.name, s.complexity, lang_name)
            for lang_name, lang_id, syntax_id in many_to_many_temp
            for s in syntaxes if s.id == syntax_id]


def task_b1(one_to_many):
    """Задание Б1: отсортированный список конструкций и языков"""
    return sorted(one_to_many, key=itemgetter(0))


def task_b2(languages, one_to_many):
    """Задание Б2: языки с количеством конструкций"""
    res2_unsorted = []
    for l in languages:
        l_syntaxes = list(filter(lambda i: i[2] == l.name, one_to_many))
        if len(l_syntaxes) > 0:
            res2_unsorted.append((l.name, len(l_syntaxes)))
    return sorted(res2_unsorted, key=itemgetter(1))


def task_b3(many_to_many):
    """Задание Б3: конструкции, заканчивающиеся на 'ов'"""
    return [(syntax_name, lang_name)
            for syntax_name, complexity, lang_name in many_to_many
            if syntax_name.endswith('ов')]


def main():
    # Тестовые данные
    languages = [
        Language(1, 'Python'),
        Language(2, 'C++'),
        Language(3, 'Java'),
        Language(4, 'JavaScript'),
        Language(5, 'C#'),
    ]

    syntaxes = [
        Syntax(1, 'if', 5, 1),
        Syntax(2, 'for', 6, 1),
        Syntax(3, 'while', 6, 2),
        Syntax(4, 'class', 8, 3),
        Syntax(5, 'function', 7, 4),
        Syntax(6, 'lambda', 7, 1),
        Syntax(7, 'interface', 8, 3),
    ]

    syntaxes_languages = [
        SyntaxLanguage(1, 1),
        SyntaxLanguage(1, 2),
        SyntaxLanguage(1, 6),
        SyntaxLanguage(2, 1),
        SyntaxLanguage(2, 3),
        SyntaxLanguage(3, 1),
        SyntaxLanguage(3, 4),
        SyntaxLanguage(3, 7),
        SyntaxLanguage(4, 1),
        SyntaxLanguage(4, 5),
        SyntaxLanguage(5, 1),
        SyntaxLanguage(5, 4),
    ]

    # Получаем соединения
    one_to_many = get_one_to_many(languages, syntaxes)
    many_to_many = get_many_to_many(languages, syntaxes, syntaxes_languages)

    # Выполняем задания
    print('Задание Б1')
    print(task_b1(one_to_many))

    print('\nЗадание Б2')
    print(task_b2(languages, one_to_many))

    print('\nЗадание Б3')
    print(task_b3(many_to_many))


if __name__ == '__main__':
    main()