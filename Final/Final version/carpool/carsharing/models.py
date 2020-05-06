from django.db import models

class User(models.Model):
    
    name = models.CharField(max_length=128, unique=True, error_messages={
                            'unique': "My unique error", 'required': "My custom error"})
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = 'user'
        verbose_name_plural = 'user'


class DriverList(models.Model):

    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    departure = models.CharField(max_length=256)
    destination = models.CharField(max_length=256)
    time = models.CharField(max_length=30)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['c_time']
        verbose_name = 'user'
        verbose_name_plural = 'user'
