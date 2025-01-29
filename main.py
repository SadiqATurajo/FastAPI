from fastapi import FastAPI
import json

app = FastAPI()

# Load JSON dataset
with open("large_cooking_dataset_5000.json", "r", encoding="utf-8") as file:
    recipes = json.load(file)

@app.get("/")
def home():
    return {"message": "Welcome to the Cooking Dataset API!"}

@app.get("/recipes")
def get_all_recipes():
    return recipes

@app.get("/recipe/{recipe_id}")
def get_recipe(recipe_id: int):
    if 0 <= recipe_id < len(recipes):
        return recipes[recipe_id]
    return {"error": "Recipe not found"}

@app.get("/search")
def search_recipe(title: str = None, cuisine: str = None):
    filtered_recipes = recipes
    if title:
        filtered_recipes = [r for r in filtered_recipes if title.lower() in r["Title"].lower()]
    if cuisine:
        filtered_recipes = [r for r in filtered_recipes if cuisine.lower() in r["Cuisine"].lower()]
    
    return filtered_recipes
