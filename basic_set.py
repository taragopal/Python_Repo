#Sets are unordered collections of unique objects.
#They are used to store multiple items in a single variable.

my_set = {1, 2, 3, 4, 5, 2, 1}
your_set = {1, 4, 5, 6, 7, 8, 9, 10}

print(my_set)
print("---------------------")
my_set.add(100)
print(my_set)
print("---------------------")
#can convert a list into a set, by using set(list_name), that would return a set of unique items. Or set to a list.

#Set DS cant be indexed, so you cant use my_set[0] to get the first item.

#Can use my_set(1 in set), and it would return true or false.
print("---------------------")
print(my_set.difference(your_set))
print(my_set.discard(1))
print(my_set)
print("---------------------")
print(my_set.difference_update(your_set))
print(my_set)
print("---------------------")
print(my_set.intersection(your_set))

print("---------------------")
print(my_set.union(your_set))
merge_set = my_set | your_set

print("---------------------")
print(my_set.issubset(your_set))
print(your_set.issuperset(merge_set))
print(merge_set)


RUN 
🏃‍♂️‍➡️🏃‍♂️‍➡️🏃‍♂️‍➡️🏃‍♂️‍➡️🏃‍♂️‍➡️🏃‍♂️‍➡️🏃‍♂️‍➡️🏃‍♂️‍➡️🏃‍♂️‍➡️🏃‍♂️‍➡️🏃‍♂️‍➡️
~/workspace/udemy$ python basic_set.py 
{1, 2, 3, 4, 5}
---------------------
{1, 2, 3, 4, 5, 100}
---------------------
---------------------
{2, 3, 100}
None
{2, 3, 4, 5, 100}
---------------------
None
{2, 3, 100}
---------------------
set()
---------------------
{1, 2, 3, 100, 4, 5, 6, 7, 8, 9, 10}
---------------------
False
False
{1, 2, 3, 100, 4, 5, 6, 7, 8, 9, 10}


