from app.commands import Command

class DivideCommand(Command):
    def execute(self, params):
        if len(params) != 2:
            raise ValueError("Divide command requires exactly two arguments.")
        
        a, b = params
        try:
            result = int(a) / int(b)
            print(result)  # Print the result to show in REPL
            return result
        except ZeroDivisionError:
            print("Error: Cannot divide by zero.")
            return None