# Chinese Zodiac Program

# Ask the user to enter their birth year.
birth_year = int(input("Enter your birth year: "))

# If the year is earlier than 1900, print the required message and stop the program.
if birth_year < 1900:
    print("Invalid Year, It should not be earlier than 1900")
    exit()

# This list is ordered based on the 12-year Chinese Zodiac cycle, starting with 1900 = Rat
zodiac_signs = [
    "Rat",
    "Ox",
    "Tiger",
    "Rabbit",
    "Dragon",
    "Snake",
    "Horse",
    "Goat",
    "Monkey",
    "Rooster",
    "Dog",
    "Pig"
]

# Use % 12 to repeat the cycle every 12 years.
cycle_index = (birth_year - 1900) % 12
zodiac_animal = zodiac_signs[cycle_index]

# Display the final zodiac result.
print(f"Your Chinese Zodiac sign is {zodiac_animal}.")
