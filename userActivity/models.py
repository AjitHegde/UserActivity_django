from django.db import models


class User(models.Model, models.Field):
    id = models.CharField(max_length=9, primary_key=True)
    real_name = models.CharField(max_length=30)
    tz = models.CharField(max_length=50)


class ActivityPeriod(models.Model, models.Field):
    start_time = models.CharField(max_length=25)
    end_time = models.CharField(max_length=25)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
