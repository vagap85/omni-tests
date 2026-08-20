import pytest


@pytest.mark.skip(reason="Функция восстановления пароля еще не реализована")
class TestRecovery:
    """Тесты восстановления пароля - пропущены, так как функция не реализована"""

    def test_recovery_page_elements_visibility(self, page):
        pass

    def test_successful_recovery_request(self, page):
        pass