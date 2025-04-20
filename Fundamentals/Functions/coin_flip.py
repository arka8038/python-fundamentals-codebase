from random import random

def coin_flip():
    """Simulates a coin flip and returns 'heads' or 'tails'."""
    
    r = random()
    print(r)
    if r < 0.5:
        return "heads"
    else:
        return "tails"
    
    
print(coin_flip())   