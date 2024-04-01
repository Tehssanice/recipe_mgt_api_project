from typing import List
from pydantic import BaseModel, Field, validator


class Nutrient(BaseModel):
    name: str
    value: float


class NutritionalInfo(BaseModel):
    calories: float
    fat: Nutrient
    protein: Nutrient
    carbs: Nutrient


class Ingredient(BaseModel):
    name: str
    quantity: float


class Recipe(BaseModel):
    title: str
    description: str = Field(..., max_length=255)
    instructions: List[str]
    ingredients: List[Ingredient]
    nutritional_info: NutritionalInfo

    @validator("ingredients")
    def ingredients_must_not_be_empty(cls, value):
        if not value:
            raise ValueError("Recipes must have at least one ingredient")
        return value
