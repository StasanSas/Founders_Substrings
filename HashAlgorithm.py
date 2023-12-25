from AlgoritmFindSubstringInString import AlgoritmFindSubstringInString as algorithm


class HashAlgorithm(algorithm):
    """
        Немного улучшенный наивный алгоритм . Тоже Имеет сложность O(m*n).
        Однако имеет преимущество за счёт использования хэша. Имеет сложность O(m+n),если колизии никогда не просходят
        и с учётом предварительной обработки.
    """
    @staticmethod
    def __start_found(string, sub_string):
        hash_str = 0
        hash_sub_str = 0
        len_substring = len(sub_string)
        for i in range(len_substring):
            hash_str += ord(string[i])
            hash_sub_str += ord(sub_string[i])
        return hash_str, hash_sub_str

    @staticmethod
    def __hash_algorithm(string, sub_string):
        tup = HashAlgorithm.__start_found(string, sub_string)
        hash_str = tup[0]
        hash_sub_str = tup[1]
        len_substring = len(sub_string)
        len_string = len(string)
        for i_str in range(len(string)):
            if hash_str == hash_sub_str:
                if sub_string == string[i_str:i_str + len_substring]:
                    return i_str
            hash_str -= ord(string[i_str])
            if i_str + len_substring >= len_string:
                return -1
            hash_str += ord(string[i_str + len_substring])

    def find_substring_in_string(self, str, sub_str):
        if self.is_correct_data(str, sub_str):
            return HashAlgorithm.__hash_algorithm(str, sub_str)
        return None

if __name__=="__main__":
    algorithm = HashAlgorithm()
    print(algorithm.find_substring_in_string('abcdefg', 'de'))
    print(algorithm.find_substring_in_string('abdefcdefg', 'cd'))
