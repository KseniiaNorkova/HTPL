file_name = input()  # получение пути к файлу

with open(file_name, 'rt', encoding='utf-8') as file:  # открытие файла
    '''извлечение данных и приведение их к списку чисел'''
    numbers = [int(line.strip()) for line in file.readlines()]

count = 0  # переменная-счетчик (будущий ответ)
numbers.sort()  # сортировка списка

while len(set(numbers)) > 1:  # проверка на равенство элементов
    for i in range(len(numbers)):
        if numbers[i] < numbers[-i - 1]:  # если i элемент меньше противоположного, то он увеличивается на 1
            numbers[i] += 1
            count += 1
            if numbers[i] < numbers[-i - 1]:  # если i элемент все еще меньше противоположного, то -i-1 уменьшается на 1
                numbers[-i - 1] -= 1
                count += 1
        if i > 1 and numbers[i] < numbers[i - 1]:  # проверка для изменения элементов в нечетных последовательностях
            numbers[i] += 1
            count += 1

print(count)
