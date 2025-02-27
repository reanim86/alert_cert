import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Определяем область доступа
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]

# Загружаем учетные данные
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# Авторизуемся и создаем клиент
client = gspread.authorize(creds)

spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1lfitdCm1akQuMKKr0-07DCU7aqd867tuDmVAMDhPQWw/edit?usp=sharing')

worksheet = spreadsheet.get_worksheet(0)

values = worksheet.get('G2:G45')
print(values)
print(type(values[0][0]))

# spreadsheet = client.create('certs')
#
# spreadsheet.share('reanim861@gmail.com', perm_type='user', role='writer')

# spreadsheet = client.open('My New Spreadsheet')

# spreadsheet = client.open('certsv7')