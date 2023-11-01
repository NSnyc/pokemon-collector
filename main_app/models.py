from django.db import models
from django.urls import reverse
from datetime import date

MEALS = (
  ('N', 'Nanab Berry'),
  ('R', 'Razz Berry'),
  ('P', 'Pinap Berry'),
)

class Held_Item(models.Model):
  name = models.CharField(max_length=50)
  color = models.CharField(max_length=20)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('held-item-detail', kwargs={'pk': self.id})

class Pokemon(models.Model):
  name = models.CharField(max_length=100)
  breed = models.CharField(max_length=100)
  description = models.TextField(max_length=250)
  age = models.IntegerField()
  held_items = models.ManyToManyField('Held_Item')

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('pokemon-detail', kwargs={'pokemon_id': self.id})

  def fed_for_today(self):
    return self.feeding_set.filter(date=date.today()).count() >= len(MEALS)


class Feeding(models.Model):
  date = models.DateField('Date')
  meal = models.CharField(
    max_length=1,
    choices=MEALS,
    default=MEALS[0][0]
  )

  pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_meal_display()} on {self.date}"

  class Meta:
    ordering = ['-date']