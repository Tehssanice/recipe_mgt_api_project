from typing import List
from pydantic import BaseModel


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
    description: str
    instructions: List[str]
    ingredients: List[Ingredient]
    nutritional_info: NutritionalInfo
