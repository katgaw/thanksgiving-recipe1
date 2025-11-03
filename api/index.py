from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from openai import OpenAI
import os
from typing import Optional

app = FastAPI(title="Thanksgiving Recipe Generator")

# Templates
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/generate-recipe")
async def generate_recipe(
    request: Request,
    diet_type: str = Form(...),
    api_key: str = Form(...)
):
    try:
        # Initialize OpenAI client with API key
        client = OpenAI(api_key=api_key)
        
        # Create the prompt based on diet type
        diet_prompts = {
            "vegetarian": "vegetarian (no meat, but can include dairy and eggs)",
            "vegan": "vegan (no animal products including dairy, eggs, or honey)",
            "lactose_intolerant": "lactose-free (no dairy or lactose-containing ingredients)",
            "no_restrictions": "traditional (no dietary restrictions)"
        }
        
        diet_description = diet_prompts.get(diet_type, "traditional")
        
        prompt = f"""
        Create a simple and delicious Thanksgiving dinner recipe for someone with {diet_description} dietary preferences.
        
        Please provide:
        1. Recipe name
        2. Brief description (1-2 sentences)
        3. Ingredients list (4-6 main ingredients)
        4. Simple cooking instructions (3-4 steps)
        5. Cooking time
        
        Keep it simple and traditional for Thanksgiving. Format it nicely for easy reading.
        """
        
        # Call OpenAI API
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful cooking assistant that creates simple, delicious Thanksgiving recipes."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        recipe = response.choices[0].message.content
        
        return templates.TemplateResponse("recipe.html", {
            "request": request,
            "recipe": recipe,
            "diet_type": diet_type
        })
        
    except Exception as e:
        return templates.TemplateResponse("error.html", {
            "request": request,
            "error": str(e)
        })

# Vercel ASGI handler
from mangum import Mangum

handler = Mangum(app)
