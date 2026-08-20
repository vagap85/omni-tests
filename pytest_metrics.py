import time
from metrics_collector import metrics


def pytest_runtest_makereport(item, call):
    """Собирает метрики после каждого теста"""
    if call.when == "call":
        duration = call.duration
        test_name = item.name
        status = "passed" if call.excinfo is None else "failed"
        browser = item.config.getoption("--browser", default="chromium")

        metrics.record_test_result(test_name, status, browser, duration)