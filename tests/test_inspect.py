import pytest


@pytest.mark.debug
def test_inspect_login(page):
    """Исследование страницы логина"""
    page.goto("https://omni.skroy.ru/login")
    page.wait_for_timeout(3000)

    # Находим все инпуты
    inputs = page.locator("input").all()
    print(f"\nНайдено инпутов: {len(inputs)}")
    for i, inp in enumerate(inputs):
        print(f"  {i}: {inp.get_attribute('type')} - {inp.get_attribute('placeholder')} - {inp.get_attribute('id')}")

    # Находим все кнопки
    buttons = page.locator("button").all()
    print(f"\nНайдено кнопок: {len(buttons)}")
    for i, btn in enumerate(buttons):
        print(f"  {i}: {btn.text_content()} - {btn.get_attribute('type')}")

    # Находим все ссылки
    links = page.locator("a").all()
    print(f"\nНайдено ссылок: {len(links)}")
    for i, link in enumerate(links):
        print(f"  {i}: {link.text_content()} - {link.get_attribute('href')}")

    page.screenshot(path="inspect_page.png")
    print("\n📸 Скриншот сохранен")