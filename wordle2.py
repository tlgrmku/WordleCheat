'''
Для жёлтых букв.
'''
fname = input('Имя созданного файла: ')
lname = input('Имя создаваемого файла: ')
symbol = input('Буква: ')
n = int(input('Местоположение буквы от 1 до 5: '))
textfile = []
with open(f'D:\\MyPython\\WordleCheat\\{fname}.txt', 'r', encoding='UTF-8') as f:
    for t in f.readlines():
        textfile.append(t.strip('\n'))

templist = []

for word in textfile:
    try:
        if not word.index(symbol) == n - 1:
            #print(word)
            templist.append(word + '\n')
    except:
        pass

print('Список готов!')
with open(f'D:\\MyPython\\WordleCheat\\{lname}.txt', 'a', encoding='UTF-8') as f:
    f.writelines(templist)