#4. Счетчик значений. Допустим, что файл с серией имен (в виде строковых значений) называется names.txt 
#и существует на диске компьютера. Напишите программу, которая показывает количество хранящихся в файле имен. 
# (Подсказка: откройте файл и прочитайте каждую хранящуюся в нем строку. Используйте переменную для подсчета 
# количества прочитанных из файла значений.)


file_name = 'names.txt'

try:
    with open(file_name, 'r') as file:
        names_count = 0

        for line in file:
            names_count += 1

        print(f"The number of names in the file {file_name} is: {names_count}")

except FileNotFoundError:
    print(f"The file {file_name} was not found.")