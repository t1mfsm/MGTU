from io import StringIO
import unittest
from unittest.mock import patch, mock_open
import main

class TestProgram(unittest.TestCase):

    @patch("builtins.open", mock_open(read_data="test data"))
    def test_filter_details_ending_with_a(self):
        expected_result = [("Звезда", 31, "ООО 'ТехноКомпания'"),
                           ("Спичка", 5, "ООО 'ТехноКомпания'"),
                           ("Гайка", 300, "АО 'Индустрия'"),
                           ("Клавиша", 30, "АО 'Индустрия'"),
                           ("Шайба", 250, "ЗАО 'Производство'"),
                           ("Пружина", 65, "ОАО 'Прогресс'"),
                           ("Плитка", 154, "Техногрупп"),
                           ("Рамка", 60, "МастерМеханика"),
                           ("Кнопка", 120, "СпецПромТехника"),
                           ("Платина", 100, "СпецПромТехника"),
                           ("Батарейка", 90, "СпецПромТехника"),
                           ("Пластмасса", 90, "Автоэлектрика"),
                           ("Ручка", 34, "ТехноСревисГарант"),
                           ("Антенна", 206, "ТехноСревисГарант"),
                           ("Скрепка", 78, "МедТехИнжиниринг"),
                           ("Трубка", 59, "ЭнергоСервис"),
                           ("Сирена", 96, "ЭнергоСервис")]
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main.main()
            actual_output = mock_stdout.getvalue()
            self.assertTrue(all(str(detail) in actual_output for detail in expected_result))

    @patch("builtins.open", mock_open(read_data="test data"))
    def test_average_prices_by_provider(self):
        expected_result = [("Инновационные Технологии", 259.5),
                           ("АгроТехника", 258.6666666666667),
                           ("ПромХолдинг", 208.33333333333334),
                           ("ОАО 'Прогресс'", 199.66666666666666),
                           ("Инженерные Решения", 166.0),
                           ("АО 'Индустрия'", 165.0),
                           ("МедТехИнжиниринг", 144.0),
                           ("ЗАО 'Производство'", 134.66666666666666),
                           ("ТехноСревисГарант", 120.0),
                           ("Производство и Сервис", 106.0),
                           ("СпецПромТехника", 103.33333333333333),
                           ("Техногрупп", 102.0),
                           ("ЭнергоСервис", 64.66666666666667),
                           ("Автоэлектрика", 60.0),
                           ("МастерМеханика", 56.333333333333336),
                           ("ГоризонтПроизводство", 49.5),
                           ("ТехноВидение", 47.0),
                           ("ООО 'ТехноКомпания'", 45.333333333333336),
                           ("СпецТехноГрупп", 40.0),
                           ("ИП 'МастерТех'", 38.5)]
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main.main()
            actual_output = mock_stdout.getvalue()
            self.assertTrue(all(str(provider) in actual_output for provider in expected_result))

    @patch("builtins.open", mock_open(read_data="test data"))
    def test_filter_providers_starting_with_a(self):
        expected_result = {"АО 'Индустрия'": ["Болт", "Реле"],
                            "Автоэлектрика": ["Шестерня"],
                            "АгроТехника": ["Клавиша"]}
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            main.main()
            actual_output = mock_stdout.getvalue()
            self.assertTrue(all(provider in actual_output for provider in expected_result.keys()))
            self.assertTrue(all(all(detail in actual_output for detail in details) for provider, details in expected_result.items()))

if __name__ == '__main__':
    unittest.main()
