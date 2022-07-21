# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
list1 = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
X = "qwe"

def find_second(str, lst):
     if lst.count(str) > 1:
         return lst.index(str, lst.index(str) + 1)
     return "-1"
print(find_second(X, list1))