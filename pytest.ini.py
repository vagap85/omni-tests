[pytest]
markers =
    smoke: Быстрые тесты для проверки основных функций
    regression: Полный регрессионный набор
    recovery: Тесты восстановления пароля
    register: Тесты регистрации
    login: Тесты авторизации

testpaths = tests
python_files = test_*.py
python_classes = Test*
python_functions = test_*

addopts =
    -v
    --tb=short
    --strict-markers
    --disable-warnings