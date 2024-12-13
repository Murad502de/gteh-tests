import requests
from test.calculators.authorization.auth_google_table import get_access_token


def get_sheet_data(spreadsheet_id):
    access_token = get_access_token()
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json',
    }
    response = requests.get(f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}', headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


def read_sheet(spreadsheet_id, range_name):
    access_token = get_access_token()
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json',
    }
    response = requests.get(f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range_name}',
                            headers=headers)
    if response.status_code == 200:
        return response.json().get('values', [])
    else:
        response.raise_for_status()


def update_sheet(spreadsheet_id, range_name, values):
    access_token = get_access_token()
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    body = {
        'range': range_name,
        'majorDimension': 'ROWS',
        'values': values,
    }
    response = requests.put(
        f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range_name}?valueInputOption=RAW',
        headers=headers, json=body)
    if response.status_code == 200:
        return response.json()
    else:
        response.raise_for_status()


# Найти ячейку по тексту
def find_cell_with_text(spreadsheet_id, sheet_name, text):
    data = get_sheet_data(spreadsheet_id)
    sheet = next(sheet for sheet in data['sheets'] if sheet['properties']['title'] == sheet_name)
    for row_idx, row in enumerate(sheet['data'][0]['rowData']):
        for col_idx, cell in enumerate(row.get('values', [])):
            if cell.get('formattedValue') == text:
                return row_idx, col_idx
    return None, None


def read_value_next_to_cell(spreadsheet_id, sheet_name, row, col, direction):
    """
    Считывает значение из ячейки, расположенной справа или снизу от указанной ячейки.

    :param spreadsheet_id: ID Google Sheets документа.
    :param sheet_name: Имя листа в документе.
    :param row: Строка начальной ячейки.
    :param col: Колонка начальной ячейки.
    :param direction: Направление поиска ('right' или 'down').
    :return: Значение ячейки или None, если ячейка не найдена.
    """
    if direction not in ['right', 'down']:
        raise ValueError("direction must be 'right' or 'down'")

    range_name = None
    if direction == 'right':
        range_name = f'{sheet_name}!{chr(ord("A") + col + 1)}{row + 1}'
    elif direction == 'down':
        range_name = f'{sheet_name}!{chr(ord("A") + col)}{row + 2}'
    return read_sheet(spreadsheet_id, range_name)


def read_value_at_intersection(spreadsheet_id, sheet_name, row, col):
    range_name = f'{sheet_name}!{chr(ord("A") + col)}{row + 1}'
    return read_sheet(spreadsheet_id, range_name)


def update_value_at_intersection(spreadsheet_id, sheet_name, row, col, new_value):
    range_name = f'{sheet_name}!{chr(ord("A") + col)}{row + 1}'
    update_sheet(spreadsheet_id, range_name, [[new_value]])
