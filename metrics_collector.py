from prometheus_client import Counter, Gauge, Histogram, start_http_server, REGISTRY
import time
import requests

# Метрики
test_total = Counter('test_total', 'Total number of tests run', ['status', 'browser', 'test_name'])
test_duration = Histogram('test_duration_seconds', 'Test execution duration', ['test_name'])
browser_usage = Gauge('browser_usage', 'Browser usage counter', ['browser'])
test_status = Gauge('test_status', 'Test status (1=pass, 0=fail)', ['test_name'])


class MetricsCollector:
    def __init__(self, port=9090):
        self.port = port
        self.start_server()

    def start_server(self):
        """Запускает сервер метрик"""
        start_http_server(self.port)
        print(f"✅ Metrics server started on port {self.port}")

    def record_test_result(self, test_name: str, status: str, browser: str, duration: float):
        """Записывает результат теста"""
        test_total.labels(status=status, browser=browser, test_name=test_name).inc()
        test_duration.labels(test_name=test_name).observe(duration)
        browser_usage.labels(browser=browser).inc()
        test_status.labels(test_name=test_name).set(1 if status == "passed" else 0)

    def get_metrics(self):
        """Возвращает метрики в формате Prometheus"""
        return REGISTRY


# Создаем экземпляр
metrics = MetricsCollector(port=9090)