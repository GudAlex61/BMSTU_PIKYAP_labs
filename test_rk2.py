# test_rk2.py
import unittest
from rk2 import *


class TestRK2(unittest.TestCase):

    def setUp(self):
        """Подготовка тестовых данных"""
        self.languages = [
            Language(1, 'Python'),
            Language(2, 'C++'),
            Language(3, 'Java'),
        ]

        self.syntaxes = [
            Syntax(1, 'if', 5, 1),
            Syntax(2, 'for', 6, 1),
            Syntax(3, 'while', 6, 2),
        ]

        self.syntaxes_languages = [
            SyntaxLanguage(1, 1),
            SyntaxLanguage(1, 2),
            SyntaxLanguage(2, 3),
        ]

    def test_task_b1(self):
        """Тест для задания Б1: сортировка по названию конструкции"""
        one_to_many = get_one_to_many(self.languages, self.syntaxes)
        result = task_b1(one_to_many)

        # Проверяем, что результат отсортирован по первому элементу (названию конструкции)
        for i in range(len(result) - 1):
            self.assertLessEqual(result[i][0], result[i + 1][0])

        # Проверяем наличие ожидаемых данных
        expected_constructions = ['for', 'if', 'while']
        result_constructions = [item[0] for item in result]
        self.assertEqual(sorted(result_constructions), sorted(expected_constructions))

    def test_task_b2(self):
        """Тест для задания Б2: подсчет конструкций по языкам"""
        one_to_many = get_one_to_many(self.languages, self.syntaxes)
        result = task_b2(self.languages, one_to_many)

        # Проверяем формат результата
        for lang_name, count in result:
            self.assertIsInstance(lang_name, str)
            self.assertIsInstance(count, int)
            self.assertGreater(count, 0)

        # Python должен иметь 2 конструкции (if, for)
        python_count = next((count for lang, count in result if lang == 'Python'), 0)
        self.assertEqual(python_count, 2)

    def test_task_b3(self):
        """Тест для задания Б3: поиск конструкций, оканчивающихся на 'ов'"""
        # Добавим тестовую конструкцию, оканчивающуюся на 'ов'
        syntaxes_with_ov = self.syntaxes + [Syntax(4, 'лов', 5, 1)]

        one_to_many = get_one_to_many(self.languages, syntaxes_with_ov)
        many_to_many = get_many_to_many(self.languages, syntaxes_with_ov, self.syntaxes_languages)

        result = task_b3(many_to_many)

        # Должна найтись конструкция 'лов'
        ov_constructions = [name for name, _ in result]
        self.assertIn('лов', ov_constructions)

        # Проверяем, что все найденные конструкции оканчиваются на 'ов'
        for syntax_name, _ in result:
            self.assertTrue(syntax_name.endswith('ов'))


if __name__ == '__main__':
    unittest.main()