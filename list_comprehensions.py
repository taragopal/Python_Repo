#list comprehensions
print("--------------LIST----------------")
mylist = [items for items in 'Welcome']
print(mylist)
print("-------------------------------")
number1 = [num for num in range(0, 20)]
print(number1)
print("-------------------------------")
number2 = [n * 2 for n in range(0, 20)]
print(number2)
print("-------------------------------")
number3 = [car**2 for car in range(0, 20)]

print(number3)
print("-------------------------------")
number4 = [i**2 for i in number3 if i % 2 == 0]
print(f'This the list of even squred elements from the list:{number4}')

#set comprehensions
print("----------------SET---------------------")
simple_dict = {
  'initial_growth %': 3,
  'projected_growth %': 5}
simple_dict = {key:value*2 for key,value in simple_dict.items()}
print(simple_dict)
print("-------------------------------")
#dictionary comprehensions
print("------------DICTIONARY------------------")

new_dict = {num:num*2 for num in [1,2,3,4,5,6,7,8,9]}
print(new_dict)



OUTPUT
🔜🔜🔜🔜🔜🔜🔜🔜🔜🔜

--------------LIST----------------
['W', 'e', 'l', 'c', 'o', 'm', 'e']
-------------------------------
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
-------------------------------
[0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38]
-------------------------------
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361]
-------------------------------
This the list of even squred elements from the list:[0, 16, 256, 1296, 4096, 10000, 20736, 38416, 65536, 104976]
----------------SET---------------------
{'initial_growth %': 6, 'projected_growth %': 10}
-------------------------------
------------DICTIONARY------------------
{1: 2, 2: 4, 3: 6, 4: 8, 5: 10, 6: 12, 7: 14, 8: 16, 9: 18}
-------------------------------

print("-------------------------------")
