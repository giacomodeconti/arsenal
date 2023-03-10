
    risposta='z'
    oggetto='v'
    print('=============================')
    print()
    print('Inserisci il nome della lista')
    print()
    print('=============================')
    print()
    lista=input()
    liste = (open('D:\Gestore liste\lista.txt', 'w'))
    liste.write()
    print()
    print('Hai creato la lista di nome',lista,)
    m=2
    while m!=20:
        print()
        print('Vuoi aggiungere qualcosa? Si o No\n')
        risposta=input()
        if risposta=='Si':
            print()
            print('Cosa vuoi aggiungere?\n')
            lista=(open('D:\Gestore liste\lista.txt','w'))
            lista.write(input())
        elif risposta=='No':
            print('===================================\n')
            print('Vuoi chiudere il programma? Si o No\n')
            print('===================================\n')
            risposta=input()
            if risposta=='Si':
                print()
                break
            else:
                print()
                print('Cosa vuoi aggiungere?')
                print()
                lista = (open('D:\Gestore liste\lista.txt', 'w'))
                lista.write(input())














