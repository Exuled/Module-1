my_dict = {'Alex': 26071993, 'Petr': 12031958, 'Mihail': 12051987}
print(my_dict)
my_dict['Elena'] = 13051999
print(my_dict)
print(my_dict.get('Elena'))
print(my_dict['Alex'])
my_dict.update({'Lev': 27071994, 'Mark': 25112022})
print(my_dict)

my_set = {1,1,2,4,33,5, 4, 'aaa', True}
print(my_set)
my_set.update({9,9, 'class', (1,2,3)})
print(my_set)
my_set.remove(4)
print(my_set)