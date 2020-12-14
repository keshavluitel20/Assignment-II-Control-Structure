def sort_tup(tup):
    return sorted(tup, key=lambda x: x[2])
my_tup = ("keshab", "luitel", 22)
my_list = [my_tup]
print(my_list)
an_tuple = [('ram', 'rai', 21), ('rita', 'limbu', 24), ('sanish', 'Tamang', 20), ('riya', 'Nepali', 25)]
my_list = my_list + an_tuple
print(my_list)
print(sort_tup(my_list))