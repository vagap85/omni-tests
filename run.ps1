chcp 65001 > $null
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  ЗАПУСК АВТОТЕСТОВ" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Запуск smoke-тестов..." -ForegroundColor Yellow
uv run pytest -m smoke -v --headed --slowmo=500 --html=report.html --self-contained-html
Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  ТЕСТЫ ЗАВЕРШЕНЫ" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Отчет сохранен в report.html" -ForegroundColor Cyan
try {
    Start-Process "report.html"
} catch {
    Write-Host "Откройте report.html вручную" -ForegroundColor Yellow
}