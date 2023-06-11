import argparse
import json
import random
from datetime import datetime
import os

def load_words(file_path):
    with open(file_path, 'r') as file:
        words = json.load(file)
    return words

def generate_cryptonym(adjectives, nouns):
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    return f'{adjective} {noun}'

def generate_command(args):
    # Load adjectives and nouns from JSON files
    adjectives = load_words(args.adjectives)
    nouns = load_words(args.nouns)

    # Generate the specified number of cryptonyms
    cryptonyms = []
    for _ in range(args.count):
        cryptonyms.append(generate_cryptonym(adjectives, nouns))

    # Print the generated cryptonyms
    for cryptonym in cryptonyms:
        print(cryptonym)

def save_command(args):
    # Load adjectives and nouns from JSON files
    adjectives = load_words(args.adjectives)
    nouns = load_words(args.nouns)

    # Generate the specified number of cryptonyms
    cryptonyms = []
    for _ in range(args.count):
        cryptonyms.append(generate_cryptonym(adjectives, nouns))

    # Save cryptonyms to a file with timestamp in the filename
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"cryptonyms_{timestamp}.txt"
    with open(filename, 'w') as file:
        for cryptonym in cryptonyms:
            file.write(cryptonym + '\n')

    print(f"Cryptonyms saved to {filename}.")

def help_command(args):
    args.parser.print_help()

def about_command(args):
    print("Cryptogenesis - Cryptonym Generator")
    print("Version: .10")
    print("Author: frostbite_actual")
    print("Description: This command-line tool generates random cryptonyms based off of a list of adjectives and nouns, and saves them to a text file.")

def howto_command(args):
    print("Usage:")
    print("    cg generate -a <adjectives_file> -n <nouns_file> -c <count>")
    print("    cg save -a <adjectives_file> -n <nouns_file> -c <count>")
    print("    cg listfiles -d <data_folder>")
    print("    cg help")
    print("    cg about")
    print("    cg howto")

def listfiles_command(args):
    # List all files in the specified data folder
    folder_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), args.data_folder)
    files = os.listdir(folder_path)

    print("Files in the data folder:")
    for file in files:
        print(file)

def main():
    parser = argparse.ArgumentParser(description="Cryptonym Generator")
    subparsers = parser.add_subparsers(title="commands", dest="command")

    # Generate command
    generate_parser = subparsers.add_parser("generate", help="Generate cryptonyms")
    generate_parser.add_argument("-a", "--adjectives", required=True, help="Path to the adjectives JSON file")
    generate_parser.add_argument("-n", "--nouns", required=True, help="Path to the nouns JSON file")
    generate_parser.add_argument("-c", "--count", type=int, default=1, help="Number of cryptonyms to generate")
    generate_parser.set_defaults(func=generate_command)
    print("Generating cryptonyms...")

    # Save command
    save_parser = subparsers.add_parser("save", help="Generate and save cryptonyms")
    save_parser.add_argument("-a", "--adjectives", required=True, help="Path to the adjectives JSON file")
    save_parser.add_argument("-n", "--nouns", required=True, help="Path to the nouns JSON file")
    save_parser.add_argument("-c", "--count", type=int, default=1, help="Number of cryptonyms to generate and save")
    save_parser.set_defaults(func=save_command)
    print("Saving cryptonyms...")

    # Help command
    help_parser = subparsers.add_parser("help", help="Show help")
    help_parser.set_defaults(func=help_command, parser=parser)

    # About command
    about_parser = subparsers.add_parser("about", help="Show information about the tool")
    about_parser.set_defaults(func=about_command)

    # Howto command
    howto_parser = subparsers.add_parser("howto", help="Show usage instructions")
    howto_parser.set_defaults(func=howto_command)

    # Listfiles command
    listfiles_parser = subparsers.add_parser("listfiles", help="List all files in the data folder, your  when listing files, just specify the folder name, not the full path.")
    listfiles_parser.add_argument("-d", "--data-folder", required=True, help="Path to the data folder")
    listfiles_parser.set_defaults(func=listfiles_command)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
