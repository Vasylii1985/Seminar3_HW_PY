#Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

main_list = ["15", "111", "64", "232", '4', "783"]

x=int(input("число: "))

def check_num(number,lists):
     return str(number) in lists or number in lists
print(check_num(x,main_list))