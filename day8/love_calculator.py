def calculate_love_score(name1, name2):
    
    # Lowercase the names
    name1 = name1.lower()
    name2 = name2.lower()
    combined_name = name1 + name2
    
    # Count both "true" and "love" occurences
    true_count = 0
    love_count = 0 
    for letter in combined_name: 
        if letter in "true":
            true_count += 1
        if letter in "love":
            love_count += 1
    love_score = str(true_count) + str(love_count)
    print(f"Love Score = {love_score}")

calculate_love_score("Kanye West", "Kim Kardashian")