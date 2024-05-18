print('Вас приветствует программа, для которой я пока не придумал название! ')
print('Введите ваш текст. Остановите ввод текста, написав "всё" на следующей', end=' ')
print('строке после вашего текста и нажав enter.')
text = str(input())
while True:
    text1 = input()
    if text1 in ['all', 'that is it', 'that\'s it', 'dc`', 'dct', 'Dct', 'Dc`' "всё", "Всё", "все", "Все"]:
        break
    text += '\n' + text1
print("\r" + 'Программа приняла ваш текст:\n', text, sep='')
word_count = 0
print('Режим замены слов включён.')
user_word1 = input('Введите слово, которое требуется заменить: \n')
word_count = text.count(user_word1)
if word_count > 0:
    print('Слово встречается в тексте ', word_count, " раз.")
    user_word2 = input('Введите слово, на которое нужно заменить слово выше: \n')
    text = text.replace(user_word1, user_word2)
    print('Результат: \n', text, sep='')
else:
    print('Слово не встречается в тексте.')
exitt = input('Нажмите enter, чтобы выйти. \n')
