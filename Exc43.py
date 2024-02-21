# Heads or Tails?

import random

outcomes = ["Heads", "Tails"]
weights = [0.7, 0.3]  # Higher weight for 'Heads'
choices = random.choices(outcomes, weights=weights, k=20)
print(choices)
# Output will be a list of 20 randomly chosen outcomes, with 'Heads' being more likely due to its higher weight
