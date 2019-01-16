from cleo import Application

from .commands import BuildCommand
from .commands import UploadCommand
from .commands import ValidateCommand


def main():
    application = Application()
    application.add(BuildCommand())
    application.add(UploadCommand())
    application.add(ValidateCommand())
    application.run()