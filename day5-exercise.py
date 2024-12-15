# Print items in the list using for loop
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits: 
    print(fruit)
    print(fruit + " pie")

print(fruits)

# Find max score using for loop
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 125, 133]

max_score = 0

for score in student_scores: 
    if score > max_score: 
        max_score = score

print(f"Max score is: {max_score}")

# Print sum of numbers 
sum = 0
for number in range(1, 101):
    sum += number
print(sum)

