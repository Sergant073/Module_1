mutable_tuple = [1, 2, 3, 4, 5],
immutable_var = (1, 'two', 3.0, [1, 2, 3, 4], True)
print(mutable_tuple)
print(immutable_var)
mutable_tuple[0][1] = 999
print('Измененный кортеж:', mutable_tuple)

# кортежи не изменяются по новым заданным значениям


mutable_list = ["green", "red", "blue", "black"], ["bad", "sad", ]
mutable_list[0][0] = "yellow"
mutable_list[1][0] = "smile"
print(mutable_list)
