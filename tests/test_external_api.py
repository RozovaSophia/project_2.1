import unittest
from unittest.mock import Mock, patch

from src.external_api import return_amount


class TestExternalAPI(unittest.TestCase):
    @patch("requests.get")
    @patch("src.utils.get_fin_transactions")
    def test_external_api(self, mock_get_fin_transactions, mock_get):
        """Тестирует функцию external_api с помощью Mock и patch"""
        mock_data = [
            {"operationAmount": {"currency": {"code": "USD"}, "amount": "100"}},
            {"operationAmount": {"currency": {"code": "RUB"}, "amount": "200"}},
        ]
        mock_get_fin_transactions.return_value = mock_data

        def side_effect(url, headers):
            mock_response = Mock()
            if "from=USD" in url:  # Если запрос на конвертацию из USD
                mock_response.status_code = 200
                mock_response.json.return_value = {"result": 7500.0}  # Примерный курс
                return mock_response
            elif "from=RUB" in url:
                mock_response.status_code = 200
                mock_response.json.return_value = {"result": 1.0}  # 1 RUB = 1 RUB (ожидаемо)
                return mock_response
            else:
                mock_response.status_code = 400  # Неизвестный запрос
                mock_response.text = "Unknown currency"
                return mock_response

        mock_get.side_effect = side_effect

        transactions = mock_get_fin_transactions()
        # Вызываем return_amount для каждой транзакции и проверяем результат
        usd_transaction = transactions[0]
        rub_transaction = transactions[1]

        usd_result = return_amount(usd_transaction)
        rub_result = return_amount(rub_transaction)

        self.assertAlmostEqual(usd_result, 7500.0, places=2)  # Проверяем конвертацию USD
        self.assertAlmostEqual(rub_result, "200", places=2)
