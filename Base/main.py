# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import numpy;


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

for _ in range(3):
    print_hi("收拾收拾收拾")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Enter a code
count = 0


class Animal(object):
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Animal.count = Animal.count + 1


cat = Animal('lucy', 10)
dog = Animal('lily', 2)
dog2 = Animal('lily', 2)
cat2 = Animal('lily', 2)
print(Animal.count)

# 给定一个矩阵 矩阵的每一项都乘以2

a = [1, 9, 8, 0, 17, 8, 5]
b = 2 * a
print(b)
c = [i for i in range(10)]
print(c)


def fi(x):
    if x == 0 or x == 1:
        return 1
    else:
        return fi(x - 1) + fi(x - 2)


print(fi(5))
