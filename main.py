import numpy as np
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    cf =np.zeros((1,3))
    ogr=np.zeros((3,4))
    tabl = np.zeros((4, 9))
    cf=[9,10,16]
    ogr=[[18,15,12,360],
         [6,4,8,192],
         [5,3,3,180]]
    for i in range(3):
        tabl[3][2+i] = (-1) * cf[i]
        tabl[i][0]=4+i
        # tabl[2][]


    print(cf)
    print(ogr)

    print(tabl)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
