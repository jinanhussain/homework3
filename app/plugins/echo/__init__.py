import sys
from app.commands import Command


class EchoCommand(Command):
    def execute(self, params=None):
        print(params)