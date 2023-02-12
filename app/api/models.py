from django.db import models


class Parlance(models.Model):
    abbr = models.CharField(max_length=20, verbose_name="缩写")
    desc = models.TextField(max_length=500, verbose_name="描述")
    zh = models.CharField(max_length=50, verbose_name="中文")
    en = models.CharField(max_length=50, verbose_name="英文")
