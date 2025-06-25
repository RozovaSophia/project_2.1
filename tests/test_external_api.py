import unittest
from unittest.mock import patch, Mock
from src.external_api import return_amount
from src.utils import get_fin_transactions

class TestExternalAPI(unittest.TestCase):
    @patch('requests.get')
    @patch('src.utils.get_fin_transactions')
    def test_external_api(self, mock_get_fin_transactions, mock_get):
        # Настройка поведения Mock
        mock_response = Mock()
        mock_response.json.return_value = {'amount': 31957.58}
        mock_get.return_value = mock_response
        mock_data = [
            {
                'operationAmount': {
                    'currency': {'code': 'USD'},
                    'amount': '100'
                }
            },
             {
                'operationAmount': {
                    'currency': {'code': 'RUB'},
                    'amount': '200'
                }
            }
        ]
        mock_get_fin_transactions.return_value = mock_data


        result = return_amount(data=mock_get_fin_transactions())
        self.assertAlmostEqual(result, 200, places=2)
