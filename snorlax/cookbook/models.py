from django.db import models


class Ingredient(models.Model):
    """Single ingredient."""

    name = models.CharField(max_length=512)


class IngredientAmount(models.Model):
    """An ingredient associated with an amount."""

    dishes = models.ForeignKey(
        "Recipe", related_name="ingredient_amounts", on_delete=models.CASCADE
    )
    ingredient = models.ForeignKey(
        "Ingredient",
        related_name="ingredient_amounts",
        on_delete=models.CASCADE,
        blank=True,
    )
    amount = models.SmallIntegerField()
    unit = models.CharField(max_length=32)
    note = models.CharField(max_length=256)


class Recipe(models.Model):
    """A dish or cocktail."""

    name = models.CharField(max_length=64)
    ingredients = models.ManyToManyField(
        "Ingredient", through="IngredientAmount", related_name="dishes"
    )


class Step(models.Model):
    """A single step in a dish or cocktail recipe."""

    text = models.CharField(max_length=512)
    preparation_time = models.DurationField()
    cooking_time = models.DurationField()
    dish = models.ForeignKey("Recipe", related_name="steps", on_delete=models.CASCADE)
