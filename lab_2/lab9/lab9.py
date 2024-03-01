#9. Обработка исключений. Измените программу, которую вы написали для упражнения 6, таким образом, 
# чтобы она обрабатывала приведенные ниже исключения: • она должна обрабатывать любые исключения IOError, 
# которые вызываются, когда файл открыт, и данные из него считываются; • она должна обрабатывать любые исключения 
# ValueError, которые вызываются, когда прочитанные из файла значения конвертируются в числовой тип.

def read_random_numbers(file_name):
    try:
        with open(file_name, 'r') as file:
            random_numbers = [int(line.strip()) for line in file]
            return random_numbers

    except FileNotFoundError:
        print(f"The file {file_name} was not found.")
        return []

    except IOError as io_error:
        print(f"An IOError occurred while reading the file: {io_error}")
        return []

    except ValueError as value_error:
        print(f"ValueError: {value_error}")
        return []

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

def main():
    file_name1 = input("Enter the file name: ")+'.txt'
    file_name= '../lab6/'+file_name1
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
