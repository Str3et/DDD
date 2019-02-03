import os
import json

# path = os.path.join("static", "Category.json")
# # f = open(path, "r", encoding="UTF-8")
# #
# # print(str(f))

with open('static/Category.json', 'r', encoding="UTF-8") as f:
    data = json.load(f)
for el in data:
    print(data)
