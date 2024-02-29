#6. Анализ файла. Напишите программу, которая читает содержимое двух текстовых файлов и сравнивает их следующим образом: 
# • показывает список всех уникальных слов, содержащихся в обоих файлах; • показывает список слов, входящих в оба файла; 
# • показывает список слов из первого файла, не входящих во второй; •показывает список слов из второго файла, не входящих в первый; 
# •показывает список слов, входящих либо в первый, либо во второй файл, но не входящих в оба файла одновременно. 
# Подсказка: для выполнения этого анализа используйте операции над множествами.

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        words = file.read().split()
        return set(words)


def main(file1_path, file2_path):
    words_file1 = read_file(file1_path)
    words_file2 = read_file(file2_path)


    # Показывает список всех уникальных слов
    all_unique_words = words_file1.union(words_file2)
    print("Список всех уникальных слов:")
    print(sorted(all_unique_words))
    # Показывает список слов, входящих в оба файла
    common_words = words_file1.intersection(words_file2)
    print("\nСписок слов, входящих в оба файла:")
    print(sorted(common_words))
    # Показывает список слов из первого файла, не входящих во второй
    words_only_in_file1 = words_file1.difference(words_file2)
    print("\nСписок слов из первого файла, не входящих во второй:")
    print(sorted(words_only_in_file1))
    # Показывает список слов из второго файла, не входящих в первый
    words_only_in_file2 = words_file2.difference(words_file1)
    print("\nСписок слов из второго файла, не входящих в первый:")
    print(sorted(words_only_in_file2))
    # Показывает список слов, входящих либо в первый, либо во второй файл, но не в оба файла одновременно
    words_either_in_file1_or_file2_but_not_both = words_file1.symmetric_difference(words_file2)
    print("\nСписок слов, входящих либо в первый, либо во второй файл, но не в оба файла одновременно:")
    print(sorted(words_either_in_file1_or_file2_but_not_both))


file1_path = "file_1.txt"
file2_path = "file_2.txt"
main(file1_path, file2_path)