# Проверка импортируемых данных -
# 1. количество передаваемых значений - id
# 2. проверка цифрового поля
# 3. Проверка логического поля
def CheckColValue(nameTable,checkValue):
    if nameTable=='users' or nameTable=='records' or nameTable=='orders':
        numValue=4
        if len(checkValue)==numValue: return True
        else: return False
    elif nameTable=='service':
        numValue = 2
        if len(checkValue)==numValue: return True
        else: return False

def ChekDigitColumnTable(nameTable,checkValue):
    if nameTable=='users':
        if checkValue[2].isdigit(): return True
        else: return False

def CheckBoolColumnTable(nameTable,checkValue):
    if nameTable=='users':
        if checkValue[3]=='0' or checkValue[3]=='1': return True
        else: return False


