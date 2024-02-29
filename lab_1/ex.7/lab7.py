# 7. Победители Мирового чемпионата. Создайте файл с именем WorldSeriesWinners.txt. 
# Он должен содержит хронологический список командпобедителей Мирового чемпионата по футболу с 1950 по 2023 год. 
# (Первая строка в файле является названием команды, которая победила в 1950 году, последняя строка - названием команды, которая победила в 2023 году. 
# Предположим, что Мировой чемпионат не проводился в 1904 и 1994 годах. В файле должны быть соответствующие пометки, указывающие на это) 
# Напишите программу, которая читает этот файл и создает словарь, в котором ключи -это названия команд, 
# а связанные с ними значения - количество побед команды в Мировом чемпионате. Программа также должна создать словарь, в котором ключи - это годы,
# а связанные с ними значения - названия команд, которые побеждали в том году. Программа должна предложить пользователю ввести год 
# в диапазоне между 1950 и 2023 годами и вывести название команды, которая выиграла Мировой чемпионат по футболу в том году и количество побед команды в Мировом чемпионате.


def read_world_series_winners(file_path):    
    winners_by_team = {}
    winners_by_year = {}
    with open(file_path, 'r', encoding='utf-8') as file:        
        lines = file.readlines()
    for year, line in enumerate(lines, start=1950):
        # Пропускаем года, в которые чемпионат не проводился        
        if year == 1904 or year == 1994:
            continue
        winner = line.strip()        
        # Обновляем словарь с количеством побед для каждой команды        
        winners_by_team[winner] = winners_by_team.get(winner, 0) + 1
        # Обновляем словарь с победителями по годам
        winners_by_year[year] = winner
    return winners_by_team, winners_by_year

def main():
    file_path = 'WorldSeriesWinners.txt'  # Укажите путь к вашему файлу
    winners_by_team, winners_by_year = read_world_series_winners(file_path)
    # Выводим возможные года и 1запрашиваем у пользователя ввод
    available_years = range(1950, 2024)
    user_year = int(input(f"Введите год ({min(available_years)}-{max(available_years)}): "))
    if user_year in available_years:
        winning_team = winners_by_year[user_year]
        wins_count = winners_by_team[winning_team]
        print(f"\nВ {user_year} году победила команда: {winning_team}")
        print(f"Общее количество их побед в чемпионатах: {wins_count}")
    else:
        print("Введенный год не входит в допустимый диапазон.")

if __name__ == "__main__":
    main()
