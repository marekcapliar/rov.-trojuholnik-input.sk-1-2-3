def obdlznik(sirka, znak='*'):
    for i in range(sirka):
        print(znak, end='')
    print()
    print(znak, end='')
    for a in range(sirka-2):
        print(' ', end='')
    print(znak)
    for i in range(sirka):
        print(znak, end='')


obdlznik(30)
