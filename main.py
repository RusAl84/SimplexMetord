import numpy as np
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
zagolovok = ['БАЗИС', 'C', 0, 1, 2, 3, 4, 5, 6]

def rasstavit_1(tabl):
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
        tabl[i][2] = ogr[i][3]
    rasstavit_1(tabl)
    print(tabl)

    #определяем вектор который будем исключить из базиса
    nishnya_stroka=tabl[3][3:9]
    if np.min(nishnya_stroka)<0:
        vvodim_vektor=np.argmin(nishnya_stroka)+1
        print("vvodim vektor " + str(vvodim_vektor))
    #определяем вектор который исключаем
    tri_chisla=[0,0,0]
    for i in range(3):

        tri_chisla[i]=tabl[i][2]/tabl[i][vvodim_vektor+2]
        #print(tabl[i][vvodim_vektor+2])
    print(tri_chisla)
    pos_min=np.argmin(tri_chisla)
    min_el=np.min(tri_chisla)
    tabl[pos_min][0]=vvodim_vektor
    razresh_el=tabl[pos_min][vvodim_vektor+2]
    print("Разрешающий элемент " + str(razresh_el))
    for i in range(2,9):
        tabl[pos_min][i]/=razresh_el
        # tabl[2][]
    bazis=[0,0,0]
    for i in range(3):
        bazis[i]=tabl[i][0]
    rasstavit_1(tabl)

    for i in range(1,7):
        if i not in bazis:
            #print("ne v bazise " + str(i))
            i+=2
            print(tabl[0][i])
            for j in range(4):
                if j != pos_min:
                    z1=tabl[j][i]
                    z2=tabl[j][vvodim_vektor+2]
                    z3=tabl[pos_min][i]
                    #print(f"{z1}  {z2} {z3} ")
                    tabl[j][i]=z1-z2*z3
                    # правило треугольника z1 - z2 * z3




    # print(cf)
    # print(ogr)
    #np.set_printoptions(formatter={'float': '{: 0.1f}'.format})
    np.set_printoptions(formatter={'float': '{:5.0f}'.format})
    print(tabl)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
