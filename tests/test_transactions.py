import unittest
from unittest.mock import mock_open, patch

import pandas as pd

from src.transactions import reads_financial_transactions, reads_financial_transactions_excel


class TestReadsFinancialTransactions(unittest.TestCase):
    @patch("src.transactions.open", new_callable=mock_open, read_data="id,state\n1,EXECUTED")
    def test_reads_financial_transactions(self, mock_file):
        actual_transactions = reads_financial_transactions("dummy_path")
        expected_transactions = [{"id": "1", "state": "EXECUTED"}]
        self.assertEqual(actual_transactions, expected_transactions)
        mock_file.assert_called_with("dummy_path", "r", encoding="UTF-8")


class TestReadsFinancialTransactions(unittest.TestCase):
    @patch("pandas.read_excel")
    def test_reads_financial_transactions_excel(self, mock_read_excel):
        data = {"id": [1], "state": ["EXECUTED"]}
        expected_df = pd.DataFrame(data)
        mock_read_excel.return_value = expected_df
        actual_transactions = reads_financial_transactions_excel("dummy_path")
        expected_transactions = [{"id": 1, "state": "EXECUTED"}]
        self.assertEqual(actual_transactions, expected_transactions)
        mock_read_excel.assert_called_with("dummy_path", parse_dates=["date"])
