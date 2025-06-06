# A list of dictionaries representing students
students = [
    {'name': 'Alice', 'grade': 88, 'age': 20},
    {'name': 'Bob', 'grade': 92, 'age': 22},
    {'name': 'Charlie', 'grade': 85, 'age': 21},
    {'name': 'David', 'grade': 92, 'age': 20}
]

# Write a python function to sort a list of dictionaries by a specific key
# and then by a secondary key if the first key is tied.
# Manual Implementation
def sort_manually(data, key_to_sort_by):
    """A straightforward manual implementation to sort by one key."""
    return sorted(data, key=lambda item: item[key_to_sort_by])

# Example Usage: Sort by age
sorted_by_age_manual = sort_manually(students, 'age')

print("\nManual Sort Result (by age):")
for student in sorted_by_age_manual:
    print(student)