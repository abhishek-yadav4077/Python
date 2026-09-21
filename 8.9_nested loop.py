"""
nested loop
    - one loop inside another loop
    - for inside for, while inside for, while inside while, for inside while
"""

for i in range(3): #outer loop -> 3 times
    for j in range(2): #inner loop -> 2 times
        print(f"i={i}, j={j}")
