name = input('What is your name? :')
password = input('What is your password ? :')
pwd_len = len(password)
#   if(pwd_len < 10):
#     print('Its a short password, please use atleast 10 characters')
#   elif:
# print( 'Password is good to be accepted')
masked_pwd = ('*' * pwd_len)
print(
    f'Hello {name} !, your password {masked_pwd} is {pwd_len} characterd long')
