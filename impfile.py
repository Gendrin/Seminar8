import exception as exp

def importFile(nameFile):
        with open(nameFile, 'r', encoding='utf-8') as impFile:
            listImpString=impFile.readlines()
            listTuple = []
            if listImpString != None:
                for i in range(len(listImpString)):
                    str = listImpString[i].strip()
                    str = tuple(str.split(';'))
                    if exp.ChekDigitColumnTable('users', str):
                        if exp.CheckColValue('users', str):
                            if exp.CheckBoolColumnTable('users', str):
                                listTuple.append(str)
                            else:
                                print(
                                    f'В имортируемой строке введены не верно булевое значение 1/0, отказано в импорте -> {str}')
                        else:
                            print(f'В имортируемой строке введены не верно числовые значения, отказано в импорте -> {str}')
                    else:
                        print(f'Срока с некорректным количеством значений, отказано в импорте -> {str}')
            print('Импортируемые данные - >',listTuple)
            impFile.close()
        return listTuple

#result = importFile('usersImp.csv')
#
#
# print()
# print(result)
