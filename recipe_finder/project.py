import tkinter as tk
from tkinter import messagebox

# Mock data for recipes (replace with actual data or API calls)
recipes = [
    { 'name': 'Pasta with Tomato Sauce', 'ingredients': ['pasta', 'tomato', 'garlic'], 'rating': 4 },
    { 'name': 'Chicken Stir Fry', 'ingredients': ['chicken', 'vegetables', 'soy sauce'], 'rating': 3 },
    { 'name': 'Vegetable Soup', 'ingredients': ['carrots', 'potatoes', 'celery', 'onion'], 'rating': 5 },
    { 'name': 'Beef Tacos', 'ingredients': ['beef', 'tortillas', 'cheese', 'lettuce', 'tomato'], 'rating': 4 },
    { 'name': 'Mushroom Risotto', 'ingredients': ['arborio rice', 'mushrooms', 'onion', 'parmesan cheese'], 'rating': 4 },
    { 'name': 'Grilled Salmon', 'ingredients': ['salmon', 'lemon', 'olive oil', 'salt', 'pepper'], 'rating': 5 },
    { 'name': 'Caprese Salad', 'ingredients': ['tomato', 'mozzarella', 'basil', 'balsamic vinegar', 'olive oil'], 'rating': 5 },
    { 'name': 'Chocolate Chip Cookies', 'ingredients': ['flour', 'butter', 'sugar', 'chocolate chips', 'vanilla extract'], 'rating': 5 },
    { 'name': 'Caesar Salad', 'ingredients': ['romaine lettuce', 'croutons', 'parmesan cheese', 'caesar dressing'], 'rating': 4 },
    { 'name': 'Spaghetti Bolognese', 'ingredients': ['spaghetti', 'ground beef', 'tomato sauce', 'onion', 'garlic'], 'rating': 4 }
]

def search_recipes():
    search_term = entry.get().lower()
    matched_recipes = []
    
    for recipe in recipes:
        if any(search_term in ingredient.lower() for ingredient in recipe['ingredients']):
            matched_recipes.append(recipe['name'])
    
    if matched_recipes:
        messagebox.showinfo("Matched Recipes", f"Recipes you can make:\n\n{', '.join(matched_recipes)}")
    else:
        messagebox.showinfo("No Recipes Found", "No recipes found matching your search criteria.")

# Create the main Tkinter window
root = tk.Tk()
root.title("Recipe Finder")

# Header
header_frame = tk.Frame(root, bg='#2ecc71', pady=20)
header_frame.pack(fill=tk.X)

title_label = tk.Label(header_frame, text="Recipe Finder", font=('Segoe UI', 24, 'bold'), fg='white', bg='#2ecc71')
title_label.pack()

# Search Form
search_frame = tk.Frame(root, padx=20, pady=10)
search_frame.pack()

search_label = tk.Label(search_frame, text="Enter ingredients:", font=('Segoe UI', 16))
search_label.grid(row=0, column=0)

entry = tk.Entry(search_frame, font=('Segoe UI', 16), width=30)
entry.grid(row=0, column=1, padx=10)

search_button = tk.Button(search_frame, text="Search", font=('Segoe UI', 16), bg='#27ae60', fg='white', command=search_recipes)
search_button.grid(row=0, column=2, padx=10)

# Footer
footer_frame = tk.Frame(root, bg='#222f3e', pady=10)
footer_frame.pack(side=tk.BOTTOM, fill=tk.X)

footer_label = tk.Label(footer_frame, text="© 2024 Recipe Finder", font=('Segoe UI', 12), fg='white', bg='#222f3e')
footer_label.pack()

# Run the main loop
root.mainloop()