from django.db import models

class Topic(models.Model):

    class Meta:
        db_table = "topic"

    title   = models.CharField(verbose_name="タイトル", max_length=100, default="")
    comment = models.CharField(verbose_name="コメント", max_length=2000)
    price   = models.IntegerField(verbose_name="金額", null=True)

    def __str__(self):
        return self.comment
