a = 10  # a is 10

a = a + 2
print(a * 2)

a = 19  # a becomes 19
print(a + 3)

a = a // 2  # a becomes 9

print("Final result of a:", a)  # Prints the final value of a

print(2+3*6/2)

import datetime

a = 3
b = 4
today = datetime.datetime.today()
day_of_week = today.weekday()
month_of_year = today.month
a = a + day_of_week
b += month_of_year

print(a)
print(b)
c = a + b
print(c)
d = "abc" * (c // 3)
print(d)


def palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False

options = {
    "A": "8025833559061079503003059701609553385208",
    "B": "7489617719749244646336564429479177169847",
    "C": "5485839837501070045005400701057389385845",
    "D": "6593036601359343374664733439531066303956"
}

for key in options:
    if not palindrome(options[key]):
        print(key)

def find_pattern_from_file(filename):
    """
    This function reads a file and counts words that:
    - Start with 'b'
    - End with 'Bob'
    - Have unlimited letters in between

    :param filename: Name of the file to read
    :return: Number of matching words
    """
    count = 0  # Counter for matches

    with open(filename, "r") as file:  # Open the file in read mode
        text = file.read()  # Read the entire file content

    words = text.split()  # Split text into words

    for word in words:  # Loop through each word
        if word.startswith("b") and word.endswith("Bob"):  # Check pattern
            count += 1  # Increment count if it matches

    return count  # Return the total number of matches

# Example usage
filename = "input.txt"  # File to read
result = find_pattern_from_file(filename)
print(f"Number of words that match the pattern: {result}")

# Lists are mutable
my_list = [5, 101, 102]
my_list[0] = 100  #
print(my_list)

# Strings are immutable
my_string = "dance"
# my_string[0] = "D"  #  This will cause an error

# To modify a string, we must create a new one
new_string = "D" + my_string[1:]
print(new_string)  # Output: "Hello"

import random

# Generate 10 random numbers
random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(1, 100))

print("Original numbers:", random_numbers)

# Modify the list based on conditions
for i in range(len(random_numbers)):
    if random_numbers[i] > 80:
        random_numbers[i] = -random_numbers[i]  # Replace with negative value
    elif random_numbers[i] < 40:
        # Sum of digits (convert to string, sum digits)
        num = random_numbers[i]
        digit_sum = sum(int(digit) for digit in str(num))
        random_numbers[i] = digit_sum  # Replace with sum of digits

# Print the modified list
print("Modified numbers:", random_numbers)


def days_since_birth(birthday):
    # Get the birth year from the last 4 characters of the string
    birth_year = int(birthday[-4:])

    # Set the current year manually
    current_year = 2025

    # Calculate full years passed (excluding birth and current year) and convert to days
    return (current_year - birth_year - 1) * 365
print(days_since_birth("24-05-2005"))

def is_valid_url(url):
    if url.startswith("http://") or url.startswith("https://"):  # Check if it starts with http or https
        if "." in url[8:] and url[-1] != ".":  # Check if there's a dot after the protocol and not at the end
            return True
    return False

print(is_valid_url("http://google.com"))
print(is_valid_url("https://example.org"))
print(is_valid_url("ftp://myfile.txt"))
print(is_valid_url("http://invalid"))
print(is_valid_url("https://website."))


