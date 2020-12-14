import csv


def make_csv(list1):
    with open('test.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerow(['name', 'address', 'age'])
        csv_writer.writerows(list1)


print(make_csv([('George' '4312 Abbey Road', 22), ('John', '54 Love Ave', 21)]))
