import pytest
from test.calculators.action.sheets import read_sheet, update_sheet

spreadsheet_id = '1n2a5EVw-ahSbhWFijF_IOzA40ZOYGglK5rSfuowSOKs'
sheet_name = 'Тестовая - расчет М30 (бэкап)'
range_name = 'A1:O32'


@pytest.fixture(scope="module")
def original_values():
    # Сохранение исходных данных перед началом тестов
    original = read_sheet(spreadsheet_id, range_name)
    print(f'Исходные значения: {original}')
    yield original
    # Восстановление исходных данных после завершения тестов
    update_sheet(spreadsheet_id, range_name, original)
    print(f'Значения восстановлены до: {original}')
