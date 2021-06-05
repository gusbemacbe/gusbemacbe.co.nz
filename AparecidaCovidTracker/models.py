from __future__ import unicode_literals
from django.contrib import admin
from django.db import models
from django.utils.html import format_html

class Product(models.Model):
    name = models.CharField(max_length = 100)
    price = models.DecimalField(max_digits = 9, decimal_places = 2)

    @admin.display
    def colored_name(self):
          return format_html(
          '<span style="color: #{};">{} {}</span>',
          self.name,
          self.price
      )
          
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')