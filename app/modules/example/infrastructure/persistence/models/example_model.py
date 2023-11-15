from django.db import models

from common.infarastructure.persistance.model import BaseModel
from modules.example.domain.models.example import Status, Example, ExampleId


class ExampleModel(BaseModel):
    title = models.CharField(
        max_length=255,
        validators=[],
        verbose_name='Название'
    )

    status = models.CharField(
        max_length=32,
        choices=Status.choices(),
        verbose_name='Статус'
    )

    is_hidden = models.BooleanField(
        verbose_name='показывать'
    )

    def to_domain(self) -> Example:
        return Example(
            id=ExampleId(self.id),
            title=self.title,
            status=Status(self.status),
            is_hidden=self.is_hidden
        )

    @staticmethod
    def from_domain(example: Example) -> 'ExampleModel':
        return ExampleModel(
            id=example.id,
            title=example.title,
            status=example.status,
            is_hidden=example.is_hidden
        )

    def formatted_title(self):
        return self.title.capitalize()

    def __str__(self):
        return self.title
