from django.contrib import admin

from .models import IngredientAmount, Recipe, Step


class StepInline(admin.TabularInline):
    model = Step
    extra = 0


class IngredientAmountInline(admin.TabularInline):
    model = IngredientAmount
    extra = 0


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientAmountInline, StepInline]


admin.site.register(Recipe, RecipeAdmin)
