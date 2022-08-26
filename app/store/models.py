from django.db import models


class City(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title


class Street(models.Model):
    title = models.CharField(max_length=150)
    city = models.ForeignKey(
        'City',
        related_name='city_street',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class Store(models.Model):
    title = models.CharField(max_length=150)
    city = models.ForeignKey(
        'City',
        related_name='cities',
        on_delete=models.SET_NULL
    )
    street = models.ForeignKey(
        'Street',
        related_name='streets',
        on_delete=models.CASCADE
    )
    house = models.CharField(max_length=150)
    time_to_open = models.TimeField(null=True, blank=True)
    time_to_close = models.TimeField(null=True, blank=True)

    def __str__(self):
        return self.title
