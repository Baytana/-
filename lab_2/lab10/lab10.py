#10. Очки в игре в гольф. Любительский гольф-клуб проводит турниры каждые выходные. Президент клуба попросил вас 
# написать две программы: • программу, которая читает имя каждого игрока и его счет в игре, вводимые с клавиатуры, 
# и затем сохраняет их в виде записей в файле golf.txt (каждая запись будет иметь поле для имени игрока и поле для 
# счета игрока); • программу, которая читает записи из файла golf.txt и выводит их на экран.

def write_golf_scores():
    try:
        with open("golf.txt", "w") as file:
            while True:
                player_name = input("Enter player's name (or 'q' to quit): ")
                if player_name.lower() == 'q':
                    break

                try:
                    player_score = int(input("Enter player's golf score: "))
                    file.write(f"{player_name}: {player_score}\n")
                except ValueError:
                    print("Invalid input. Please enter a valid integer for the golf score.")

    except IOError as io_error:
        print(f"An IOError occurred while writing to the file: {io_error}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def read_golf_scores():
    try:
        with open("golf.txt", "r") as file:
            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("The file 'golf.txt' was not found.")

    except IOError as io_error:
        print(f"An IOError occurred while reading the file: {io_error}")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    print("Golf Score Management System")
    print("1. Enter golf scores")
    print("2. Display golf scores")
    print("3. Quit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        write_golf_scores()
    elif choice == '2':
        read_golf_scores()
    elif choice == '3':
        print("Program terminated.")
    else:
        print("Invalid choice. Please enter a number from 1 to 3.")

if __name__ == "__main__":
    main()
