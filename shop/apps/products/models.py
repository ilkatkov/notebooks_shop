from django.db import models
import datetime, os
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    category_title = models.CharField("Название категории", max_length = 200)
    category_description = models.TextField("Описание категории")
    
    def __str__(self):
        return self.category_title

    class Meta():
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

class Processor(models.Model):
    processor_title = models.CharField("Название процессора", max_length = 200)
    processor_description = models.TextField("Описание процессора")
    
    def __str__(self):
        return self.processor_title

    class Meta():
        verbose_name = "Процессор"
        verbose_name_plural = "Процессоры"

class Videocard(models.Model):
    videocard_title = models.CharField("Название видеокарты", max_length = 200)
    videocard_description = models.TextField("Описание видеокарты")
    
    def __str__(self):
        return self.videocard_title

    class Meta():
        verbose_name = "Видеокарта"
        verbose_name_plural = "Видеокарты"

class Product(models.Model):
    product_title = models.CharField("Название товара", max_length = 200)
    product_image = models.ImageField("Изображение товара", upload_to='')
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    processor = models.ForeignKey(Processor, on_delete = models.CASCADE)
    product_ram = models.FloatField("Постоянная память")
    product_rom = models.FloatField("Оперативная память")
    product_description = models.TextField("Описание товара")
    product_price = models.FloatField("Цена товара")
    pub_date = models.DateTimeField("Дата публикации товара")

    def __str__(self):
        return self.product_title

    class Meta():
        verbose_name = "Ноутбук"
        verbose_name_plural = "Ноутбуки"

