from django.db import models

class Book(models.Model):
    CATEGORY_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Education', 'Education'),
        ('Science', 'Science'),
        ('Biography', 'Biography'),
    ]

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True, default="0000000000000")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    availability_status = models.BooleanField(default=True)

    def __str__(self):
        return self.title







