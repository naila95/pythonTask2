
original_tuple = (1, 2, 3)
tuple_list = list(original_tuple)
yeni_element = 4
tuple_list.append(yeni_element)
yeni_tuple = tuple(tuple_list)

print(yeni_tuple)