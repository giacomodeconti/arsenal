def main():
    print('==========================')
    print()
    print('Che lista vuoi modificare?')
    print()
    print('==========================')
    print()
    import os
    print(os.listdir('D:\Gestore liste'))
    lista=input()
    if lista=='1':
        open('D:\Gestore liste\lista1.txt','r').read()





