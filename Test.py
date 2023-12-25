from unittest import TestCase, main
import os
from BoeraMurraHorspulaAlgorithm import BoeraMurraHorspulaAlgorithm
from KnuthMorrisPrathAlgorithm import KnuthMorrisPrathAlgorithm
from HashAlgorithm import HashAlgorithm
from SimpleAlgorithm import SimpleAlgorithm


class TestAlgorithms(TestCase):

    def _check_test(self, str, sub_str, answer):
        list_algorithms = [
            SimpleAlgorithm(),
            HashAlgorithm(),
            KnuthMorrisPrathAlgorithm(),
            BoeraMurraHorspulaAlgorithm()
        ]

        for algorithm in list_algorithms:
            result = algorithm.find_substring_in_string(str, sub_str)
            self.assertEqual(result, answer, msg=algorithm.__str__())

    def test_simple(self):
        self._check_test("a", "a", 0)
        self._check_test("aboba", "abob", 0)
        self._check_test("abcdefg", "f", 5)
        self._check_test("Python", "thon", 2)

    def test_exeption(self):
        self._check_test(None, "a", None)
        self._check_test("a", None, None)
        self._check_test(5, "a", None)
        self._check_test(25, 5, None)
        self._check_test("abc", "abcdef", None)

    def test_with_recurring_sequences(self):
        self._check_test("aabaaabaaaab", "aaaab", 7)
        self._check_test("TTACACTTCAACTTACTCAACTTACACTTACTACACTTACT", "ACTC", 14)
        self._check_test("TCATTCACATACTTCACATACTCATTCATCACATACTCAT", "TCACATACTT", 4)

    def test_with_many_different_letters(self):
        self._check_test("thsvdjndyh", "vdjn", 3)
        self._check_test("nbuhirsmcawdlppqzajfunemxplasmbgrirlqmcnz", "plasmbg", 25)
        self._check_test("ibovaesonijppfaebuovhawpdoinsjpakaxpinveomxs", "doinsjpakaxpinveom", 24)

    def test_with_real_text(self):
        self._check_test("Python is an easy to learn, powerful programming language.", "powerful programming", 28)
        self._check_test("лавировали лавировали да не вылавировали ", "вылавировали", 28)
        self._check_test("<meta data-vue-meta=\"ssr\" property=\"fb:app_id\" content=\"444736788986613\">",
                         "content=\"", 47)

    def test_simple_without_result(self):
        self._check_test("aaaaaaaaa", "b", -1)
        self._check_test("thsvdjndyh", "vdan", -1)
        self._check_test("ACTCATTCACATTCAACTCATTCACATACTTCACATAC", "ATTCACATC", -1)

    def test_found_index_first_substring(self):
        self._check_test("aaaaaaaaa", "aaaa", 0)
        self._check_test("Что такое Кот. Код многозначное понятие. Кодом,", "Код", 15)
        self._check_test("TCGTCAACAATCGCAACAGCAATCGCAATCGCAATCACAATCGCAACAAT", "AATCGC", 8)

    def read_file(self, adress):
        with open(adress, 'r', encoding="utf-8") as f:
            text = f.read()
        return text

    def file_testing(self, path_file):
        for i in range(1, 6):
            real_path_str = os.path.abspath(path_file + "_{}.txt".format(i))
            string = self.read_file(real_path_str)
            start_substring = ((98*len(string))//1000)
            end_substring = ((99*len(string))//1000)
            substring = string[start_substring: end_substring]
            self._check_test(string, substring, start_substring)

    def test_long_real_text(self):
        part_path = "Data/real_text/real_text"
        self.file_testing(part_path)

    def many_different_simbols(self):
        part_path = "Data/many_different_simbols/many_different_simbols"
        self.file_testing(part_path)

    def test_recurring_sequences(self):
        part_path = "Data/recurring_sequences/recurring_sequences"
        self.file_testing(part_path)


if __name__ == '__main__':
    main()
