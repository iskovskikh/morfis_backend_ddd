from django.db import models

from modules.example.domain.models.example import Status, Example, ExampleId


class BaseModel(models.Model):
    # id = models.UUIDField(
    #     primary_key=True,
    #     default=uuid.uuid4,
    #     editable=False,
    #     verbose_name='uuid'
    # )

    id = models.IntegerField(primary_key=True)

    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ExampleModel(BaseModel):
    title = models.CharField(
        max_length=255,
        validators=[],
        verbose_name='Название'
    )

    status = models.IntegerField(
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
            id=int(example.id),
            title=example.title,
            status=example.status
        )

    def formatted_title(self):
        return self.title.Capitalize()

    def __str__(self):
        return self.title
