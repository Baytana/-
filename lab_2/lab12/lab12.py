#12. Среднее количество шагов. Браслет для занятий спортом - это носимое устройство, которое отслеживает вашу 
# физическую активность, количество сожженных калорий, сердечный ритм, модели сна и т. д. Одним из самых
# распространенных видов физический активности, который отслеживает большинство таких устройств, является количество 
# шагов, которые вы делаете каждый день. Среди исходного кода главы 6 вы найдете файл steps.txt. Этот файл содержит
# количество шагов, которые человек делал каждый день в течение года. В файле 365 строк, и каждая строка содержит 
# количество шагов, сделанных в течение дня. (Первая строка - это число шагов, сделанных 1 января, вторая строка- 
# число шагов, сделанных 2 января, и т. д.) Напишите программу, которая читает файл и за тем выводит среднее 
# количество шагов, сделанных в течение каждого месяца. (Данные были записаны в год, который не был високосным, 
# и поэтому февраль имеет 28 дней.)

import random

def read_steps_data(file_path):
    try:
        with open(file_path, 'r') as file:
            steps_data = [int(line.strip()) for line in file.readlines()]
        return steps_data
    except FileNotFoundError:
        print(f"\nFile '{file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return None

def generate_random_numbers(num_count, min_value, max_value):
    random_numbers = [random.randint(min_value, max_value) for _ in range(num_count)]
    return random_numbers

def write_random_numbers_to_file(file_path, random_numbers):
    try:
        with open(file_path, 'w') as file:
            for num in random_numbers:
                file.write(str(num) + '\n')
        print(f"\nRandom numbers written to '{file_path}' successfully.")
    except Exception as e:
        print(f"An error occurred while writing the file: {e}")

def calculate_monthly_average(steps_data):
    if not steps_data:
        return None

    months = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31, "June": 30,
              "July": 31, "August": 31, "September": 30, "October": 31, "November": 30, "December": 31}

    monthly_totals = {month: 0 for month in months}
    monthly_days = {month: 0 for month in months}

    current_month = "January"

    for i, steps in enumerate(steps_data, start=1):
        monthly_totals[current_month] += steps
        monthly_days[current_month] += 1

        if i % months[current_month] == 0:
            current_month = list(months.keys())[(list(months.keys()).index(current_month) + 1) % 12]

    monthly_averages = {month: monthly_totals[month] / monthly_days[month] for month in months}

    return monthly_averages

def main():
    file_path = "steps.txt"
    num_count = 365
    min_value = 200
    max_value = 6000

    random_numbers = generate_random_numbers(num_count, min_value, max_value)
    write_random_numbers_to_file(file_path, random_numbers)
    
    steps_data = read_steps_data(file_path)

    if steps_data:
        monthly_averages = calculate_monthly_average(steps_data)

        if monthly_averages:
            print("Average number of steps per month:")
            for month, average in monthly_averages.items():
                print(f"{month}: {average:.2f}")

if __name__ == "__main__":
    main()
