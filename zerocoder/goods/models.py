from django.db import models

# Create your models here.

class Product(models.Model):
   category = models.ForeignKey(
      Category, verbose_name="Категория", on_delete=models.CASCADE, default=""
   )
   title = models.CharField(verbose_name="Наименование", max_length=255)
   slug = models.SlugField(unique=True)
   image = models.ImageField(verbose_name="Изображение", upload_to="flowers/")
   description = models.TextField(verbose_name="Описание", null=True)
   price = models.DecimalField(verbose_name="Цена", default=0, max_digits=5, decimal_places=2)
   features = models.ManyToManyField(
      "specs.ProductFeatures", verbose_name="Характеристика товара", blank=True, related_name="features_for_product"
   )
   shipping_price = models.IntegerField(verbose_name="Стоимость доставки", default=0)
   sale_value = models.DecimalField(
      verbose_name="Величина скидки",
      default=0,
      help_text="В процентах. Значок процента не ставить!",
      max_digits=5, decimal_places=2
   )
   available = models.BooleanField(verbose_name="Наличие товара", default=True)
   search_vector = SearchVectorField(null=True, blank=True)

   class Meta:
      verbose_name = "Товары"
      verbose_name_plural = "Товары"
      ordering = ["id"]
      indexes = [
         GinIndex(fields=["search_vector"])
      ]

   def __str__(self):
      return f"{self.title}"
