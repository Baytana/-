file_name = input("Enter the file name: ")+'.txt'

try:
    with open(file_name, 'r') as file:
        lines = file.readlines()

        for i, line in enumerate(lines, start=1):
            print(f"{i}: {line}", end='')

except FileNotFoundError:
    print(f"The file {file_name} was not found.")