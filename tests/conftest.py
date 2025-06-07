import pytest

@pytest.fixture
def fixture_for_mask():
    return ["1234567890123456", "12345678901234567890", "!@#$%^&*()", "", [12, 13, 14], (12, ), {}, False]