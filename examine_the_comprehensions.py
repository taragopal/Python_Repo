some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
for values in some_list:
    if some_list.count(values) > 1:
        if values not in duplicates:
            duplicates.append(values)
print(duplicates)

print("---------Get the same answer by shortening it using comprehensions-----------")
duplicates = [items for items in some_list if some_list.count(items) > 1]
print (duplicates) 
print("---------Test Using comprehensions-----------")
