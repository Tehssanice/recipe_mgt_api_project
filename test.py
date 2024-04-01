import requests

base_url = "http://localhost:8000/api"


recipe_data = {
    "title": "Healthy Pasta Salad",
    "description": "A delicious and nutritious pasta salad recipe",
    "instructions": [
        "Cook pasta according to package instructions.",
        "Combine cooked pasta with chopped vegetables and herbs.",
        "Dress with a light vinaigrette.",
    ],
    "ingredients": [
        {"name": "Pasta", "quantity": 200},
        {"name": "Tomatoes", "quantity": 1},
        {"name": "Cucumber", "quantity": 0.5},
    ],
    "nutritional_info": {
        "calories": 350,
        "fat": {"name": "Fat", "value": 10},
        "protein": {"name": "Protein", "value": 15},
        "carbs": {"name": "Carbs", "value": 40},
    },
}

# Example data for searching recipes
search_criteria = {
    "title": "Pasta",  # Test searching by title
    # Test filtering by ingredients (non-existent ingredient)
    "ingredients": ["Tomatoes", "Carrots"],
    "low_calories": 400,  # Test filtering by low-calorie threshold
}


def test_create_recipe():
    url = f"{base_url}/recipes"
    response = requests.post(url, json=recipe_data)
    assert response.status_code == 200
    assert response.json()["title"] == recipe_data["title"]  # Basic data check


def test_search_recipes():
    url = f"{base_url}/recipes"
    for criteria, expected_count in [
        (search_criteria, 1),  # Expect 1 recipe due to "Pasta" in title
        # Expect 0 recipes for a lower calorie threshold
        ({"low_calories": 300}, 0),
    ]:
        response = requests.get(url, params=criteria)
        assert response.status_code == 200
        recipes = response.json()
        assert len(recipes) == expected_count


if __name__ == "__main__":
    test_create_recipe()
    test_search_recipes()
    print("Tests completed successfully!")
