import sys

# capsys is a built-in fixture that will capture stdin/stdout


def test_capture_stdout(capsys):
    do_chatty_function()
    captured = capsys.readouterr()
    assert captured.out == "The quick brown fox\n"
    assert captured.err == "The fox died\n"


def do_chatty_function():
    print("The quick brown fox")
    sys.stderr.write("The fox died\n")
