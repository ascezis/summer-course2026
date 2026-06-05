import os 
import requests
from datetime import datetime

FOLDER_NAME = "automaton_reports"
FILE_NAME = "crypto_log.txt"

if not os.path.exists(FOLDER_NAME):
    os.makedirs(FOLDER_NAME)
    print(f"Новая директория создана: {FOLDER_NAME}")


URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

try:
    response = requests.get(URL)
    if response.status_code == 200:
        data = response.json()
        btc_price = data["bitcoin"]["usd"]

        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        log_entry = f"[{current_time}] Курс битка равен: ${btc_price}\n"

        full_path = os.path.join(FOLDER_NAME, FILE_NAME)
        
        with open(full_path, "a", encoding="utf-8") as file:
            file.write(log_entry)

        print(f"Данные успешно сохранены в {full_path}: {log_entry.strip()}")
    else:
        print(f"Ошибка запроса. Статус-код: {response.status_code}")

except Exception as e:
    print(f"Не удалось получить данные {e}")