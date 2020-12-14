import csv
with open('test.csv', 'r') as file:
    reader = csv.DictReader(file)
    ordered_dict_list = list(reader)[0]
    to_dict = dict(ordered_dict_list)
    print(to_dict)