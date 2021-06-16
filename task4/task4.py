import sys

def compare(firstword, secondword):
    if "*" in firstword:
        print("Символ * не должен быть частью первой строки")
        return
    #Флаг = 0 - символы слов должны совпадать либо второе слово должно иметь *
    #Флаг = 1 - допускается любой символ в первом слове
    #флаг = 2 - первое слово закончились, а второе нет
    flag = 0 
    comp1 = 0
    comp2 = 0
    while True:
        #Проверка оставшихся символов второго слова по окончанию первого
        if flag == 2:
            while True:
                if secondword[comp2] == '*':
                    if comp2 < (len(secondword) - 1):
                        comp2 += 1
                    else:
                        #Все оставшиеся символы второго слова равны *
                        print('OK')
                        return
                else:
                    #Обнаружено различие
                    print('KO')
                    return
        #Если сравнимые символы совпадают
        elif firstword[comp1] == secondword[comp2]:
            flag = 0
            #Оба слова закончились, несовпадение не обнаружено
            if comp1 == (len(firstword) - 1) and comp2 == (len(secondword) - 1):
                print('OK')
                return
            #Следующий символ первого слова
            if comp1 < (len(firstword) - 1):
                comp1 += 1
            else:
                #Первое слово закончились
                flag = 2
            #Следующий символ второго слова
            if comp2 < (len(secondword) - 1):
                comp2 += 1
            else:
                #Первое слово не может содержать символа *
                #окончание второго слова раньше первого не на * означает их различие
                print('KO')
                return
        #Символы не совпадают
        else:
            #Если второе слово имеет символ * переход к следующему символу второго слова
            if secondword[comp2] == '*' and comp2 < (len(secondword) - 1):
                flag = 1
                comp2 += 1
            #Если второе слово закончилось символом * и различий в слове до этого не было найдено, слова совпадают
            elif secondword[comp2] == '*' and comp2 == (len(secondword) - 1):
                print('OK')
                return
            #Символы не совпадают и второе слово не имеет сопостовимого символа *
            elif flag == 0:
                print('KO')
                return
            #Символ первого слова относится к * во втором, переход к следующей букве первого слова
            elif flag == 1:
                if comp1 < (len(firstword) - 1):
                    comp1 += 1
                else:
                    #В первом слове не осталось символов которые можно сопоставить символу второго слова
                    print('KO')
                    return
    return



if __name__ == "__main__":
    if len(sys.argv) == 3:
        compare(str(sys.argv[1]), str(sys.argv[2]))
    else:
        print("Неверные входные аргументы. Ожидается два слова")