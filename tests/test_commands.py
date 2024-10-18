import pytest
from app import App
from app.plugins.add import AddCommand
from app.plugins.subtract import SubtractCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.divide import DivideCommand

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command."""
    # Simulate user entering 'greet' followed by 'exit'
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

def test_app_menu_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'menu' command."""
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    
    assert str(e.value) == "Exiting...", "The app did not exit as expected"

# Add tests for the calculator commands
def test_app_add_command(monkeypatch, capfd):
    # Simulate input for the REPL: add 5 3 and exit
    inputs = iter(['add 5 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):  # Expect SystemExit when 'exit' is called
        app.start()
    
    # Capture the output
    captured = capfd.readouterr()
    assert "8" in captured.out, "Add command did not return the expected output"

def test_app_subtract_command(monkeypatch, capfd):
    # Simulate input for the REPL: subtract 5 3 and exit
    inputs = iter(['subtract 5 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):  # Expect SystemExit when 'exit' is called
        app.start()

    # Capture the output
    captured = capfd.readouterr()
    assert "2" in captured.out, "Subtract command did not return the expected output"

def test_app_multiply_command(monkeypatch, capfd):
    # Simulate input for the REPL: multiply 5 3 and exit
    inputs = iter(['multiply 5 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):  # Expect SystemExit when 'exit' is called
        app.start()

    # Capture the output
    captured = capfd.readouterr()
    assert "15" in captured.out, "Multiply command did not return the expected output"

def test_app_divide_command(monkeypatch, capfd):
    # Simulate input for the REPL: divide 6 3 and exit
    inputs = iter(['divide 6 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):  # Expect SystemExit when 'exit' is called
        app.start()

    # Capture the output
    captured = capfd.readouterr()
    assert "2.0" in captured.out, "Divide command did not return the expected output"

def test_app_divide_by_zero(monkeypatch, capfd):
    # Simulate input for the REPL: divide 5 0 and exit
    inputs = iter(['divide 5 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit):  # Expect SystemExit when 'exit' is called
        app.start()

    # Capture the output
    captured = capfd.readouterr()
    assert "Cannot divide by zero" in captured.out, "Divide by zero did not raise the correct error message"