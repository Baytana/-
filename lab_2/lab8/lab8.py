#8. Программа чтения файлов со случайными числами. Выполнив предыдущее задание (программу записи файла со 
# случайными числами), напишите еще одну программу, которая читает случайные числа из файла, выводит их на экран и 
# затем показывает приведенные ниже данные: • сумму чисел; • количество случайных чисел, прочитанных из файла.

def read_random_numbers(file_name):
    try:
        with open(file_name, 'r') as file:
            random_numbers = [int(line.strip()) for line in file]
            return random_numbers

    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
        return []

    except Exception as e:
        print(f"An error occurred: {e}")
        return []

def main():
    file_name1 = input("Enter the file name: ")+'.txt'
    file_name='../lab7/'+file_name1
    random_numbers = read_random_numbers(file_name)

    if random_numbers:
        print("Random numbers:")
        for number in random_numbers:
            print(number)

        total_sum = sum(random_numbers)
        count = len(random_numbers)

        print(f"\nSum of numbers: {total_sum}")
        print(f"Number of random numbers read from the file: {count}")

if __name__ == "__main__":
    main()
