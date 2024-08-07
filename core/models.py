from django.db import models

class Contact(models.Model):
    created_on = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name
