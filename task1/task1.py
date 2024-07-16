import argparse


parser = argparse.ArgumentParser(description="Выводит массив из первых элементов интервалов")
parser.add_argument('n', type=int, help='Размер массива (от 1 до n)')
parser.add_argument('m', type=int, help='Длина интервала')
args = parser.parse_args()

n = args.n
m = args.m

round_array = [*range(1, n + 1)] * m  # создается список элементов, образующих круговой массив
answer = ''  # переменная для вывода

for ind, i in enumerate(round_array):
    if not ind % (m - 1):  # проверяем кратность индекса числу m
        '''если в ответе уже есть хотя бы один элемент, проверяем является ли следующий единицей'''
        if len(answer) > 1 and i == 1:
            break  # прерываем цикл, если проверка не прошла
        answer += str(i)  # если все проверки прошли, в ответ добавляем элемент

print(answer)  # вывод ответа
