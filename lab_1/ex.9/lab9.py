#9. Словарный индекс. Напишите программу, которая читает содержимое текстового файла. Программа должна создать словарь, 
#в котором пары "ключ: значение" описаны следующим образом: • к л ю ч - ключами являются отдельные слова в файле; 
#• значение - каждое значение является списком, который содержит номера строк в файле, где найдено слово (ключ). 
#Например, предположим, что слово "робот" найдено в строках 7, 18, 94 и 138. Словарь будет содержать элемент, в котором 
#ключом будет строковое значение "робот", а значением - список, содержащий номера 7, 18, 94 и 138. После создания словаря 
#программа должна создать еще один текстовый файл, называемый словарным индексом, в котором приводится содержимое словаря.
#Словарный индекс должен содержать список слов в алфавитном порядке, хранящихся в словаре в качестве ключей, и номера строк, в которых эти слова встречаются в исходном файле.


def create_index(file_path):
    index = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            words = line.strip().split()
            for word in words:
                word = word.strip(',.?!;:"()').lower()  # Убираем пунктуацию и переводим в нижний регистр
                if word:
                    if word not in index:
                        index[word] = []
                    if line_num not in index[word]:
                        index[word].append(line_num)
    return index

def save_index(index, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for word in sorted(index.keys()):
            file.write(f"{word}: {', '.join(map(str, index[word]))}\n")

def main():
    input_file = 'input.txt'
    output_file = 'index.txt'

    index = create_index(input_file)
    save_index(index, output_file)
    print("Словарный индекс сохранен в файле 'index.txt'.")

if __name__ == "__main__":
    main()
