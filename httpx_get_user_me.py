from os import access

import httpx  # Импортируем библиотеку HTTPX

# Инициализируем JSON-данные, которые будем отправлять в API
login_payload = {
    "email": "user@example.com",
    "password": "password"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученные токены
print("Status Code:", login_response.status_code)
print("Login response:", login_response_data)


# Вырезаем токен для доступа
access_token = login_response_data["token"]["accessToken"]

# Формируем payload для выполнения get запроса
headers = {"Authorization": f"Bearer {access_token}"}

# Выполняем запрос на получение пользователя
access_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)
access_response_data = access_response.json()

# Выводим данные пользователя
print("Status Code:", access_response.status_code)
print("User data:", access_response_data)

