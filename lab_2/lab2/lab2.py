#2. Вывод на экран верхней части файла. Напишите программу, которая запрашивает у пользователя имя файла. 
# Программа должна вывести на экран только первые пять строк содержимого файла. Если в файле меньше пяти строк, 
# то она должна вывести на экран все содержимое файла.

file_name = input("Enter the file name: ")+".txt"

try:
    with open(file_name, 'r') as file:
        lines = file.readlines()[:5]

        for line in lines:
            print(line, end='')

except FileNotFoundError:
    print(f"The file {file_name} was not found.")
