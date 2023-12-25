from AlgoritmFindSubstringInString import AlgoritmFindSubstringInString as algorithm


class SimpleAlgorithm(algorithm):
    """
        Наивный алгоритм поиска подстроки в строке. Имеет сложность O(m*n).
        Обычно нигде не используется,так как есть алгоритмы лучше и несильно сложнее
    """
    @staticmethod
    def __simple_algorithm(string, sub_string):
        for i_str in range(len(string)-len(sub_string)+1):
            flag = False
            for i_sub_str in range(len(sub_string)):
                if string[i_str + i_sub_str] != sub_string[i_sub_str]:
                    flag = True
                    break
            if flag:
                continue
            return i_str
        return -1

    def find_substring_in_string(self, str, sub_str):
        if self.is_correct_data(str, sub_str):
            return SimpleAlgorithm.__simple_algorithm(str, sub_str)
        return None



if __name__=="__main__":
    algorithm = SimpleAlgorithm()
    print(algorithm.find_substring_in_string('abcdefg', 'de'))
    print(algorithm.find_substring_in_string('abdefcdefg', 'cd'))
