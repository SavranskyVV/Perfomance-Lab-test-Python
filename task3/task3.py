import sys
import re
import datetime
#sys.argv = ['task3.py', 'filepath', 'startlog', 'endlog']
#Приведение даты к типу datetime
def datestandart(strtime):
    strtime = re.split('-|T|:|Т', strtime)
    #Исключение trailing zeros мешающих переходу к datetime 
    for i in range(1,5):
        if strtime[i][0] == 0:
            strtime[i] = strtime[i][1]
    strtime = datetime.datetime(int(strtime[0]),int(strtime[1]),int(strtime[2]),int(strtime[3]),int(strtime[4]),int(strtime[5]))
    return strtime

def logread(filepath, startlog, endlog):
    try:
        startlog = datestandart(startlog)
    except Exception:
        print("Невозможно привести второй аргумент к datetime" + '\n' 
        + "убедитесь что формат соответсвует год-месяц-деньТчас:минута:секунда и не содержит других разделителей")
        return
    try:
        endlog = datestandart(endlog)
    except Exception:
        print("Невозможно привести третий аргумент к datetime" + '\n' 
        + "убедитесь что формат соответсвует год-месяц-деньТчас:минута:секунда и не содержит других разделителей")
        return
    if startlog > endlog:
        print("Время окончания выборки не может быть раньше времени начала выборки")
        return
    try:
        file1 = open(filepath, 'r')
    except Exception:
        print("Неправильно указан путь к файлу или файл не найдет")
        return
    #num_lines = sum(1 for line in file1)
    #if num_lines <= 2:
       # print("Недостаточное количество строк в log файле")
       # return
    volume = int(file1.readline())
    current = int(file1.readline())
    counttasks = 0
    counttopups = 0
    counterrors = 0
    toped = 0
    topupfails = 0
    scooped = 0
    scoopfails = 0
    for line in file1:
        logline = re.split(' - ', line)
        logtime = datestandart(logline[0])
        logaction = logline[2]
        if logtime <= endlog and logtime >= startlog:
            #Запись в логе находится в интерисуемом интервале
            counttasks += 1
            try:
                firstlog
            except NameError:
                firstlog = logtime
                firstcurrent = current
            if 'scoop' in logaction:
                needed = int(re.search(r'\d+', logaction).group())
                if needed <= current:
                    current = current - needed
                    scooped += needed
                else:
                    counterrors += 1
                    scoopfails += needed
            if 'top up' in logaction:
                counttopups += 1
                needed = int(re.search(r'\d+', logaction).group())
                if needed <= (volume - current):
                    current = current + needed
                    toped += needed
                else:
                    counterrors += 1
                    topupfails += needed
        elif logtime < startlog:
            #Запись в логе находится до интерисуемого интервала, отслеживается изменения уровня воды
            if 'scoop' in logaction:
                needed = int(re.search(r'\d+', logaction).group())
                if needed <= current:
                    current = current - needed
            if 'top up' in logaction:
                needed = int(re.search(r'\d+', logaction).group())
                if needed <= (volume - current):
                    current = current + needed
        else:
            #Запись в логе находится после интерисуемого интервала, прекращение чтения лога
            lastcurrent = current
            break
    try:
        lastcurrent
    except NameError:
        lastcurrent = current
    with open('Result.csv', "w", newline='') as csv_file:
        csv_file.write("[Действий][Ошибок][Залито][Не Залито][Забрано][Не Забрано][Было][Стало]\n")
        if counttasks != 0:
            counterrors = "{:.0%}".format(counterrors/counttasks)
        else:
            lastcurrent = '-'
            firstcurrent = '-'
        csv_file.write("[{} действий][{}][{}л][{}л][{}л][{}л][{}л][{}л]".format(counttasks,counterrors,toped,topupfails,scooped,scoopfails,firstcurrent,lastcurrent))
    file1.close()
    return
    

if __name__ == "__main__":
    if len(sys.argv) == 4:
        logread(str(sys.argv[1]),str(sys.argv[2]),str(sys.argv[3]))
    else:
        print("Неверное количество аргументов")
        print("Ожидаемые аргументы - путь к log файлу" + '\n'
        + "время начала и конца лога в формате год-месяц-деньТчас:минуты:секунды" + '\n'
        + "ожидаемый формат лог файла:" + '\n' + "Вместимость бочки первой строкой" + '\n' 
        + "Количество воды в бочке на момент начала ведения лога второй строкой"
        + '\n' + "записи в формате Время (год-месяц-деньТчас:минута:секунда) - Пользователь - Действие (top up/scoop) и количество воды")