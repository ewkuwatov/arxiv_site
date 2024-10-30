from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Essay(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    file = models.FileField(upload_to='essays/')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10000)

    def __str__(self):
        return f'{self.title} - {self.category.name} - {self.price} сум.'
