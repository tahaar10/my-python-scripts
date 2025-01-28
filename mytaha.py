import json

data = [
    {"name": "Alice", "role": "Engineer"},
    {"name": "Bob", "role": "Manager"}
]

print(json.dumps(data, indent=4))
