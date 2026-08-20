import pytest


@pytest.mark.debug
def test_inspect_register_real(page):
    """Ищем реальную страницу регистрации"""
    print("\n🔍 Ищем страницу регистрации...")

    # Переходим на страницу логина
    page.goto("https://omni.skroy.ru/login")
    page.wait_for_timeout(2000)

    # Нажимаем на ссылку "Зарегистрируйтесь"
    register_link = page.locator('a:has-text("Зарегистрируйтесь")')
    if register_link.count() > 0:
        print("✅ Нашли ссылку 'Зарегистрируйтесь'")
        register_link.click()
        page.wait_for_timeout(3000)

        # Сохраняем текущий URL
        current_url = page.url
        print(f"\n📍 URL после клика: {current_url}")

        # Ищем все поля ввода
        inputs = page.locator("input").all()
        print(f"\n📝 Найдено полей ввода: {len(inputs)}")

        for i, inp in enumerate(inputs):
            try:
                placeholder = inp.get_attribute("placeholder") or "Нет placeholder"
                input_type = inp.get_attribute("type") or "Нет type"
                input_id = inp.get_attribute("id") or "Нет id"
                input_name = inp.get_attribute("name") or "Нет name"
                print(f"  {i}: type='{input_type}', placeholder='{placeholder}', id='{input_id}', name='{input_name}'")
            except:
                print(f"  {i}: не удалось получить данные")

        # Ищем кнопки
        buttons = page.locator("button").all()
        print(f"\n🔘 Найдено кнопок: {len(buttons)}")
        for i, btn in enumerate(buttons):
            try:
                text = btn.text_content() or "Нет текста"
                print(f"  {i}: '{text}'")
            except:
                print(f"  {i}: не удалось получить текст")

        # Проверяем, есть ли форма регистрации
        if len(inputs) >= 3:
            print("\n✅ Похоже, это страница регистрации!")
        else:
            print("\n⚠️ На странице мало полей ввода. Возможно, это не страница регистрации.")

        # Делаем скриншот
        page.screenshot(path="register_page_real.png")
        print("\n📸 Скриншот сохранен: register_page_real.png")
    else:
        print("❌ Ссылка 'Зарегистрируйтесь' не найдена")