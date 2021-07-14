from django.db import models


class Product(models.Model):
    name = models.CharField('Название', max_length=255)
    price = models.IntegerField('Цена')
    quantity = models.PositiveIntegerField('Количество товара')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Category(models.Model):
    product = models.ForeignKey('product.Product', models.CASCADE, 'product_category', null=True)
    category = models.CharField('Категория', max_length=255)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.category


