import random

lower_case = list('abcdefghijklmnopqrstuvwxyz')
upper_case = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list("!@#$&*?|/")

new_list = [lower_case, upper_case, numbers, symbols]

generated_password_lenght = 6

generated_password = ''
for j in range(100):
    for i in range(generated_password_lenght):
        generated_password += random.choice(new_list[i%4])
        print(generated_password)
    





