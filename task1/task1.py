import sys
#sys.argv = ['task1.py', 'nb', 'base', 'baseDst']

def tobase(nb, base, baseDst=None):
    Result = ''
    Length = len(base)
    if baseDst is not None:
    #Возврат числа к десятичной системе счисления
        Base10 = 0
        LengthNb = len(nb)
        for i in range(0, LengthNb):
            try:
                Base10 = Base10 + base.index(nb[i])*(Length)**(LengthNb-i-1)
            except Exception:
                print("Исходное число содержит символ не входящий в его систему счисления")
                return
        Length = len(baseDst)
        print("Результат перевода " + str(nb) + " из системы счисления " + str(base) + " к системе счисления " + str(baseDst) + ":")
        base = baseDst
    else:
        Base10 = nb
        print("Результат перевода " + str(nb) + " из десятичной к системе счисления " + str(base) + ":")
    #Перевод десятичного числа к новой системе счисления
    while Base10 > 0:
        Result = base[Base10%Length] + Result
        Base10 = Base10//Length
    print(Result)
    return
    

if __name__ == "__main__":
    if len(sys.argv) == 3:
        try:
            tobase(int(sys.argv[1]), str(sys.argv[2]))
        except Exception:
            print('Невозможно привести первый аргумент к целому числу')
    elif len(sys.argv) == 4:
        tobase(str(sys.argv[1]), str(sys.argv[2]), str(sys.argv[3]))
    else:
        print("Неправильное количество аргументов" + '\n')
        print("Входные аргументы для перехода от десятичной системы счисления:" + '\n' 
        + "nb - Десятичное число" + '\n' + "base - Символы искомой системы счисления в порядке возврастания" + '\n')
        print("Входные аргументы для изменения системы счисления:" 
        +'\n' + "nb - Число в произвольной системе счисления" + '\n'
        + "base - Символы исходной системы счисления в порядке возврастания" + "\n"
        + "baseDst - Символы искомой системы счисления в порядке возврастания")