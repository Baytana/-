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
