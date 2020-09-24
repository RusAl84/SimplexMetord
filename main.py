import numpy as np
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def rasstavit_1(tabl):
    zagolovok=['БАЗИС','C',0,1,2,3,4,5,6]
    for g in range(3):
        z = tabl[g, 0]
        for i in range(3,9):
            if zagolovok[i]==z:
                for j in range(4):
                    tabl[j][i]=0
                tabl[g][i]=1

# Press the green button in the gutter to run the script.
if __name__ == '__main__':


    cf =np.zeros((1,3))
    ogr=np.zeros((3,4))
    tabl = np.zeros((4, 9))
    cf=[9,10,16]
    ogr=[[18,15,12,360],
         [6,4,8,192],
         [5,3,3,180]]
    #Заполним табличку
    for i in range(3):
        tabl[3][3+i] = (-1) * cf[i]
        tabl[i][0]=4+i
        for j in range(3):
            tabl[j][3+i]=ogr[j][i]
        tabl[i][2] = ogr[i][0]
    rasstavit_1(tabl)



        # tabl[2][]


    print(cf)
    print(ogr)

    print(tabl)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
