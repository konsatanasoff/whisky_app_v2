from django.db import models


class DrinkModel(models.Model):
    TYPE_CHOICE_SCOTCH = "Scotch"
    TYPE_CHOICE_BOURBON = "Bourbon"
    TYPE_CHOICE_IRISH = "Irish"

    TYPE_CHOICES = [
        (TYPE_CHOICE_SCOTCH, "Scotch"),
        (TYPE_CHOICE_BOURBON, "Bourbon"),
        (TYPE_CHOICE_IRISH, "Irish"),
    ]

    type = models.CharField(
        max_length=7,
        choices=TYPE_CHOICES,
    )

    name = models.CharField(max_length=50)
    age = models.IntegerField(default=3)
    description = models.TextField(max_length=500)
    image = models.URLField()

    def __str__(self):
        return f'{self.name} ({self.type}), aged for {self.age} years'
