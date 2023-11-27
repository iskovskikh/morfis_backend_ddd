from typing import Any

from common.application.command.command import Command


class CommandCreate(Command):
    repository: Any
    validated_data: dict
