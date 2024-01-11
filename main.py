programming_dictionary = {
    "bug": "an error in a program that prevents it from working well.",
    "list": "used to store collections of data.",
    "loop": "the action of doing something over and over again.",
}

# retrieving data from the dictionary
# print(programming_dictionary['loop'])

# adding new items to dictionary

# edit an item in dictionary

# print(programming_dictionary)

# create an empty dictionary
empty_dictionary = {}

# loop through a dictionary
for key in programming_dictionary:
    print(f"{key}: {programming_dictionary[key]}")

#######################################

# nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# nesting a list in a dictionary
travel_log_a = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# nesting a dictionary in another dictionary
travel_log_b = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    },
}

# nesting dictionaries in a list
travel_log_c = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]
print(travel_log_c[0]['cities_visited'][1])
