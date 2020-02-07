# List Overlap


list_a = ['dog', 'cat', 'rabbit', 'hamster', 'gerbil']
list_b = ['dog', 'hamster', 'snake']


def overlap(list_a, list_b):
    list_c=[value for value in list_a if value in list_b]
    return list_c


print(overlap(list_a, list_b))


for x in list_a:
    if x not in list_b:
        print(x)

for y in list_b:
    if y not in list_a:
        print (y)
