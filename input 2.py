def riadok(n, text=''):
    if len(text) != 0:
        text = ' ' + text + ' '
    a = len(text)
    n -= a
    for i in range(n // 2):
        print('*', end='')
    print(text, end='')
    for i in range(40 - (n // 2) - a):
        print('*', end='')
    print('\n')


sir = 40
riadok(sir)
riadok(sir, 'Ján Botto')
riadok(sir, 'Žltá ľalija')
riadok(sir, '-')
riadok(sir, 'Stojí stojí mohyla')
riadok(sir, 'Na mohyle zlá chvíľa')
riadok(sir, 'na mohyle tŕnie chrastie')
riadok(sir, 'a v tom tŕní chrastí rastie')
riadok(sir)
