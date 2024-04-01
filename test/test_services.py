from models import Recipe
from services import RecipeService


def test_recipe_service():
    # Creating some example recipes
    recipe1 = Recipe(title="Chocolate Cake", description="Delicious chocolate cake recipe", instructions=[
                     "1. Mix ingredients", "2. Bake in oven"], ingredients=[], nutritional_info={})
    recipe2 = Recipe(title="Pasta Carbonara", description="Classic Italian pasta dish", instructions=[
                     "1. Cook pasta", "2. Fry bacon and garlic", "3. Mix with eggs and cheese"], ingredients=[], nutritional_info={})

    # Test create_recipe method
    RecipeService.create_recipe(recipe1)
    assert len(RecipeService.recipes) == 1
    RecipeService.create_recipe(recipe2)
    assert len(RecipeService.recipes) == 2

    # Test get_all_recipes method
    all_recipes = RecipeService.get_all_recipes()
    assert len(all_recipes) == 2
    assert recipe1 in all_recipes
    assert recipe2 in all_recipes

    # Test get_recipe method
    assert RecipeService.get_recipe("Chocolate Cake") == recipe1
    assert RecipeService.get_recipe("Nonexistent Recipe") is None

    # Test delete_recipe method
    assert RecipeService.delete_recipe("Chocolate Cake") is True
    assert len(RecipeService.recipes) == 1
    assert RecipeService.delete_recipe("Nonexistent Recipe") is False
    assert len(RecipeService.recipes) == 1

    # Test update_recipe method
    updated_recipe = Recipe(
        title="Updated Recipe",
        description="Updated description",
        instructions=[],
        ingredients=[],
        nutritional_info={})

    assert RecipeService.update_recipe(
        "Pasta Carbonara", updated_recipe) is True
    assert RecipeService.get_recipe("Updated Recipe") == updated_recipe

    # Test search_recipes method
    assert len(RecipeService.search_recipes("Pasta")) == 1
    assert len(RecipeService.search_recipes("Cake")) == 0
