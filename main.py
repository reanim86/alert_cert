import gspread
from oauth2client.service_account import ServiceAccountCredentials
from datetime import datetime, date, timedelta
# from dateutil.relativedelta import relativedelta

def work_google():
    # Определяем область доступа
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    # Загружаем учетные данные
    creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
    # Авторизуемся и создаем клиент
    client = gspread.authorize(creds)
    spreadsheet = client.open_by_url(
        'https://docs.google.com/spreadsheets/d/1lfitdCm1akQuMKKr0-07DCU7aqd867tuDmVAMDhPQWw/edit?usp=sharing'
    )
    worksheet = spreadsheet.get_worksheet(0)
    values = worksheet.get('G2:G100')
    n = 2
    result = []
    for date_cert in values:
        if date_cert:
            date_time_str = date_cert[0]
            date_time_object = datetime.strptime(date_time_str, '%d.%m.%Y').date()
            date_today = date.today()
            date_delta = date_time_object - date_today
            month = timedelta(days=31)
            if date_delta <= month:
                val = worksheet.get(f'A{n}:I{n}')
                result.append(val)
        n += 1
    return result

if __name__ == '__main__':
    print(work_google())