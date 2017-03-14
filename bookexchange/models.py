from django.db import models

class Person(models.Model):
    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

class Book(models.Model):
    def __str__(self):
        return self.title

    seller = models.ForeignKey(Person, on_delete=models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
