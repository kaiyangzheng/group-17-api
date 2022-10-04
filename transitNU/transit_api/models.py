from django.db import models

# Create your models here.
class Train(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    line = models.CharField(max_length=255)
    longitude = models.FloatField()
    latitude = models.FloatField()
    bearing = models.FloatField()
    status = models.CharField(max_length=255)
    stop = models.CharField(max_length=255, null=True)

# class TrainLocation(models.Model):
#     id = models.AutoField()
#     train = models.ForeignKey(Train)
#     latitude = models.FloatField()
#     longitude = models.FloatField()
#     bearing = models.FloatField()

# class TrainStatus(models.Model):
#     id  = models.AutoField()
#     status = models.CharField()
#     stop = models.CharField()
