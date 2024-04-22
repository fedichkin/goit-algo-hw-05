import sys
from colorama import Fore, Style


def parse_log_line(line: str) -> dict:
    date, time, level, message = line.split(' ', 3)

    return {'date': date, 'time': time, 'level': level, 'message': message}


def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r') as file:
            logs = [parse_log_line(el.strip()) for el in file.readlines()]
    except FileNotFoundError:
        print('File is not found')
        exit(0)
    except OSError:
        print('Error reading file')
        exit(0)

    return logs


def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda el: el['level'].lower() == level.lower(), logs))


def count_logs_by_level(logs: list) -> dict:
    stat = {'info': 0, 'error': 0, 'debug': 0, 'warning': 0}

    for log in logs:
        stat[log['level'].lower()] += 1

    return stat


# set color of text for every level of log
def display_level(level: str) -> str:
    match level.upper():
        case 'INFO':
            return f'{Fore.BLUE}{level.upper()}{Style.RESET_ALL}'
        case 'ERROR':
            return f'{Fore.RED}{level.upper()}{Style.RESET_ALL}'
        case 'DEBUG':
            return f'{Fore.GREEN}{level.upper()}{Style.RESET_ALL}'
        case 'WARNING':
            return f'{Fore.YELLOW}{level.upper()}{Style.RESET_ALL}'
        case _:
            return level


def display_log_counts(counts: dict):
    print('Рівень логування | Кількість')
    print('-----------------|----------')
    for level, count in counts.items():
        # gel level with color
        level_label = display_level(level)
        # calc max number of symbols in the column, color label include more symbols than simple level,
        # but symbols of colors is not visible
        # column width is 17 symbols
        max_symbols = len(level_label) - len(level) + 17
        print(f'{level_label: <{max_symbols}}| {count}')


def display_select_levels_logs(level: str, logs: list):
    print(f'Деталі логів для рівня "{display_level(level)}":')
    for item in logs:
        print(f'{item['date']} {item['time']} - {item['message']}')


def main():
    if len(sys.argv) < 2:
        print('The path to the log file is not specified')
        exit(0)

    path = sys.argv[1]
    select_level = sys.argv[2] if len(sys.argv) > 2 else None

    list_logs = load_logs(path)
    statistics = count_logs_by_level(list_logs)
    display_log_counts(statistics)

    # if set second argument get logs of this level and show
    if select_level:
        select_level_logs = filter_logs_by_level(list_logs, select_level)
        print('\v')
        display_select_levels_logs(select_level, select_level_logs)


if __name__ == '__main__':
    main()
