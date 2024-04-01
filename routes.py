from fastapi import APIRouter, HTTPException
from models import Recipe
from services import RecipeService
from typing import List

router = APIRouter()


@router.post("/recipes/", response_model=Recipe)
def create_recipe(recipe: Recipe):
    return RecipeService.create_recipe(recipe)


@router.get("/recipes/", response_model=List[Recipe])
def get_recipes():
    return RecipeService.get_all_recipes()


@router.get("/recipes/{title}", response_model=Recipe)
def get_recipe(title: str):
    recipe = RecipeService.get_recipe(title)
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe


@router.delete("/recipes/{title}")
def delete_recipe(title: str):
    if not RecipeService.delete_recipe(title):
        raise HTTPException(status_code=404, detail="Recipe not found")
    return {"message": "Recipe deleted"}


@router.put("/recipes/{title}")
def update_recipe(title: str, updated_recipe: Recipe):
    if not RecipeService.update_recipe(title, updated_recipe):
        raise HTTPException(status_code=404, detail="Recipe not found")
    return updated_recipe
