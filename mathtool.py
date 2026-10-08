import sys
import math

MAX_VALUE = 10000

HELP_TEXT = """mathtool - решение уравнений вида A*x^2 + B*x + C = 0

Использование:
  python3 mathtool.py                       вывод справки
  python3 mathtool.py --help                 вывод справки
  python3 mathtool.py solve                  ввод коэффициентов с клавиатуры
  python3 mathtool.py solve -a 1 -b -3 -c 2  решение с заданными коэффициентами

Коэффициенты A, B, C - целые числа, по модулю не превышающие 10000."""


def parse_arguments():
    args = sys.argv[1:]

    if len(args) == 0 or args[0] == "--help":
        print(HELP_TEXT)
        sys.exit(0)

    if args[0] != "solve":
        print("ОШИБКА: неизвестная команда", file=sys.stderr)
        sys.exit(1)

    if len(args) == 1:
        # только "solve" - вводим с клавиатуры
        return None

    if len(args) == 7 and args[1] == "-a" and args[3] == "-b" and args[5] == "-c":
        return args[2], args[4], args[6]

    print("ОШИБКА: неверный набор параметров", file=sys.stderr)
    sys.exit(1)


def read_from_keyboard():
    a_str = input("Введите A: ")
    b_str = input("Введите B: ")
    c_str = input("Введите C: ")
    return a_str, b_str, c_str


def convert_to_int(a_str, b_str, c_str):
    try:
        a = int(a_str)
        b = int(b_str)
        c = int(c_str)
    except ValueError:
        print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
        sys.exit(1)
    return a, b, c


def check_range(a, b, c):
    if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
        print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
        sys.exit(1)


def solve_linear(b, c):
    if b != 0:
        print("Уравнение линейное")
        x = -c / b
        print(f"x = {x:.3f}")
    else:
        print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
        sys.exit(1)


def solve_quadratic(a, b, c):
    print("Уравнение квадратное")

    d = b * b - 4 * a * c
    print(f"D = {d}")

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"x1 = {x1:.3f}")
        print(f"x2 = {x2:.3f}")
    elif d == 0:
        x = -b / (2 * a)
        print(f"x = {x:.3f}")
    else:
        print("Действительных корней нет")


def main():
    parsed = parse_arguments()

    if parsed is None:
        a_str, b_str, c_str = read_from_keyboard()
    else:
        a_str, b_str, c_str = parsed

    a, b, c = convert_to_int(a_str, b_str, c_str)
    check_range(a, b, c)

    if a == 0:
        solve_linear(b, c)
    else:
        solve_quadratic(a, b, c)

    sys.exit(0)


if __name__ == "__main__":
    main()