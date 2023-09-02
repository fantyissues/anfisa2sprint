from django.db import models


class PublishedModel(models.Model):
    """Абстрактная модель. Добавляет флаг is_published."""
    is_published = models.BooleanField('Опубликовано', default=True)

    class Meta:
        abstract = True


class OutputOrderModel(models.Model):
    """Абстрактная модель. Добавляет поле output_order"""
    output_order = models.PositiveSmallIntegerField(
        'Порядок отображения', default=100
    )

    class Meta:
        abstract = True
