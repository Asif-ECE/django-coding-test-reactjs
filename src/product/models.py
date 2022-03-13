from config.g_model import TimeStampMixin
from django.db import models


# Create your models here.
class Variant(TimeStampMixin):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    #active = models.BooleanField(default=True)


class Product(TimeStampMixin):
    title = models.CharField(max_length=255)
    sku = models.SlugField(max_length=255, unique=True)
    description = models.TextField()


class ProductImage(TimeStampMixin):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    file_path = models.URLField(max_length=255)
    thumbnail = models.SmallIntegerField()


class ProductVariant(TimeStampMixin):
    variant = models.CharField(max_length=255)
    variant_id = models.ForeignKey(Variant, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)


class ProductVariantPrice(TimeStampMixin):
    product_variant_one = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_one')
    product_variant_two = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_two')
    product_variant_three = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                              related_name='product_variant_three')
    price = models.DecimalField(decimal_places=2)
    stock = models.IntegerField(max_length=11)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
