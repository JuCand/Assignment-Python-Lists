# Task 1: Given the two lists. Find out if Alice submitted their assignment and attended class.

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]
print("Alice" in submitted)
print("Alice" in attended)
print("Alice" in attended and "Alice" in submitted )