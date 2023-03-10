def main():
    import os
    z='D:\Gestore liste'
    for x in range (1, 2):
        lista = (os.listdir(z))
        import winsound
        print('====================\n')
        print('Sto caricando ...\n')
        print('===================')
        winsound.Beep(37, 2000)
        print(lista)



