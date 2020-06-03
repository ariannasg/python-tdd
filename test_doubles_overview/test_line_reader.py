from unittest.mock import MagicMock

import pytest
from pytest import raises

from test_doubles_overview.line_reader import read_from_file


# https://docs.pytest.org/en/latest/monkeypatch.html
# Sometimes tests need to invoke functionality which depends on global
# settings or which invokes code which cannot be easily tested such as network
# access. The monkeypatch fixture helps you to safely set/delete an attribute,
# dictionary item or environment variable, or to modify sys.path for importing.
@pytest.fixture()
def mock_open(monkeypatch):
    mock_file = MagicMock()
    mock_file.readline = MagicMock(return_value="test line")
    mock_open = MagicMock(return_value=mock_file)
    monkeypatch.setattr("builtins.open", mock_open)
    return mock_open

def test_returns_correct_string(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=True)
    monkeypatch.setattr("os.path.exists", mock_exists)
    result = read_from_file("blah")
    mock_open.assert_called_once_with("blah", "r")
    assert result == "test line"


def test_throws_exception_with_bad_file(mock_open, monkeypatch):
    mock_exists = MagicMock(return_value=False)
    monkeypatch.setattr("os.path.exists", mock_exists)
    with raises(Exception):
        result = read_from_file("blah")
