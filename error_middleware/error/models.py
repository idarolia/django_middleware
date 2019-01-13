from django.db import models


class Error(models.Model):
    error_status = models.CharField(max_length=10)
    error = models.CharField(max_length=500)

    def __str__(self):
        return self.error_status + ":" + self.error
