from collections import defaultdict, deque
from typing import List

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # Define a method to find all recipes that can be made given the ingredients and supplies.

        graph = defaultdict(list)
        # Create a graph where each ingredient points to the recipes it is used in.

        in_degree = {}
        # Dictionary to store the number of ingredients (dependencies) required for each recipe.

        for i, recipe in enumerate(recipes):
            # Iterate through each recipe and its index.

            in_degree[recipe] = len(ingredients[i])
            # Initialize the in-degree (number of dependencies) for the recipe.

            for ing in ingredients[i]:
                # Iterate through the ingredients required for the current recipe.

                graph[ing].append(recipe)
                # Add the recipe to the list of recipes that depend on the current ingredient.

        queue = deque(supplies)
        # Initialize a queue with the available supplies (ingredients we already have).

        res = []
        
        while queue:
            item = queue.popleft()
            # Remove an item (ingredient or recipe) from the front of the queue.

            for recipe in graph[item]:
                # Iterate through all recipes that depend on the current item.
                in_degree[recipe] -= 1
                # Decrease the in-degree (number of dependencies) for the recipe.

                if in_degree[recipe] == 0:
                    # If the recipe has no more dependencies, it can be made.
                    queue.append(recipe)
                    res.append(recipe)
        return res