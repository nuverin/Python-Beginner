#fungsi Join
name = ["Hilmy", "Aboyyi"]

print(" ".join(name))

#membuat daftar
table = [i * 2 
 for i in range(1, 5)]
print(list(table))

#zip method
table_of_two = [ 2 * i for i in range(1,11)]
for x,y in zip(range(1,11), table_of_two):
    print('2 * {} = {}'.format(x,y))


