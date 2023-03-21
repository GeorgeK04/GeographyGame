import random

# define a list of countries and their corresponding capitals
countries = {"France": "Paris", "Germany": "Berlin", "Spain": "Madrid", "Italy": "Rome", "Japan": "Tokyo", "United Kingdom": "London", "Russia": "Moscow", "India": "New Delhi", "Brazil": "Brasilia", "China": "Beijing"}

# shuffle the countries and select five at random
selected_countries = random.sample(list(countries), 5)

# create a dictionary to keep track of the user's score
score = {"correct": 0, "incorrect": 0}

# loop through the selected countries and ask the user for their capital
for country in selected_countries:
    capital = input("What is the capital of {}? ".format(country))
    if capital == countries[country]:
        print("Correct!")
        score["correct"] += 1
    else:
        print("Incorrect. The capital of {} is {}.".format(country, countries[country]))
        score["incorrect"] += 1

# print the user's score
print("You got {} out of {} correct!".format(score["correct"], score["correct"] + score["incorrect"]))
