from abc import ABCMeta, abstractmethod

class AlgoritmFindSubstringInString(metaclass=ABCMeta):
    """Этот абстрактный класс используется для удобства написания тестов"""

    @abstractmethod
    def find_substring_in_string(self, string, substring):
        """Найти подстроку в строке"""

    def is_correct_data(self, string, substring):
        if string is None or substring is None:
            return False
        if not (type(substring) is str and type(string) is str):
            return False
        if len(substring) > len(string):
            return False
        return True