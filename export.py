
def exportFile(nameTable,expData):
    with open(nameTable+'Exp.csv', 'w', encoding='utf-8') as expFile:
        for i in range(len(expData)):
            expFile.write(expData[i]+'\n')
            #print(expData[i])
        expFile.close