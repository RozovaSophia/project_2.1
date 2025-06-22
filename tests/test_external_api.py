from unittest.mock import Mock

def test_external_api():
    mock_amount = Mock(return_value=31957.58)
    requests.get() = mock_amount
    assert return_amount() == 31957.58
    mock_amount.assert_called_once()
