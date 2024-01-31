import csv, json

json_file = "products.json"

with open(json_file) as f:
    json_file = json.load(f) 

csv_file = []

header = ["id", "title", "price", "description", "category", "image", "rating", "rating_count"]

csv_file.append(header)

for field in json_file:

    field_list = list(field.values())

    last_item:dict = field_list.pop()

    last_item_list = list(last_item.values())

    field_list.extend(last_item_list)

    csv_file.append(field_list)

with open('products.csv', 'w') as f_w:
    csv_writer = csv.writer(f_w)
    csv_writer.writerows(csv_file)


