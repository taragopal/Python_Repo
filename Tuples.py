#Tuple is same as list, but it is immutable
# Tuples could be used for locked rows and cols in a table, primary key and secondary keep type scenarios
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])  #print 2nd item in the tuple
print(my_tuple)  #prints the entire tuple
x = my_tuple[1]
y = my_tuple[2]
x, y, z, *other = (1, 2, 3, 4, 5)
print(other)

#Tuple has count() and index() methods only.
