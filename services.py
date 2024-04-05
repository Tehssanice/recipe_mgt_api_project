from typing import List, Optional
from fastapi import HTTPException
from models import Recipe


class RecipeService:
    recipes = []

    @classmethod
    def create_recipe(cls, recipe: Recipe):
        cls.recipes.append(recipe)
        return recipe

    # @classmethod
    # def get_all_recipes(cls) -> List[Recipe]:
    #     return cls.recipes

    @classmethod
    def get_recipe(cls, title: str) -> Optional[Recipe]:
        for recipe in cls.recipes:
            if recipe.title == title:
                return recipe
        return None

    @classmethod
    def delete_recipe(cls, title: str):
        for idx, recipe in enumerate(cls.recipes):
            if recipe.title == title:
                del cls.recipes[idx]
                return True
        return False

    @classmethod
    def update_recipe(cls, title: str, updated_recipe: Recipe):
        for idx, recipe in enumerate(cls.recipes):
            if recipe.title == title:
                cls.recipes[idx] = updated_recipe
                return True
        return False
