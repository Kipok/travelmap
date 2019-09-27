from django.db import models


class TravelRecord(models.Model):
    """Model holding travel records"""
    place_name = models.CharField(max_length=300, verbose_name="Название места")
    desc = models.TextField(max_length=3000, verbose_name="Описание",
                            blank=True, default="")
    start_date = models.DateField(verbose_name="Дата начала")
    end_date = models.DateField(verbose_name="Дата окончания")
    lon = models.DecimalField(max_digits=9, decimal_places=6,
                              verbose_name="Долгота")
    lat = models.DecimalField(max_digits=9, decimal_places=6,
                              verbose_name="Широта")

    class Meta:
        verbose_name = 'Запись о путешествии'
        verbose_name_plural = 'Записи о путешествиях'

    def __str__(self):
        return self.place_name


class TravelImage(models.Model):
    """Model holding travel images"""
    photo = models.ImageField(verbose_name="Фото", upload_to='uploads')
    text = models.CharField(max_length=500, verbose_name="Описание фото",
                            blank=True)
    travel = models.ForeignKey(TravelRecord, on_delete=models.CASCADE,
                               verbose_name="Путешествие",
                               related_name="travel_images")
