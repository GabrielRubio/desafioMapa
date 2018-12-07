from django.db import models

# Create your models here.

class Maps(models.Model):
    name = models.CharField(max_length=150, unique=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Maps'

class Distances(models.Model):
    map_name = models.ForeignKey(Maps, on_delete=None)
    point_A = models.CharField(max_length=150, blank=False)
    point_B = models.CharField(max_length=150, blank=False)
    distance = models.IntegerField()

    def __str__(self):
        return self.map_name

    class Meta:
        db_table = 'Distances'