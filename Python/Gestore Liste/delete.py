def main():
    import os
    z = 'D:\Gestore liste'
    print('===========================\n\nQuale lista vuoi eliminare?\n\n===========================\n')
    lista = (os.listdir(z))
    print('\n', lista)
    r=input()
    q=('\q')
    d='D:\Gestore liste'
    z=(d+q+r)
    print(z)
    os.remove('D:\Gestore liste\qlista')  #devo finire

