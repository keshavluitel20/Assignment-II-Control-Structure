import json
help(json)
my_dictionary = {
    'name': 'Keshab',
    'age': 21
}
dict_json = json.dumps(my_dictionary)
print(dict_json)
final_dict = json.loads(dict_json)
print(final_dict)