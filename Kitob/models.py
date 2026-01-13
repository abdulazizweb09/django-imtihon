from django.db import models

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=50)
    birz_year=models.IntegerField()

    def __str__(self):
        return self.name

class Book(models.Model):
    title=models.CharField(max_length=250)
    author=models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    price=models.IntegerField()
    stock=models.IntegerField()

    def __str__(self):
        return self.title

class Customer(models.Model):
    name=models.CharField(max_length=250)
    email=models.EmailField()
    
    def __str__(self):
        return self.name

class Order(models.Model):
    customer=models.ForeignKey(
        Customer,
        on_delete=models.CASCADE
    )
    book=models.ForeignKey(
        Book,
        on_delete=models.CASCADE
    )
    quantity=models.IntegerField()

