import json
import random
from datetime import datetime

def load_words(file_path):
    with open(file_path, 'r') as file:
        words = json.load(file)
    return words

def generate_cryptonym(adjectives, nouns):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f'{adjective} {noun}'

# Load adjectives and nouns from JSON files
adjectives = load_words('data/adjectives.json')
nouns = load_words('data/nouns.json')

# Generate 10 cryptonyms
cryptonyms = []
for _ in range(100):
    cryptonyms.append(generate_cryptonym(adjectives, nouns))

# Save cryptonyms to a file with timestamp in the filename
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"cryptonyms_{timestamp}.txt"
with open(filename, 'w') as file:
    for cryptonym in cryptonyms:
        file.write(cryptonym + '\n')

print(f"Cryptonyms saved to {filename} in the same directory as this program.")
