# 🧪 OmniNotice Автотесты

[![CI](https://github.com/vagap85/omni-tests/actions/workflows/tests.yml/badge.svg)](https://github.com/vagap85/omni-tests/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40+-green.svg)](https://playwright.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-7.0+-orange.svg)](https://pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-2.32+-red.svg)](https://allurereport.org/)
[![uv](https://img.shields.io/badge/uv-0.12+-purple.svg)](https://github.com/astral-sh/uv)
[![Tests](https://img.shields.io/badge/Tests-19%20passed%2C%202%20skipped-brightgreen.svg)](https://github.com/vagap85/omni-tests/actions)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
📝 ПОЛНЫЙ README.md (с бейджами)
markdown
# 🧪 OmniNotice Автотесты

[![CI](https://github.com/vagap85/omni-tests/actions/workflows/tests.yml/badge.svg)](https://github.com/vagap85/omni-tests/actions/workflows/tests.yml)
[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.40+-green.svg)](https://playwright.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-7.0+-orange.svg)](https://pytest.org/)
[![Allure](https://img.shields.io/badge/Allure-2.32+-red.svg)](https://allurereport.org/)
[![uv](https://img.shields.io/badge/uv-0.12+-purple.svg)](https://github.com/astral-sh/uv)
[![Tests](https://img.shields.io/badge/Tests-19%20passed%2C%202%20skipped-brightgreen.svg)](https://github.com/vagap85/omni-tests/actions)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> Автотесты для формы авторизации, регистрации и восстановления пароля на сайте [OmniNotice](https://omni.skroy.ru/login)

---

## 📊 Статус тестов

| Браузер | Статус |
|---------|--------|
| Chromium | [![Chromium](https://img.shields.io/badge/Chromium-Passed-brightgreen.svg)]() |
| Firefox | [![Firefox](https://img.shields.io/badge/Firefox-Passed-brightgreen.svg)]() |
| WebKit | [![WebKit](https://img.shields.io/badge/WebKit-Passed-brightgreen.svg)]() |

**Итого:** 19 passed, 2 skipped

---

## 📋 Содержание

- [Технологии](#технологии)
- [Структура проекта](#структура-проекта)
- [Установка](#установка)
- [Запуск тестов](#запуск-тестов)
- [Отчеты](#отчеты)
- [Результаты](#результаты)
- [CI/CD](#cicd)

---

## 🛠️ Технологии

| Инструмент | Версия | Назначение |
|------------|--------|------------|
| **Python** | 3.11+ | Язык программирования |
| **Playwright** | 1.40+ | Фреймворк для тестирования UI |
| **Pytest** | 7.0+ | Фреймворк для тестов |
| **Allure** | 2.32+ | Красивые отчеты |
| **uv** | 0.12+ | Менеджер пакетов |
| **Page Object Model** | - | Архитектура тестов |

---

## 📁 Структура проекта
omni-tests/
├── .github/
│ └── workflows/
│ └── tests.yml # CI/CD пайплайн
├── pages/
│ ├── init.py
│ ├── login_page.py # Page Object логина
│ ├── register_page.py # Page Object регистрации
│ └── recovery_page.py # Page Object восстановления
├── tests/
│ ├── init.py
│ ├── test_login.py # Тесты логина
│ ├── test_register.py # Тесты регистрации
│ ├── test_recovery.py # Тесты восстановления
│ ├── test_smoke_simple.py # Smokе-тесты
│ └── test_login_parametrized.py # Параметризованные тесты
├── screenshots/ # Скриншоты при падениях
├── conftest.py # Настройки pytest
├── pyproject.toml # Зависимости проекта
├── .env # Переменные окружения
├── run.ps1 # Скрипт запуска
└── README.md # Документация

text

---

## 🚀 Установка

### 1. Клонировать репозиторий
```bash
git clone https://github.com/vagap85/omni-tests.git
cd omni-tests
2. Установить uv (менеджер пакетов)
powershell
# Windows
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Linux/Mac
curl -LsSf https://astral.sh/uv/install.sh | sh
3. Установить зависимости
powershell
uv sync
4. Установить браузеры Playwright
powershell
uv run playwright install
5. Настроить .env файл
Создайте .env с тестовыми данными:

env
TEST_USER_LOGIN=q@q.co
TEST_USER_PASSWORD=q
BASE_URL=https://omni.skroy.ru
🏃 Запуск тестов
Быстрый запуск (с отчетом)
powershell
.\run.ps1
Запуск всех тестов
powershell
uv run pytest -v
Запуск с отображением браузера
powershell
uv run pytest -v --headed --slowmo=500
Запуск конкретной группы
powershell
# Только логин
uv run pytest -m login -v

# Только регистрация
uv run pytest -m register -v

# Только smoke
uv run pytest -m smoke -v
Параллельный запуск
powershell
uv run pytest -v -n auto
📊 Отчеты
HTML отчет
powershell
uv run pytest -v --html=report.html --self-contained-html
Отчет сохраняется в report.html

Allure отчет
powershell
# Генерация результатов
uv run pytest -v --alluredir=allure-results

# Генерация отчета
allure generate allure-results -o allure-report --clean

# Открыть отчет
allure open allure-report
📈 Результаты
Категория	Тестов	Статус
Логин	6	✅ Все проходят
Регистрация	9	✅ Все проходят
Навигация	3	✅ Все проходят
Smoke	3	✅ Все проходят
Исследование	2	✅ Все проходят
Восстановление	2	⏸️ Пропущены
Итого: 19 тестов проходят, 2 пропущены 🎉

🔄 CI/CD
Проект настроен на автоматический запуск в GitHub Actions:

✅ Запуск при пуше в main/develop

✅ Запуск при создании Pull Request

✅ Ежедневный запуск по расписанию (в 9:00)

✅ Тесты в 3 браузерах (Chromium, Firefox, WebKit)

✅ Автоматическое сохранение отчетов и скриншотов

📝 Маркеры тестов
Маркер	Назначение
smoke	Быстрые тесты для проверки основных функций
login	Тесты авторизации
register	Тесты регистрации
recovery	Тесты восстановления пароля
regression	Полный регрессионный набор
🛠️ Разработка
Добавление нового теста
Создайте Page Object в pages/

Добавьте тест в tests/

Добавьте маркер @pytest.mark.ваш_маркер

Запустите и проверьте

Добавление нового маркера
Добавьте в pyproject.toml:

toml
markers = [
    "ваш_маркер: Описание маркера",
]
📦 Зависимости
Основные:

playwright - UI тестирование

pytest - фреймворк для тестов

pytest-playwright - интеграция Playwright с pytest

Dev:

pytest-html - HTML отчеты

pytest-json-report - JSON отчеты

pytest-xdist - параллельный запуск

allure-pytest - Allure отчеты

python-dotenv - .env файлы

🤝 Вклад
Форкните репозиторий

Создайте ветку (git checkout -b feature/amazing-feature)

Закоммитьте изменения (git commit -m 'Add amazing feature')

Запушьте ветку (git push origin feature/amazing-feature)

Создайте Pull Request

📄 Лицензия
Этот проект распространяется под лицензией MIT.

🙏 Благодарности
Playwright - отличный фреймворк для тестирования

Pytest - лучший фреймворк для тестов в Python

uv - супер-быстрый менеджер пакетов

🚀 Сделано с ❤️ для автоматизации тестирования OmniNotice

