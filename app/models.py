# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class User(models.Model):
    """Database model for Users"""
class Dealer(models.Model):
  """Class Model for Dealer"""

class Customer(models.Model):
    """Class Model for Customer"""

class Inventory(models.Model):
    """Class model for Inventory"""