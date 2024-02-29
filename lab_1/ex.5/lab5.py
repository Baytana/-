#5. Частота слов. Напишите программу, которая считывает содержимое текстового файла. 
# Она должна создать словарь, в котором ключами являются отдельные слова в файле, а значениями - 
# количество появлений каждого слова. Например, если слово 'это' появляется 128 раз, то словарь должен 
# содержать элемент с ключом 'это' и значением 128. Программа должна либо показать частотность каждого слова, 
# либо создать второй файл, содержащий список слов и их частот.

def count_word_frequency(file_path):
    word_freq = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for i in file:
            words = i.split()
            for word in words:
                if word:
                    word = word.lower()  # приводим слово к нижнему регистру
                    if word in word_freq:
                        word_freq[word] += 1
                    else:
                        word_freq[word] = 1
    return word_freq


# def show_word_frequency(word_freq):
#     for word, freq in word_freq.items():
#         print(f'{word}: {freq}')


def save_word_frequency_to_file(word_freq, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, freq in word_freq.items():
            file.write(f'{word}: {freq}\n')


file_path = 'file_1.txt'
word_freq = count_word_frequency(file_path)
   
output_file = 'file_2.txt'
save_word_frequency_to_file(word_freq, output_file)
print('Cохранен в файле file_2.txt')
