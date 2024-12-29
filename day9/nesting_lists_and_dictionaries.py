capitals = {
    "France": ["Paris"],
    "Germany": ["Berlin"]
}

# Nested list in dictionary
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Stuttgart"]
}

# Print Lille
print(travel_log["France"][1])

nested_list = ["A", "B", ["C", "D"]]
print(nested_list[2][1])

travel_log = {
    "France": {
        "num_times_visited": 8,
        "cities_visisted": ["Paris", "Lille", "Dijon"]
        },
    "Germany": {
        "num_times_visited": 4,
        "cities_visisted": ["Berlin", "Stuttgart"]
        }
}

# Print Stuttgart
print(travel_log["Germany"]["cities_visisted"][1])