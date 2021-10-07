from unittest import mock

from lib.fancy import do_something_fancy
from lib.shmancy import shmancy


@mock.patch("test_mock_imported_functions.do_something_fancy")
def test_locally_imported_do_something_fancy(mock_do_something_fancy):
    mock_do_something_fancy.return_value = "fancy"

    assert call_fancy() == "fancy"


@mock.patch("test_mock_imported_functions.do_something_fancy")
def test_do_something_fancy_imported_elsewhere(mock_do_something_fancy):
    mock_do_something_fancy.return_value = "fancy"

    assert shmancy() == "huh"


@mock.patch("lib.shmancy.do_something_fancy")
def test_do_something_fancy_imported_elsewhere_properly(mock_do_something_fancy):
    mock_do_something_fancy.return_value = "fancy"

    assert shmancy() == "fancy"


def call_fancy():
    return do_something_fancy()
