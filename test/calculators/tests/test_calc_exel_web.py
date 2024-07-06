# import pytest
from test.calculators.action.sheets import read_sheet, update_sheet

# class MyTestCase():
#     def test_and_restore(spreadsheet_id, range_name, test_values):
#         # Сохранение исходных значений
#         original_values = read_sheet(spreadsheet_id, range_name)
#         print(f'Исходные значения: {original_values}')
#
#         # Изменение значений для тестирования
#         update_sheet(spreadsheet_id, range_name, test_values)
#         print(f'Новые значения для тестирования: {test_values}')
#
#         # Ваши тесты здесь
#         # ...
#
#         # Восстановление исходных значений
#         update_sheet(spreadsheet_id, range_name, original_values)
#         print(f'Значения восстановлены до: {original_values}')


# if __name__ == '__main__':
# Пример использования
spreadsheet_id = '1n2a5EVw-ahSbhWFijF_IOzA40ZOYGglK5rSfuowSOKs'
range_name = 'Тестовая - расчет М30!A1'

# Чтение данных
data = read_sheet(spreadsheet_id, range_name)
print(f'Старое значение: {data}')


