class Name_List():

    def __init__(self, *args, **kwargs):
        print(id(args))
        a = args[0]
        a.sort()
        print(f" first name = {a[0]} and second name = {a[1]}")


a = ['keshab', 'luitel', 'krishna', 'manish', 'ram', 'krish']
print(id(a))
Name_List(a)
