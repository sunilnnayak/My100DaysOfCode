# Day 8 (24/7/2022)

1. Dictionaries
{Key:Value}

programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again."
}

print(programming_dictionary["Bug"])    - to retrive the data from dict

programming_dictionary["Loop"] = "The action of doing something again and again."
print(programming_dictionary)                           --adding new items to dictionary/ Can also b used for updating any Value

programming_dictionary = {}
print(programming_dictionary)                           -- Wipe out an existing dictionary

# to Loop throgh the dict
for key in programming_dictionary:
    print(key)                                          --gives only key 1 by 1
    print(programming_dictionary[key])                  -- we can take value



2. Nesting Lists and Dictionaries

# Nesting 
capitals = {
  "France": "Paris",
  "Germany": "Berlin",
}

# Nesting a List in a Dictionary

travel_log = {
  "France": ["Paris", "Lille", "Dijon"],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting Dictionary in a Dictionary

travel_log = {
  "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting Dictionaries in Lists

travel_log = [
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