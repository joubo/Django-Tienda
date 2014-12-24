from django.db import models
from django.contrib.auth.models import User

# Create your models here.

User.add_to_class('direccion', models.CharField(max_length = 40)),
User.add_to_class('telefono', models.CharField(max_length=9)),