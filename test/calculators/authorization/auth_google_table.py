import os
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow

# Путь к файлу с учетными данными OAuth2
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CLIENT_SECRET_FILE = os.path.join(BASE_DIR, 'src', 'client_secret.json')
TOKEN_PATH = os.path.join(os.path.dirname(CLIENT_SECRET_FILE), 'token.json')
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def get_access_token():
    creds = None
    # Проверка наличия файла token.json
    if os.path.exists(TOKEN_PATH):
        creds = Credentials.from_authorized_user_file(TOKEN_PATH, SCOPES)
    # Если токены недействительны или отсутствуют, выполните аутентификацию
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Сохранение токенов в token.json
        with open(TOKEN_PATH, 'w') as token:
            token.write(creds.to_json())
    return creds.token
