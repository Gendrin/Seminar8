# Добавление / Удаление / Редактирование записей БД
import sqlite3

def seq(nameTable):
    connect = sqlite3.connect('barbershop.db')
    cursor = connect.cursor()
    cursor.execute("SELECT max(id) FROM {0};".format(nameTable))
    maxId = cursor.fetchone()
    seq= maxId[0]
    connect.close()
    if seq==None: return 1
    else:
        return seq+1

def InsertTable(nameTable,inData):
    if inData!=None:
        connect = sqlite3.connect('barbershop.db')
        cursor = connect.cursor()
        if nameTable == 'users' or 'records' or 'orders':
            cursor.execute("INSERT INTO {0} VALUES(?, ?, ?, ?, ?);".format(nameTable), inData)
        elif nameTable == 'service':
            cursor.execute("INSERT INTO {0} VALUES(?, ?, ?);".format(nameTable), inData)
        connect.commit()
        connect.close()
    else:
        print('Введены некорректные данные! Добавление записи в таблицу отменено.')

def UpdateUser(inId,inData):
    if inData!=None:
        connect = sqlite3.connect('barbershop.db')
        cursor = connect.cursor()
        sql=CreateSQLStr("UPDATE users SET ",inData)+" WHERE id={0}".format(inId)
        print(sql)
        cursor.execute(sql)
        if(input('Вы уверены в редактировании пользователя? Подтвердить операцию - "1", отмена - "any key"'))=='1':
            connect.commit()
        connect.close()
def DeletRecord(nameTable,inId):
    #global connect
    if inId!=None:
        try:
            connect = sqlite3.connect('barbershop.db')
            cursor = connect.cursor()
            sql = "DELETE FROM {0} WHERE id={1}".format(nameTable, inId)
            print(sql)
            cursor.execute(sql)
            if (input('Вы уверены в удалении записи? Подтвердить операцию - "1", отмена - "any key"')) == '1':
                connect.commit()
                print('Запись успешно удалена!')
                cursor.close()
            else:
                print('Отмена удаления записи!')
                cursor.close()
        except sqlite3.Error as Error:
            print('Ошибка при работе с SQLite',Error)
        finally:
            connect.close()

def ViewExpTable(nameTable):
    try:
        connect = sqlite3.connect('barbershop.db')
        cursor = connect.cursor()
        sql = "SELECT * FROM {0} ".format(nameTable)
        print(sql)
        cursor.execute(sql)
        result = cursor.fetchall()
        cursor.close()
        expList=[]
        for i in range(len(result)):
            expString='';
            for j in range(len(result[i])):
                print(result[i][j],end=' ')
                if j<len(result[i])-1:
                    expString+=str(result[i][j])+';'
                else: expString+=str(result[i][j])
            if i>5 and i%5==0: input('Нажмите любую клавишу!')
            print()
            expList.append(expString)
    except sqlite3.Error as Error:
        print('Ошибка при работе с SQLite', Error)
    finally:
        #print(expList)
        return expList
        connect.close()



def CreateSQLStr(startSQL,inData):
    flag= 0
    for i in range(len(inData)):
        if inData[i] != '':
            if i == 1: startSQL, flag = startSQL + ' fname=' + "'" + str(inData[i]) + "'", flag + 1

            if i == 2 and flag==0: startSQL, flag = startSQL + 'lname=' + "'" + str(inData[i]) + "'", flag + 1
            elif i == 2 and flag==1: startSQL, flag = startSQL + ', lname=' + "'" + str(inData[i]) + "'", flag + 1

            if i == 3 and flag==0: startSQL, flag = startSQL + 'phone=' + str(inData[i]), flag + 1
            elif i == 3 and flag>=1: startSQL, flag = startSQL + ', phone=' + str(inData[i]), flag + 1
    if flag:
        return startSQL
    else: return None

def FindInTable(nameTable,inData):
    if inData!=None:
        connect = sqlite3.connect('barbershop.db')
        cursor = connect.cursor()
        if nameTable == 'users':
            sql="SELECT * FROM {0} WHERE".format(nameTable)
            flag=0
            for i in range(len(inData)):
                if inData[i]!='':
                    if i == 0: sql,flag = sql + ' fname=' + "'" + str(inData[i]) + "'",flag+1
                    if i == 1: sql,flag = sql + ' lname=' + "'" + str(inData[i]) + "'",flag+1
                    if i == 2: sql,flag = sql + ' phone=' + str(inData[i]),flag+1
            if flag:
                cursor.execute(sql)
                result = cursor.fetchall()
                connect.close()
                if len(result)>1:
                    print(f'Обнаружено более одного значения, повторите с дополнительными данными -> {result}')
                    return None
                elif len(result)==1:
                    #print(f'Результат поиска -> Имя: {result[0][1]} Очество: {result[0][2]} Телефон: {result[0][3]}')
                    return result[0][0],'Результат поиска -> Имя: {0} Очество: {1} Телефон: {2}'\
                        .format(result[0][1],result[0][2],result[0][3])
                elif len(result)==0:
                    print('Данные по условиям поиска не обнаружены!')
                    return None
            else:
                print('Данные для поиска введены не верно/отсутствуют!')
                return None
    else:
        print('Данные для поиска введены не верно/отсутствуют!')
        return None

def InsertDataForSearch(nameTable):
    if nameTable=='users':
        print('Ввод информации для поиска пользователей')
        print('Введите информацию о клиенте разделенную запятыми в формате: x,x,x - Пример: Иван,,')
        inData = input('Имя, Отчество, телефон - минимум одно значение').split(',')
        if len(inData) == 3:
            if inData[2] == '':
                return inData
            elif inData[2].isdigit():
                return inData
            else:
                print('Некорректный ввод номера телефона')
                return None


def InsertUser():
    print('Ввод информации о клиентах, мастерах:')
    print('Введите информацию о клиенте разделенную запятыми в формате: Иван,,,1')
    inData = input('Имя, Отчество - необязательно, телефон, клиент или мастер -> 1 или 0: ').split(',')
    if len(inData) == 4 and inData[3].isdigit():
        inData.insert(0, str(seq('users')))
        inData = tuple(inData)
        print(inData)
        return inData
    else: return None
def EditUser():
    resultFind = FindInTable('users', InsertDataForSearch('users'))
    if resultFind!=None:
        if resultFind[0] != None:
            print(f'Старые данные {resultFind[1]}')
            inData = InsertUser()
            if inData != None:
                print(f'Новые данные {inData[1]} {inData[2]} {inData[3]} {inData[4]}')
                UpdateUser(resultFind[0], inData)
def DeleteUser():
    resultFind = FindInTable('users', InsertDataForSearch('users'))
    if resultFind!=None:
        if resultFind[0] != None:
            print(f'Удаляемые данные {resultFind[1]}')
            DeletRecord('users', resultFind[0])


exp = ViewExpTable('users')
print()
print(exp)
# test=InsertDataForSearch('users')
# test=FindInTable('sers',test)
# print(test)
# Чтобы удалить или отредатировать пользователя его предварительно нужно найти.
# Для поиска формируем кортеж данных через ф-ию InsertUser, если результат однозначен - 1 позиция
# Удаление - подтверждение
# Редактирование - повторный ввод нового значения.
#FindInTable('users', me.InsertDataForSearch('users')))
#print(InsertDataForSearch('users'))

#findId,strResult=FindInTable('users',InsertDataForSearch('users'))
# resultFind=FindInTable('users',InsertDataForSearch('users'))
# if resultFind[0]!=None:
#      print(f'Старые данные {resultFind[1]}')
#      inData=InsertUser()
#      print(f'Новые данные {inData[1]} {inData[2]} {inData[3]} {inData[4]}')
#      if inData!=None:
#          UpdateUser(resultFind[0],inData)




#UpdateUser(FindInTable('users',InsertDataForSearch('users')),InsertUser())

#def EditUser():
#inData=('','','123')
#test=InsertDataForSearch('users')
#print(test)
#print(FindInTable('users',InsertDataForSearch('users')))

# print(seq('users'))
# print(seq('records'))
# print(seq('service'))
# print(seq('orders'))
# insertUsers()
#print('Введите информацию о клиенте разделенную запятыми в формате:')
# inData=input('Имя, Отчество - необязательно, телефон, клиент или мастер -> 1 или 0: ').split(',')
# if len(inData)==4 and inData[3].isdigit():
#     inData.insert(0,str(seq('users')))
#     inData=tuple(inData)
#     print(inData)
# else:
#     print('Введены некорректные данные!')