import sys
import re
import math
#sys.argv = ['task2.py', 'filepath']

def intersSphLine(filepath):
    try:
        file1 = open(filepath, 'r')
    except Exception:
        print("Неправильно указан путь к файлу или файл не найдет")
        return
    for line in file1:
        print(line)
        keys = line.split()
        #Исключение лишних символов из ключей
        for i in range(0, len(keys)):
            keys[i] = re.sub('\[|\]|\{|\}|\,|\:', '', keys[i])
        #Считывание ключей - координат X Y Z центра сферы после слова center
        #R радиуса сферы после слова radius, 
        #координат точек линии X1 Y1 Z1 X2 Y2 Z2 после слова line
        xSph = float(keys[keys.index('center') + 1])
        ySph = float(keys[keys.index('center') + 2])
        zSph = float(keys[keys.index('center') + 3])
        r = float(keys[keys.index('radius') + 1])
        x1 = float(keys[keys.index('line') + 1])
        y1 = float(keys[keys.index('line') + 2])
        z1 = float(keys[keys.index('line') + 3])
        x2 = float(keys[keys.index('line') + 4])
        y2 = float(keys[keys.index('line') + 5])
        z2 = float(keys[keys.index('line') + 6])
        #Решения задачи о пересечении линии со сферой через квадратичное уравнение
        #a*t**2 + b*t + c = 0
        a = (x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2
        b = -2*((x2 - x1)*(xSph - x1) + (y2 - y1)*(ySph - y1) + (zSph - z1)*(z2 - z1))
        c = (xSph - x1)**2 + (ySph - y1)**2 + (zSph - z1)**2 - r**2
        disc = b**2 - 4*a*c
        if disc > 0:
            t1 = (-b+math.sqrt(disc))/(2*a)
            t2 = (-b-math.sqrt(disc))/(2*a)
            xt1 = round(x1 + (x2 - x1)*t1,2)
            yt1 = round(y1 + (y2 - y1)*t1,2)
            zt1 = round(z1 + (z2 - z1)*t1,2)
            xt2 = round(x1 + (x2 - x1)*t2,2)
            yt2 = round(y1 + (y2 - y1)*t2,2)
            zt2 = round(z1 + (z2 - z1)*t2,2)
            print("Линия заданная точками: {}{}".format([x1,y1,z1],[x2,y2,z2]))
            print("пересекает сферу заданную центром {} и радиусом {}".format([xSph,ySph,zSph],r))
            print("в точках {} и {}".format([xt1,yt1,zt1],[xt2,yt2,zt2]) + '\n')
        elif disc == 0:
            t = -b/(2*a)
            xt1 = round(x1 + (x2 - x1)*t,2)
            yt1 = round(y1 + (y2 - y1)*t,2)
            zt1 = round(z1 + (z2 - z1)*t,2)
            print("Линия заданная точками: {}{}".format([x1,y1,z1],[x2,y2,z2]))
            print("касается сферы заданной центром {} и радиусом {}".format([xSph,ySph,zSph],r))
            print("в точке {}".format([xt1,yt1,zt1]) + '\n')
        else:
            print("Линия заданная точками: {}{}".format([x1,y1,z1],[x2,y2,z2]))
            print("не пересекает сферу заданную центром {} и радиусом {}".format([xSph,ySph,zSph],r) + '\n')
    file1.close()
    return
    

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        intersSphLine(str(sys.argv[1]))
    else:
        print("Отсутсвует аргумент")
        print("Ожидаемый аргумент - путь к файлу")