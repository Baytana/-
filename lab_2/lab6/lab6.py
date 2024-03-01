# 6. Среднее арифметическое чисел. Допустим, что файл с рядом целых чисел называется numbers.txt и 
# существует на диске компьютера. Напишите программу, которая вычисляет среднее арифметическое всех 
# хранящихся в файле чисел.


file_name = 'numbers.txt'

try:
    with open(file_name, 'r') as file:
        total_sum = 0
        count = 0

        for line in file:
            number = int(line.strip())
            total_sum += number
            count += 1

        average = total_sum / count if count > 0 else 0

        print(f"The average of numbers in the file {file_name} is: {average}")

except FileNotFoundError:
    print(f"The file {file_name} was not found.")
