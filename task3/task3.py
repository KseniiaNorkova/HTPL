import json


def make_report(tests_path, values_path, report_path):
    """функция для заполнения отчета данными файла values на основе структуры tests"""
    with (open(tests_path, 'r') as f1,
          open(values_path, 'r') as f2):
        tests_f = json.load(f1)
        values_f = json.load(f2)  # приведение json файлов к формату для python

    values_d = {item['id']: item['value'] for item in values_f['values']}  # создание словаря со значениями из values

    def fill_values(test_data):
        '''рекурсивно заполняет недостающие значения в tests'''
        for i in test_data:
            i['value'] = values_d.get(i['id'], "")
            if 'values' in i:
                fill_values(i['values'])

    fill_values(tests_f['tests'])

    with open(report_path, 'w') as f3:
        json.dump(tests_f, f3, indent=4)  # создание/заполнение файла report


file_tests, file_values, file_report = input(), input(), input()
make_report(file_tests, file_values, file_report)

