from django.db import models

# Create your models here.
class Reporter(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.first_name,self.last_name


class Article(models.Model):
    headline = models.CharField(max_length=100)
    pub_date = models.DateTimeField()
    reporter = models.ForeignKey(Reporter,on_delete=models.CASCADE)

    def __str__(self):
        return self.headline




