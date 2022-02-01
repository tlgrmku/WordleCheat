'''
Исключение слов с серыми буквами 
'''
textfile = [] 
with open('words.txt', 'r', encoding='UTF-8') as f:
    for t in f.readlines():
        textfile.append(t.strip('\n'))

black = input('Сервые буквы: ')
white = input('Жёлтые буквы: ')
lname = input('Имя создаваемого файла: ')

blacklist = []
whitelist = []

for e in black:
    for word in textfile:
        if word not in blacklist:
            if word.find(e) >= 0:
                blacklist.append(word)
            else:
                pass
        else:
            pass

for i in white:
    for word2 in textfile:
        if word2 not in blacklist:
            if word2.find(i) >= 0:
                whitelist.append(word2 + '\n')
            else:
                pass
        else:
            pass

print('Список готов!')
with open(f'{lname}.txt', 'a', encoding='UTF-8') as f:
    f.writelines(whitelist)





