from typing import List
from fastapi import APIRouter, Depends, Body, Query, HTTPException
from sqlalchemy import or_
from sqlalchemy.orm import Session
from services import get_db
from models import Recipe, Ingredient, NutritionalInfo

app = APIRouter()

# Dependency for database session


def get_session():
    db = next(get_db())
    yield db
    db.close()


def create_recipe(recipe: Recipe, session: Session = Depends(get_db)):
    # Use the session object for database operations
    session.add(recipe)
    session.commit()
    return recipe


@app.post("/recipes")
async def create_recipe(recipe: Recipe, session: Session = Depends(get_session)):
    # Save recipe and related ingredients/nutritional info
    session.add(recipe)
    session.commit()
    return recipe


@app.put("/recipes/{recipe_id}")
async def update_recipe(recipe_id: int, updated_data: Recipe = Body(...), session: Session = Depends(get_session)):
    # Retrieve the recipe to update
    recipe = session.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    # Update recipe attributes based on provided data
    for field, value in updated_data.dict().items():
        setattr(recipe, field, value)

    session.commit()
    return recipe


@app.patch("/recipes/{recipe_id}")
async def partially_update_recipe(recipe_id: int, update_data: dict = Body(...), session: Session = Depends(get_session)):
    # Retrieve the recipe to update
    recipe = session.query(Recipe).filter(Recipe.id == recipe_id).first()
    if not recipe:
        raise HTTPException(status_code=404, detail="Recipe not found")

    # Update only specified fields in the recipe
    for field, value in update_data.items():
        setattr(recipe, field, value)

    session.commit()
    return recipe
