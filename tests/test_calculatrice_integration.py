import builtins
from io import StringIO
import sys
import src.calculatrice as calc


def run_session(inputs):
    """Feed a list of inputs to input() and capture printed output."""
    it = iter(inputs)
    _input = lambda _: next(it)
    old_input, old_stdout = builtins.input, sys.stdout
    try:
        builtins.input = _input
        sys.stdout = StringIO()
        calc.main()
        return sys.stdout.getvalue()
    finally:
        builtins.input = old_input
        sys.stdout = old_stdout


def test_add_flow():
    # Choose 1 (add), enter 2 + 3, then quit
    out = run_session(["1", "2", "3", "n"])
    assert "Result" in out
    assert "5.0" in out


def test_subtract_flow():
    out = run_session(["2", "10", "3", "n"])
    assert "7.0" in out


def test_multiply_flow():
    out = run_session(["3", "4", "5", "n"])
    assert "20.0" in out


def test_divide_flow():
    out = run_session(["4", "8", "2", "n"])
    assert "4.0" in out


def test_divide_by_zero_flow():
    out = run_session(["4", "7", "0", "n"])
    assert "division by zero" in out.lower()


def test_invalid_choice_then_quit():
    # invalid choice, then 'y' to continue, then valid add, then quit
    out = run_session([
        "9",        # invalid choice
        "y",        # continue after invalid choice
        "1",        # now choose addition
        "2", "2",   # numbers
        "n"         # quit
    ])
    assert "Invalid choice" in out
    assert "Result: 4.0" in out


