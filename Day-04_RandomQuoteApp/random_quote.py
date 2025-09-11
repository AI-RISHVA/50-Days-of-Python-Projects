import random

def get_random_quote():
    with open("quotes.txt", "r") as file:
        quotes = file.readlines()
    return random.choice(quotes).strip()

def main():
    print(" Your Random Quote ")
    print(get_random_quote())

if __name__ == "__main__":
    main()
