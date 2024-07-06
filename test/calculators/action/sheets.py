import requests
from test.calculators.authorization.auth_google_table import get_access_token


def read_sheet(spreadsheet_id, range_name):
    access_token = get_access_token()
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Accept': 'application/json',
    }
    response = requests.get(f'https://sheets.googleapis.com/v4/spreadsheets/{spreadsheet_id}/values/{range_name}',
                            headers=headers)
    if response.status_code == 200:
        return response.json()['values']
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
