turtle_guess = input('Хотите, я что-нибудь нарисую?\n')
if turtle_guess in ['да', 'yes', 'lf', 'нуы', 'Yes', 'Нуы', 'Да', 'Lf']:
    import turtle
    i = 1
    print("Вводите цвета на английском языке c через запятую.")
    colors = input()
    colors = colors.split(', ')
    pups = len(colors)
    bgcolor = input('Введите цвет заднего фона:\n')
    if bgcolor == '':
        bgcolor = 'Black'
    t = turtle.Turtle()
    turtle.bgcolor(bgcolor)
    try:
        print('Загрузка...')
        for pups in range(360):
            t.pencolor(colors[pups % len(colors)])
            t.width(pups / 100 + 1)
            t.forward(pups)
            t.left(59)
        print('Рисунок готов!')
    except Exception as e:
        print(f'Ошибка: {e}')
else:
    print('Ладно...')
end = input('Нажмите enter, чтобы выйти.')