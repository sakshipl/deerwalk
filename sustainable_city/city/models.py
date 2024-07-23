from django.db import models


class City(models.Model):
    name = models.CharField(max_length=100)
    population = models.IntegerField()
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "cities"


class Tag(models.Model):
    name = models.CharField(max_length=100)


class Building(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name
