from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Lending(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book_id = models.PositiveIntegerField()  # Assuming book_id is an integer. Adjust type if necessary.
    date_borrowed = models.DateTimeField(default=timezone.now)
    date_due = models.DateTimeField()

    def __str__(self):
        return f"Lending {self.id} - User: {self.user.email}, Book ID: {self.book_id}"
