import requests

# Пробуем HTTP (а не HTTPS)
try:
    response = requests.get('http://t-e-t-o.ct.ws/ping.php', timeout=10)
    print(response.text)
except Exception as e:
    print(f"Ошибка: {e}")
