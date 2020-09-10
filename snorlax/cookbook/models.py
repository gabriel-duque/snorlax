from django.db import models


class Ingredient(models.Model):
    """Single ingredient."""

    name = models.CharField(max_length=512, unique=True)

    def __str__(self):
        """Return a human-readable representation of this object."""
        return self.name


class IngredientAmount(models.Model):
    """An ingredient associated with an amount."""

    recipes = models.ForeignKey(
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
    note = models.CharField(max_length=256, blank=True)

    def __str__(self):
        """Return a human-readable representation of this object."""
        return f"{self.ingredient}: {self.amount} {self.unit}"


class Recipe(models.Model):
    """A dish or cocktail."""

    name = models.CharField(max_length=64, unique=True)
    ingredients = models.ManyToManyField(
        "Ingredient", through="IngredientAmount", related_name="recipes"
    )
    servings = models.SmallIntegerField()

    def __str__(self):
        """Return a human-readable representation of this object."""
        return self.name


class Step(models.Model):
    """A single step in a dish or cocktail recipe."""

    text = models.CharField(max_length=512)
    preparation_time = models.DurationField(blank=True)
    cooking_time = models.DurationField(blank=True)
    dish = models.ForeignKey("Recipe", related_name="steps", on_delete=models.CASCADE)

    def __str__(self):
        """Return a human-readable representation of this object."""
        return self.text
