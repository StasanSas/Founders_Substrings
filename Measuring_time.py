import time
import os
import matplotlib.pyplot as plt
from BoeraMurraHorspulaAlgorithm import BoeraMurraHorspulaAlgorithm
from KnuthMorrisPrathAlgorithm import KnuthMorrisPrathAlgorithm
from HashAlgorithm import HashAlgorithm
from SimpleAlgorithm import SimpleAlgorithm


class InfoAlgorithm:

    def __init__(self, algorithm, color, label):
        self.algorithm = algorithm
        self.color = color
        self.label = label

def read_file(adress):
    with open(adress, 'r', encoding="utf-8") as f:
        text = f.read()
    return text

def file_parse(path_file, strart, end, amount_files):
    result = {}
    for i in range(1, amount_files + 1):
        real_path_str = os.path.abspath(path_file + "_{}.txt".format(i))
        string = read_file(real_path_str)
        start_substring = int((strart * len(string)) // 1000)
        end_substring = int((end * len(string)) // 1000)
        substring = string[start_substring: end_substring]
        result["str_{}".format(i)] = string
        result["sub_str_{}".format(i)] = substring
    return result




def measiring_time_algoritm(func, string, substring):
    start = time.time()
    func(string, substring)
    return time.time() - start


def write_documents_in_file(file):
    list_algorithms = [
        SimpleAlgorithm(),
        HashAlgorithm(),
        KnuthMorrisPrathAlgorithm(),
        BoeraMurraHorspulaAlgorithm()
    ]

    file.write("n - длина строки\nm - длина подстроки")
    file.write("\n")
    file.write("\n")
    file.write("""
синий - наивный алгоритм
черный - хэш алгоритм
красный - Кнута Морриса Прата алгоритм
зелёный - Боера Мура Хорспула алгоритм
    """)
    file.write("\n")
    file.write("\n")
    for algorithm in list_algorithms:
        file.write(algorithm.__class__.__name__)
        file.write("\n")
        file.write(algorithm.__doc__)
        file.write("\n")
    file.write("\n")
    file.write("\n")

def summa(list_values):
    sum = 0
    for value in list_values:
        sum+=value
    return sum

def get_delta(list_values, coef):
    average = summa(list_values) / len(list_values)
    sum = 0
    for value in list_values:
        sum += (value-average)*(value-average)
    s = (sum / (len(list_values) - 1)) ** 0.5
    delta = coef * (s / (len(list_values) ** 0.5))
    return delta

def parse_points(list_points):
    list_x = []
    list_average_points = []
    list_average_points_minus_delta = []
    list_average_points_plus_delta =[]
    for tup in list_points:
        list_x.append(tup[0])
        list_average_points_minus_delta.append(tup[1])
        list_average_points.append(tup[2])
        list_average_points_plus_delta.append(tup[3])
    return (list_x, list_average_points_minus_delta, list_average_points, list_average_points_plus_delta)


def analiz_one_point(algorithm_info, data, coef, amount_file):
    time_list = []
    for i in range(1, amount_file+1):
        func = algorithm_info.algorithm.find_substring_in_string
        time_list.append(measiring_time_algoritm(func, data["str_{}".format(i)], data["sub_str_{}".format(i)]))
    average = summa(time_list) / len(time_list)
    delta = get_delta(time_list, coef)
    return average, delta

def analiz_delta_string(path, algorithm_info, start_string, step):
    list_points = []
    string_for_file = ''
    for j in range(start_string, 1000, step):
        data = file_parse(path, j, j + 1, 16)  # от 1000
        average, delta = analiz_one_point(algorithm_info, data, 2.1314, 16)
        list_points.append((j/10, average - delta, average, average + delta))
        if j+step > 1000:
            string_for_file = algorithm_info.algorithm.__class__.__name__ + "  --  {} / +- {}\n".format(average, delta)
    return list_points, string_for_file


def analiz_delta_sub_string(path, algorithm_info, sub_string, step):
    list_points = []
    string_for_file = ''
    for j in range(sub_string, 30, step):
        data = file_parse(path, 500, 500 + j, 16)  # от 1000
        average, delta = analiz_one_point(algorithm_info, data, 2.1314, 16)
        list_points.append((j/10, average - delta, average, average + delta))
        if j+step > 30:
            string_for_file = algorithm_info.algorithm.__class__.__name__ + "  --  {} / +- {}\n".format(average, delta)
    return list_points, string_for_file

def analiz_delta_sub_string_for_worst_data(path, algorithm_info, sub_string, step):
    list_points = []
    string_for_file = ''
    for j in range(sub_string, 30, step):
        data = file_parse(path, 500-((1+j)/200), 500 + ((1+j)/200), 6)  # от 1000
        average, delta = analiz_one_point(algorithm_info, data, 2.5706, 6)
        list_points.append((j/10, average - delta, average, average + delta))
        if j+step > 30:
            string_for_file = algorithm_info.algorithm.__class__.__name__ + "  --  {} / +- {}\n".format(average, delta)
    return list_points, string_for_file


def measiring_one_folder(path, file, ax, start, step, analiz_delta, title):
    list_algorithms = [
        InfoAlgorithm(SimpleAlgorithm(), 'b', "Simple"),
        InfoAlgorithm(HashAlgorithm(), 'black', "Hash"),
        InfoAlgorithm(KnuthMorrisPrathAlgorithm(), 'r', "KnuthMorrisPrath"),
        InfoAlgorithm(BoeraMurraHorspulaAlgorithm(), 'g', "BoerMurrHorspul")
    ]
    #  холостые запуски
    for algorithm_info in list_algorithms:
        algorithm_info.algorithm.find_substring_in_string("aaaaaaabbbbgcisaon", "bgci")

    type_analiz = analiz_delta.__name__
    file.write("{}\n\n".format(title))

    for algorithm_info in list_algorithms:
        list_points, string_for_file = analiz_delta(path, algorithm_info, start, step)
        file.write(string_for_file)
        tup_list = parse_points(list_points)
        color = algorithm_info.color
        ax.plot(tup_list[0], tup_list[1], color=color, linestyle=':', marker='^', alpha=0.5)
        ax.plot(tup_list[0], tup_list[2], color=color, linestyle='-', marker='o')
        ax.plot(tup_list[0], tup_list[3], color=color, linestyle=':', marker='^', alpha=0.5)
    ax.set_xlabel("Длина (под-)строки в %")
    ax.set_ylabel("время")
    ax.set_title(title)
    file.write("\n\n")

if __name__=="__main__":
    desktop = os.path.expanduser("~\Desktop")
    new_file = open(desktop + "\\Measuring_time.txt", "w+")
    write_documents_in_file(new_file)

    f, axs = plt.subplots(3, 2)
    measiring_one_folder("Data/real_text/real_text",
                         new_file, axs[0, 0], 200, 150, analiz_delta_string,
                         "Реальный текст(изменение длины строки)")
    print(1)
    measiring_one_folder("Data/recurring_sequences/recurring_sequences",
                         new_file, axs[1, 0], 200, 150, analiz_delta_string,
                         "Текст,похожий на расшифрованное днк (изменение длины строки)")
    print(2)
    measiring_one_folder("Data/many_different_simbols/many_different_simbols",
                         new_file, axs[2, 0], 200, 150, analiz_delta_string,
                         "Текст,где сного самых разных символов (изменение длины строки)")
    print(3)
    measiring_one_folder("Data/worst_data/worst_data",
                         new_file, axs[0, 1], 1, 5, analiz_delta_sub_string_for_worst_data,
                         "Данные,на которых работает медленно наивный алгоритм (изменение длины подстроки)")
    print(4)
    measiring_one_folder("Data/recurring_sequences/recurring_sequences",
                         new_file, axs[1, 1], 1, 5, analiz_delta_sub_string,
                         "Текст,похожий на расшифрованное днк (изменение длины подстроки)")
    print(5)
    measiring_one_folder("Data/many_different_simbols/many_different_simbols",
                         new_file, axs[2, 1], 1, 5, analiz_delta_sub_string,
                         "Текст,где сного самых разных символов (изменение длины подстроки)")

    new_file.close()
    plt.show()




