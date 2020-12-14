tup = [('keshab', 'luitel', 22), ('Shyam', 'rai', 20), ('rina', 'shah', 16), ('krishna', 'tamang', 'None')]

li = []

for a in tup:
    li.append(a[2])

print(li)

sum = 0

count = 0

for i in range(len(li)):

    if type(li[i]) == int:
        sum = sum + li[i]

        count = count + 1

aveg = sum / count

print(aveg)
