from django.db import models


class SubOrder(models.Model):
    product = models.OneToOneField('product.Product', models.CASCADE, related_name='order_product')
    quantity = models.PositiveIntegerField('Количество товара', default=0)
    cost = models.FloatField('Общая стоимость товара', default=0)

    def cost(self):
        self.cost = self.quantity * self.product.price
        self.cost.save()


class Order(models.Model):
    user = models.OneToOneField('user.User', models.CASCADE, related_name='order_user')
    suborder = models.ForeignKey(SubOrder, models.CASCADE, 'suborder')
    date = models.DateTimeField('Дата заказа', auto_now_add=True)
    total_price = models.FloatField('Общая стоимость заказа', default=0)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        
    def __str__(self):
        return f'Заказ: {self.user}'

    def get_total_price(self):
        a = sum([suborder.cost for item in self.suborder.cost.all()])
        return a