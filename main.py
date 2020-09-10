import numpy as np
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def sqrt2(x):

    if x<=6:
        return pow(x, 2)
    elif x<=8:
        return  x**3
    elif x<=20:
        return x


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(sqrt2(5))
    # print(sqrt2(7))
    # print(sqrt2(10))
    # print(sqrt2(30))
    # np.
    # rows = []
    # columns = []
    # num = 0
    # for i in range(2):
    #     for j in range(6):
    #         num += 1
    #         columns.append(num)
    #     rows.append(columns)
    #     columns = []
    # for i in range(0,2):
    #     for j in range(0,6):
    #         num+=1
    #         print(num)
    #         rows[i][j]=num
    # print(F" {rows} \n \n \n ")

    # cf=[5,4,5]
    # for i in range(3):
    #     cf[i]*=-1
    # print(cf)
    # tabl = np.zeros((4, 9))
    # print(tabl)
    mas=[]
    for i in range(4):
        row=[1,2,3]
        mas.append(row)
    mas.insert(1,[1,2,3,4])

    print(F"\n  mas= {mas} \n")
    z=range(5)
    print(z)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
