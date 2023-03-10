import socket
import sys

def invia_comandi(s):
    while True :
        comando = input('->')
        if comando == 'ESC':
            print ('Sto chiudendo la connessione sol server')
            s.close()
            sys.exit()
        else:
            s.send(comando.encode())
            data = s.recv(4096)
            print(str(data, 'utf-8'))
def conn_sub_server(indirizzo_server):
    try:
        s = socket.socket() #creazione socket client
        s.connect(indirizzo_server)
        print(f'Connessione al Server {indirizzo_server} stabilita')
    except socket.error as errore:
        print('Sto uscendo \n error')
        sys.exit()
    invia_comandi(s)

if __name__ == '__main__':
    conn_sub_server(('192.168.127',80))
