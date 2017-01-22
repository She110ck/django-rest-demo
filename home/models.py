from django.db import models


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True,blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Book(models.Model):
    title = models.CharField(max_length=100)
    page_size = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
