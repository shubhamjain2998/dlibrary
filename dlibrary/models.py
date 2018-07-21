from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.
def validate_img(upload):
    ext = upload.name[-4:]
    if not ext in ['.jpg', ".png"]:
        raise ValidationError(u'File type not supported!')
    if upload.size > 1024 * 500:
        raise ValidationError(u'File too big!')


class Branch(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images//", validators=[validate_img], null=True)
    attachment = models.FileField(upload_to="docs//", null=True, blank=True)

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    mobno = models.IntegerField()
    subject = models.CharField(max_length=100, null=True)
    message = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Suser(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

