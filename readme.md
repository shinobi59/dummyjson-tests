# DummyJSON API Tests

[![Tests](https://github.com/shinobi59/dummyjson-tests/actions/workflows/tests.yml/badge.svg)](https://github.com/shinobi59/dummyjson-tests/actions/workflows/tests.yml)
[![Allure Report](https://img.shields.io/badge/Allure-Report-brightgreen)](https://shinobi59.github.io/dummyjson-tests/)

Автоматизированные тесты для публичного API [DummyJSON](https://dummyjson.com).

## Стек
- Python 3.12+
- pytest — тест-фреймворк
- requests — HTTP-клиент
- allure-pytest — генерация отчётов
- GitHub Actions — CI/CD

## Что тестируется

- **Авторизация (JWT)** - получение токена, невалидные данные
- **Products (CRUD, поиск, пагинация)**
- **Carts (CRUD, вложенные структуры, математика)**
- **Негативные сценарии** - 404, отсутствие обязательных полей

## Структура проекта
```
dummyjson-tests/
├── api/ # HTTP-клиент
│ ├── client.py
│ ├── auth.py 
│ ├── carts.py 
│ └── products.py 
├── tests/ # тесты
│ ├── test_auth.py
│ ├── test_carts.py
│ └── test_products.py
├── conftest.py # pytest-фикстуры
├── pytest.ini # конфигурация pytest
└── requirements.txt
```

## Allure-отчёт

Локально:

```bash
pytest
allure serve allure-results
```

Либо открыть **живой отчёт**: [shinobi59.github.io/dummyjson-tests](https://shinobi59.github.io/dummyjson-tests/)

## Установка и запуск

```bash
git clone https://github.com/shinobi59/dummyjson-tests.git
cd restful-booker-tests
python -m venv .venv
.venv\Scripts\activate         # Windows
# source .venv/bin/activate    # Linux/Mac
pip install -r requirements.txt
pytest
```  

## CI

Тесты запускаются автоматически на GitHub Actions при каждом push и pull request.
Результаты Allure публикуются на GitHub Pages — [живой отчёт](https://shinobi59.github.io/dummyjson-tests/).


## Автор

Максим — QA Engineer, [GitHub](https://github.com/shinobi59)

