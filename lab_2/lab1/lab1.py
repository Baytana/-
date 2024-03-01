with open('number.txt', 'r') as file:
    lines = file.readlines()

    for line in lines:
        numbers = line.split()

        for number in numbers:
            print(number)