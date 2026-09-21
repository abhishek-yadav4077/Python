scores = [2, 45, 102, 4, 9, 12, 45, 90, 1, 0, 1]
# print(len(scores))
"""
#total score
total = 0
for score in scores:
    total += score
    print(score, total)
print(f"Total runs scored is: {total}")

#another way -> sum()
total = sum(scores)
print(f"Total runs scored is: {total}")


#Highest score
highest = scores[0] #assume that the first value is highest
for score in scores:
    if highest < score:
        highest = score
print(highest)

#another way -> max()
highest = max(scores)
print(highest)


#Lowest score
lowest = scores[0] #assume that the first value is lowest
for score in scores:
    if lowest > score:
        lowest = score
print(lowest)
"""
#another way -> min()
lowest = min(scores)
print(lowest)

