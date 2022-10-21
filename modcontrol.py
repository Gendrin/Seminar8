import edit as me
import export as exp
import impfile as impf





def Operation(code_op):
    if code_op =='1': me.InsertTable('users',me.InsertUser())
    elif code_op =='2':
        print('Редактируем пользователя! Задайте критерии поиска!')
        me.EditUser()
    elif code_op =='3':
        print('Удаляем пользователя! Задайте критерии поиска!')
        me.DeleteUser()
    elif code_op =='4':
        print('Отображаем всех пользователей информационной системы!!')
        me.ViewExpTable('users')
    elif code_op =='5':
        print('Импорт пользователей из файла в базу!!')
        #impf.importFile('usersImp')
    elif code_op =='6':
        print('Экспорт пользователей информационной системы в файл!!')
        exp.exportFile('users',me.ViewExpTable('users'))
