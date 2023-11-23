from typing import Any

from common.application.services.commands.command import Command


class CommandCreate(Command):
    repository: Any
    validated_data: dict
