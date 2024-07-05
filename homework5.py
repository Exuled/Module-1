#immutable_var = 1, 'str', True
#immutable_var [0] = 200  В кортеже данные не меняются, если внутри кортежа нет списка
mutable_list = [1, 'str'], True
mutable_list [0][1] = 200
print(mutable_list)