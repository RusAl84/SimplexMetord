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
    print_hi('PyCharm')
    # print(sqrt2(5))
    # print(sqrt2(7))
    # print(sqrt2(10))
    # print(sqrt2(30))
    # np.
    x = 2
    y = 6
    rows = []
    columns = []
    num = 0
    for i in range(2):
        for j in range(6):
            num += 1
            columns.append(num)
        rows.append(columns)
        columns = []
    # for i in range(0,2):
    #     for j in range(0,6):
    #         num+=1
    #         print(num)
    #         rows[i][j]=num
    print(F" {rows} \n \n \n ")

    tabl = np.zeros((4, 9), )
    tabl[1,1]="Petya"
    print(tabl)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
