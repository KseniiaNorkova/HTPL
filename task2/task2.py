import argparse


parser = argparse.ArgumentParser(description="Проверяет вхождение точки в окружность")
parser.add_argument('file_1', type=str, help='Путь к файлу с координатами и радиусом окружности')
parser.add_argument('file_2', type=str, help='Путь к файлу с координатами точек')
args = parser.parse_args()

file_1 = args.file_1
file_2 = args.file_2

# file_1, file_2 = input(), input()

with open(file_1, 'rt', encoding='utf-8') as file_1:  # открытие 1 файла
    f1 = (line for line in file_1.readlines())  # построчное разделение файла
    x, y = map(int, next(f1).strip().split())  # извлечение координат центра окружности
    r = int(next(f1).strip())  # извлечение радиуса окружности

with open(file_2, 'rt', encoding='utf-8') as file_2:
    f2 = (line for line in file_2.readlines())

r = r ** 2  # приведение r к R

for line in f2:
    i, j = map(int, line.split())  # извлечение координат точки
    summ = (x - i) ** 2 + (y - j) ** 2  # формула для сравнения с R
    '''если summ больше r, значит точка вне окружности; если равно - на окружности, меньше - в'''
    if summ == r:
        print(0)
    elif summ < r:
        print(1)
    else:
        print(2)

