from AlgoritmFindSubstringInString import AlgoritmFindSubstringInString as algorithm


class BoeraMurraHorspulaAlgorithm(algorithm):

    """
        Используется для анализа теста,где встречается большое кол-во разных букв и
        нет часто повторяющихся последовательстей. Сложность в неудачных случаях O(n*m).
        В некоторых удачных O(n/m). В среднем O(n+m).
    """
    @staticmethod
    def __found_dict_delta(sub_str):
        d = {}  # тфблица смещений

        # заполняем таблицу с конца,чтобы было легко  находить наименьшее расстоение для много раз встречающихся букв
        for i in range(len(sub_str) - 2, -1, -1):
            if sub_str[i] not in d.keys():  # если сивлол встретился 1-ый раз,добавим в таблицу
                d[sub_str[i]] = len(sub_str) - i - 1

        # если последний символ подстроки нигде ещё не встречается в подстроке ,то дальше
        # при не совпадении последнего сивола подстроки со строкой,можно сделать
        # хорошую оптимизацию
        if sub_str[len(sub_str) - 1] not in d.keys():
            d[sub_str[len(sub_str) - 1]] = len(sub_str)

        d['**'] = len(sub_str)  # ещё тут крутая оптимазация,если
        return d

    @staticmethod
    def __algoritm_boera_murra_horspula(str, sub_str):
        d = BoeraMurraHorspulaAlgorithm.__found_dict_delta(sub_str)
        i_str = len(sub_str) - 1  # счетчик проверяемого символа в строке
        while i_str < len(str):
            delta_for_compare = 0
            is_Not_right = False
            for i_sub_str in range(len(sub_str) - 1, -1, -1):
                if str[i_str - delta_for_compare] != sub_str[i_sub_str]:
                    if i_sub_str == len(sub_str) - 1:
                        delta_i_str = d[str[i_str]] if d.get(str[i_str], False) else d['**']
                        # если не равен последний символ,то делаем смешение хорошее,если буквы из строки вообще нет
                        # в подстроке,а иначе делаем так,чтобы сравниваемая буква строки
                        # на следующей итерации сравнивалась с буквой подстроки равной ей
                    else:
                        delta_i_str = d[sub_str[i_sub_str]]
                        # а вот тут у нас есть знания о том,что прошлые буквы(подстроки) прошли сравнение успешно
                        # и среди них нет сраниваемой буквы и тогда делаем перемещение,чтобы
                        # не попала текуще сраниваемая буква в промежуток,где мы сравнивнили буквы

                    i_str += delta_i_str  # смещение счетчика строки
                    is_Not_right = True  # есnm ли несовпадение символа
                    break

                delta_for_compare += 1  # потом сравниваем следую с конца буквы подстроки со строчной

            if not is_Not_right:  # если дошли до начала образа, значит, все его символы совпали
                return i_str - delta_for_compare + 1
        else:
            return -1  # не нашли ничего

    def find_substring_in_string(self, str, sub_str):
        if self.is_correct_data(str, sub_str):
            return BoeraMurraHorspulaAlgorithm.__algoritm_boera_murra_horspula(str, sub_str)
        return None


if __name__ == "__main__":
    algorithm = BoeraMurraHorspulaAlgorithm()
    print(algorithm.find_substring_in_string('abcdefg', 'de'))
    print(algorithm.find_substring_in_string('abdefcdefg', 'cd'))
