#7. Программа записи файла со случайными числами. Напишите программу, которая пишет в файл ряд случайных чисел. 
# Каждое случайное число должно быть в диапазоне от 1 до 500. Приложение должно предоставлять пользователю возможность
# назначать количество случайных чисел, которые будут содержаться в файле.


import random

def write_random_numbers(file_name, count):
    try:
        with open(file_name, 'w') as file:
            for _ in range(count):
                random_number = random.randint(1, 500)
                file.write(f"{random_number}\n")
        print(f"{count} random numbers have been written to {file_name}.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    file_name = input("Enter the file name: ")+'.txt'

    try:
        count = int(input("Enter the number of random numbers to generate: "))
        if count <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    write_random_numbers(file_name, count)

if __name__ == "__main__":
    main()
