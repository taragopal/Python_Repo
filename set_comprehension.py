print("--List values that appearing more than once ----")

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
duplicates = []
for values in some_list:
    if some_list.count(values) > 1:
        if values not in duplicates:
            duplicates.append(values)
print(duplicates)

#Test using comprehensions
#convert the above code into a list comprehension
#convert the set to a list
#iterate over the list and count the number of times the item appears in the list
#update the list with the items that appear more than once


print("---------Test Using comprehensions shortcuts -----------")


duplicates = list(set([items for items in some_list if some_list.count(items) > 1]))
print (duplicates) 

