import csv

labels = ["State_code", "name", "population", "rank"]
states = {"MH": {"name": "Maharashtra", "population": "124862220", "rank": "3rd"},
          "UP": {"name": "Uttar Pradesh", "population": "199812341", "rank": "4th"},
          "RJ": {"name": "Rajasthan", "population": "81032689", "rank": "1st"}
          }
# Writing nested dictionary to csv format
with open("states.csv", "w", newline="") as file:
    csv_var = csv.DictWriter(file, labels)
    csv_var.writeheader()
    for state in states:
        csv_var.writerow({label: states[state].get(label) or state for label in labels})

# Reading csv file and converting to dictionary form
with open("states.csv") as file_open:
    csv_list = [[value.strip() for value in read_data.split(",")] for read_data in file_open.readlines()]

(_, *header), *data = csv_list
csv_dict = {}
for row in data:
    key, *values = row
    csv_dict[key] = {key: value for key, value in zip(header, values)}
    print(csv_dict)
