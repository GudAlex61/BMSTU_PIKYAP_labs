from operator import itemgetter

class Syntax:
    """Синтаксическая конструкция"""

    def __init__(self, id, name, complexity, lang_id):
        self.id = id
        self.name = name
        self.complexity = complexity  # количественный признак
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


def main():
    # Соединение данных один-ко-многим
    one_to_many = [(s.name, s.complexity, l.name)
                   for l in languages
                   for s in syntaxes
                   if s.lang_id == l.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(l.name, sl.lang_id, sl.syntax_id)
                         for l in languages
                         for sl in syntaxes_languages
                         if l.id == sl.lang_id]

    many_to_many = [(s.name, s.complexity, lang_name)
                    for lang_name, lang_id, syntax_id in many_to_many_temp
                    for s in syntaxes if s.id == syntax_id]

    print('Задание Б1')
    # Список всех связанных синтаксических конструкций и языков, отсортированный по конструкциям
    res1 = sorted(one_to_many, key=itemgetter(0))
    print(res1)

    print('\nЗадание Б2')
    # Список языков с количеством синтаксических конструкций в каждом языке
    res2_unsorted = []
    for l in languages:
        # Синтаксические конструкции этого языка
        l_syntaxes = list(filter(lambda i: i[2] == l.name, one_to_many))
        if len(l_syntaxes) > 0:
            res2_unsorted.append((l.name, len(l_syntaxes)))


    # Сортировка по количеству конструкций
    res2 = sorted(res2_unsorted, key=itemgetter(1))
    print(res2)

    print('\nЗадание Б3')
    # Список всех синтаксических конструкций, у которых название заканчивается на «ов», и названия их языков
    res3 = []
    for syntax_name, complexity, lang_name in many_to_many:
        if syntax_name.endswith('ов'):
            res3.append((syntax_name, lang_name))

    print(res3)


if __name__ == '__main__':
    main()