#5. Сумма чисел. Допустим, что файл с рядом целых чисел называется numbers.txt и существует на диске компьютера. 
# Напишите программу, которая читает все хранящиеся в файле числа и вычисляет их сумму.

file_name = 'numbers.txt'

try:
    with open(file_name, 'r') as file:
        total_sum = 0

        for line in file:
            number = int(line.strip())
            total_sum += number

        print(f"The sum of numbers in the file {file_name} is: {total_sum}")

except FileNotFoundError:
    print(f"The file {file_name} was not found.")
