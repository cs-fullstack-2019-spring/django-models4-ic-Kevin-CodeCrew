from django.db import models


class Reporter(models.Model):
    reporter_first_name = models.CharField(max_length=100)
    reporter_last_name = models.CharField(max_length=100)
    reporter_email = models.CharField(max_length=100)


# Create your models here.

class Article(models.Model):
    article_name = models.CharField(max_length=100)
    article_pubdate = models.DateField()
    article_reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)
