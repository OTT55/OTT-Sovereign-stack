scores = [88, 92, 45, 76, 95, 61, 83, 70]

total = 0
for score in scores:
    total += score

average = total / len(scores)
highest = max(scores)
lowest = min(scores)

print(f"Average: {average}")
print(f"Highest: {highest}")
print(f"Lowest: {lowest}")

for score in scores:
    if score >= 90:
        print(f"{score} - Excellent")
    elif score >= 70:
        print(f"{score} - Good")
    else:
        print(f"{score} - Needs Work")