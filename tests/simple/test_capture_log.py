import logging


def test_capture_logging(caplog):
    caplog.set_level(logging.DEBUG)
    do_chatty_function()
    assert "The quick brown fox" in caplog.text
    assert "The fox died" in caplog.text


def test_capture_logging_with_level(caplog):
    caplog.set_level(logging.INFO)
    do_chatty_function()
    assert "The quick brown fox" in caplog.text
    assert "The fox died" not in caplog.text


def test_capture_logging_with_context(caplog):
    with caplog.at_level(logging.INFO):
        do_chatty_function()
    assert "The quick brown fox" in caplog.text
    assert "The fox died" not in caplog.text


def do_chatty_function():
    logging.info("The quick brown fox")
    logging.debug("The fox died")
