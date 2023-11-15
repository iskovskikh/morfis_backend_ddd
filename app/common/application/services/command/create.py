from common.application.services.command.command import Command
from common.infarastructure.persistance.repository import Repository


class CommandCreate(Command):
    repository: Repository
    validated_data: dict
