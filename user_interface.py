import modcontrol as mc
def StartMenu():
    print("Barbershop welcomes you!\n\n\n")
    print("Working with:\n")
    print("1 - Pre-registration - Предварительная запись на услугу\n")
    print("2 - Complite orders - - Оформление/просмотр выполненных работ\n")
    print("3 - Add base Client\Master - Конфигурирование пользователей в системе Клиенты/Мастера\n")
    print("4 - Configurate service - Конфигурирование оказываемых услуг\n")
    print("0 - exit\n")
    chk=input()
    if chk=='1': print('Меню предварительной записи в разработке')
    elif chk=='2': print('Меню оформления выполненных работ в разработке')
    elif chk == '3':MenuConfigUser()
    elif chk == '4':print('Меню онфигурирования услуг в разработке')
    elif chk=='0': return
    else:
        print('Выбрано не верное число')
        return
# Доавить пользователя / Удалить пользователя / Изменить пользователя
# Импортировать пользователей из файла
# Экспортировать пользователей в файл
def MenuConfigUser():
    print("Config users welcomes you!\n\n\n")
    print("Working with:\n")
    print("1 - Add User\n")
    print("2 - Edit user\n")
    print("3 - Delete user\n")
    print("4 - View all user\n")
    print("5 - Import users from file\n")
    print("6 - Export users in files\n")
    print("0 - Start menu\n")
    chk = input()
    if chk == '1'or chk == '2' or chk == '3' or chk == '4' or chk == '5' or chk == '6':
        mc.Operation(chk)
        input('Нажмите ввод для продолжения')
        MenuConfigUser()
    elif chk == '0': StartMenu()
    else:
        print('Выбрано не верное число')
        return
