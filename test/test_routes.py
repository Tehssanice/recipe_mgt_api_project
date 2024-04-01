from services import RecipeService
from models import Recipe, Ingredient, NutritionalInfo
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_recipe():
    # Creating some example ingredients
    ingredient1 = Ingredient(name="Flour", quantity=200)
    ingredient2 = Ingredient(name="Sugar", quantity=100)
    ingredient3 = Ingredient(name="Eggs", quantity=2)

    # Creating an example nutritional information
    nutritional_info = NutritionalInfo(
        calories=300, fat={"name": "Fat", "value": 15},
        protein={"name": "Protein", "value": 10},
        carbs={"name": "Carbs", "value": 40})

    # Creating a recipe
    recipe = Recipe(
        title="Chocolate Cake",
        description="Delicious chocolate cake recipe",
        instructions=[
            "1. Mix ingredients", "2. Bake in oven"],
        ingredients=[ingredient1, ingredient2, ingredient3], nutritional_info=nutritional_info)

    # Adding the recipe to the recipe service
    created_recipe = RecipeService.create_recipe(recipe)

    # Check if the recipe was successfully added
    assert created_recipe == recipe


def test_get_recipe_by_title():
    # Get recipe by title
    recipe = RecipeService.get_recipe("Chocolate Cake")

    # Check if the correct recipe is returned
    assert recipe.title == "Chocolate Cake"


def test_delete_recipe():
    # Delete recipe by title
    deleted = RecipeService.delete_recipe("Chocolate Cake")

    # Check if the recipe was successfully deleted
    assert deleted
