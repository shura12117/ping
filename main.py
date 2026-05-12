import requests

# Пробуем HTTP (а не HTTPS)
try:
    response = requests.get('dsfdgffdg.atwebpages.com/ping.php', timeout=10)
    print(response.text)
except Exception as e:
    print(f"Ошибка: {e}")
