import pytest
from faker import Faker

from src.infrastructure.logger import Logger

fake = Faker(locale="pt-BR")


class TestLogger:
    @pytest.fixture
    def logger(self):
        return Logger(__name__)

    def test_return_a_formatted_message(self, logger):
        message = fake.text()
        formatted_message = logger._get_log_message(message)

        assert formatted_message == message

    def test_return_a_formatted_message_with_full_message(self, logger):
        message = fake.text()
        full_message = fake.text()
        formatted_message = logger._get_log_message(message, full_message)

        assert formatted_message == f"{message} - {full_message}"

    def test_return_a_formatted_message_with_operation(self, logger):
        message = fake.text()
        operation = fake.pystr()
        formatted_message = logger._get_log_message(message, operation=operation)

        assert formatted_message == f"({operation}): {message}"

    def test_return_a_full_formatted_message(self, logger):
        message = fake.text()
        full_message = fake.text()
        operation = fake.pystr()
        formatted_message = logger._get_log_message(
            message, full_message, operation=operation
        )

        assert formatted_message == f"({operation}): {message} - {full_message}"
