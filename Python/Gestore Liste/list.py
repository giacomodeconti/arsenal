def main():
    x=10
    while x==10:
        print('===========================')
        print()
        print('Benvenuto nel gestore liste')
        print()
        risposta = 'x'
        elenco = 'z'
        print('===========================')
        print()
        print('1 Crea Lista')
        print('2 Modifica Lista')
        print('3 Elimina Lista')
        print('4 Sfoglia Liste')
        print()
        print('===========================')
        print()
        print('Scrivi il numero')
        print()
        elenco = input()
        if elenco == '1':
            print()
            import create
            create.main()
            break
        elif elenco == '2':
            print()
            import modify
            modify.main()
            break
        elif elenco == '3':
            print()
            import delete
            delete.main()
            break
        elif elenco == '4':
            print()
            import read
            read.main()
            break
        else:
            print()
            print('Comando non valido')
            print()









