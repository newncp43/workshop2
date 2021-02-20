import json

# a Python object (dict):
python_dict = {
    "name": "New",
    "age" : 20,
    "city" : "Chonburi"
}

# convert into JSON:
json_string = json.dumps(python_dict)

# the result is a JSON string
print(json_string)