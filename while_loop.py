n = int(input("Enter a number to find all the even numbers upto that number:"))
if n < 0:
  n = int(input("Please enter a positive number :"))

#elif n == str():
# n = int(input("Please enter a number :"))
#else:
# print("Thank you for entering a valid number")
a = 1
while a <= n:
  if a % 2 == 0:
    print(a)
  a = a + 1

print("\n")

L = []
while len(L) < 3:
  new_name = input("Please enter a new name: ").strip().capitalize()
  L.append(new_name)

print("Sorry list is full")
print(L)
