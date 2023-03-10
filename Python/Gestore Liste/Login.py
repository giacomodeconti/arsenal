__authors__ = 'Giacomo'

risposta=('xy')
accesso=('Accesso negato')
z=75
print('======================\n')
print('______BENVENUTO_______\n')
print('======================\n')
print('Inserisci i tuoi dati\n')
print('======================\n')
while z==75:
    print('Inserisci il nome utente\n ')
    nomeutente = input()
    print()
    print('Inserisci la password\n ')
    password = input()
    if (((nomeutente == '1') and password == '1') or (nomeutente == 'giorgio') and password == '123'):
        print()
        print('===============================\n')
        print('Sei entrato come amministratore\n')
        print('===============================\n')
        import list
        list.main()
    elif (((nomeutente == 'francesco') and password == '909') or (nomeutente == 'mirco') and password == '909'):
        print()
        print('========================\n')
        print('Sei entrato come operaio\n')
        print('========================\n')
        import list
        list.main()
    else:
        print('Accesso negato')


















