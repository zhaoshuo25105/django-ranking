from django.db import models

# Create your models here.


class Score(models.Model):
    name = models.CharField(max_length=20, verbose_name='玩家号')
    get_score = models.IntegerField(verbose_name='分数')

class Rank(models.Model):
    ranking = models.IntegerField()
    score = models.OneToOneField(Score,on_delete=None,primary_key=True)


