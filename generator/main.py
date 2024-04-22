import re
from typing import Callable


# this generator gives one number at a time to save memory
def generator_numbers(text: str):
    while True:
        # we are looking only for the first occurrence, the generator may not request the next number
        match = re.search(r'\s(\d+\.?\d*)\s', text)
        if not match:
            break
        yield float(match.group(1))
        # cut off the text, leaving only the part in which you have not yet searched
        next_start_search_index = match.span()[1]
        text = text[next_start_search_index:]


def sum_profit(text: str, func: Callable):
    sum = 0
    for number in func(text):
        sum += number

    return sum


def main():
    text = 'Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, ' \
           'доповнений додатковими надходженнями 27.45 і 324.00 доларів.'
    total_income = sum_profit(text, generator_numbers)
    print(f"Загальний дохід: {total_income}")


if __name__ == '__main__':
    main()
