from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Meal(models.Model):
    user = models.ForeignKey('auth.User', related_name='meals', on_delete=models.CASCADE)
    datetime = models.DateTimeField(auto_now_add=True)
    calories = models.IntegerField()
    description = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('datetime',)