import json
import argparse


parser = argparse.ArgumentParser(description="Проверяет вхождение точки в окружность")
parser.add_argument('tests_path', type=str, help='Путь к файлу tests.json')
parser.add_argument('values_path', type=str, help='Путь к файлу values.json')
parser.add_argument('report_path', type=str, help='Путь к файлу report.json')
args = parser.parse_args()

tests_path = args.tests_path
values_path = args.values_path
report_path = args.report_path

# tests_path, values_path, report_path = input(), input(), input()


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


make_report(tests_path, values_path, report_path)

