Write-Host "🧹 Начинаем очистку проекта..." -ForegroundColor Green

# Удаляем кэш
Write-Host "🗑️ Удаляем кэш..." -ForegroundColor Yellow
Remove-Item -Recurse -Force .pytest_cache -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force __pycache__ -ErrorAction SilentlyContinue
Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force -ErrorAction SilentlyContinue

# Удаляем старые отчеты
Write-Host "🗑️ Удаляем старые отчеты..." -ForegroundColor Yellow
Remove-Item -Force report.html -ErrorAction SilentlyContinue
Remove-Item -Force report.json -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force allure-results -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force allure-report -ErrorAction SilentlyContinue

# Удаляем старые скрипты (оставляем только run.ps1)
Write-Host "🗑️ Удаляем старые скрипты..." -ForegroundColor Yellow
Remove-Item -Force run_tests_all.ps1 -ErrorAction SilentlyContinue
Remove-Item -Force run_with_allure.ps1 -ErrorAction SilentlyContinue
Remove-Item -Force run_simple.ps1 -ErrorAction SilentlyContinue
Remove-Item -Force generate_allure_report.ps1 -ErrorAction SilentlyContinue
Remove-Item -Force fix_encoding.ps1 -ErrorAction SilentlyContinue

# Удаляем screenshots (если хотите)
# Write-Host "🗑️ Удаляем скриншоты..." -ForegroundColor Yellow
# Remove-Item -Recurse -Force screenshots -ErrorAction SilentlyContinue

Write-Host ""
Write-Host "✅ Проект очищен!" -ForegroundColor Green
Write-Host ""
Write-Host "📁 Остались только важные файлы:" -ForegroundColor Cyan
Write-Host "  - pages/         (Page Objects)" -ForegroundColor Cyan
Write-Host "  - tests/         (Тесты)" -ForegroundColor Cyan
Write-Host "  - conftest.py    (Настройки)" -ForegroundColor Cyan
Write-Host "  - pyproject.toml (Зависимости)" -ForegroundColor Cyan
Write-Host "  - run.ps1        (Запуск)" -ForegroundColor Cyan
Write-Host "  - .env           (Переменные)" -ForegroundColor Cyan