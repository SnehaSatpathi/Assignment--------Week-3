import json

# Create JSON file
data = {
    "name": "Sneha",
    "course": "B.Tech",
    "year": 3,
    "skills": ["Python", "Flask", "Spring Boot"]
}

with open("student.json", "w") as f:
    json.dump(data, f, indent=4)

# Read JSON file
with open("student.json", "r") as f:
    loaded_data = json.load(f)

print("JSON Data:", loaded_data)
