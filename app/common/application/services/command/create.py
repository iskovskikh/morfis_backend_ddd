from dataclasses import dataclass

from common.application.services.command.command import Command
from common.infarastructure.repositories.repository import Repository


class CommandCreate(Command):
    repository: Repository
    validated_data: dict
