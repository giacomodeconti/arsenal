#!/usr/bin/python

# questo simbolo (#) serve per aggiungere un commento affianco alla stringa

#Uso del print

>>> print "hello" #print finziona sia per i str che per i int
>>> "hello" = "world"
>>> print "hello"
'world'
>>> print 1
1
>>> print 1-1
 0

# I SEGNI

# il segno * per la moltipliaczione 
# il segno ** per la potenza (2**2)
# il segno / per la frazione
# il segno + per l'addizione
# il segno - per la sottrazione
# ()[]{} le parentesi servono per dare la precedenza all'argomento
# la virgola serve per separare es: print ('Ciao', nome)
# l'apostrofo (questo ' o questo ") serve per ripetere qualcosa
# !=  significa diversi
# /n serve per andare a capo quando si scrive fra''

# float o string(str) o int e type mostra il valore della variabile 

>>> type (1.8) #float 
>>> type ("18") #str
>>> type ("ei") #str
>>> type (18) #int

#esempi

>>> ciao = type ("ei") # "ei"è str ma può essere anche float o int es: (1.8) (18)
>>> print ciao
<type> 'str'

#Uso dell'id

>>> id (3)
>>> print id(3) # l'id funziona solo con il print e non con il type
94586843222328
>>> betty = 3
>>> id (betty) 
94586843222328

# la funzione id prende un valore o una variabile e ritorna un intero che agisce come un identificatore unico del valore

# La conversione del tipo

>>> int # CONEVERTE LA VIRGOLA IN INTERI

>>> int ("32") #oppure senza le "
>>> int (3.9) #risulterà 3 perchè python arrotonda per difetto

>>> float # CONVERTE INTERI E STRINGHE CON LA VIRGOLA

>>> float (32)
32.0
>>> float (1.8)
1.8

>>> str # CONVERTE AL TIPO DI STRINGA 

>>> str (32)
'32'

#Uso dell'input

>>> nome=input('Come ti chiami?') #L'input serve a chiedere un'informazione all'utente
>>> print ('Ciao', nome)
Come ti chiami? Giacomo
Ciao Giacomo

#Uso dell'eval

#L'eval serve a convertire qualsiasi parola in numero senza le "

>>> scatola=input ('Dammi un numro')
Dammi un numero 10 #ora scatola eqivale a 10
>>> print scatola
10
#ma se facciamo
>>> print (scatola + 2) #bisogna usare l'eval
error
>>> scatola=eval (input('Dammi u numero'))
Dammi un numero 10
>>> print scatola
10
>>> print (scatola+5)
15

#Indicizzare le parole

>>> scatola='ciao a tutti'
>>> print (scatola[0])
c
>>> print (scatola[0:4]] # la : sta per dire di prendere dallo 0 al 4
ciao
#Spiegazione per una SINGOLA lettera
0123456789101112
ciao a tutti
#Spiegazione da lettera a lettera
0123456789101112
ciao a tutti #queso perchè ciao a tutti è ocupato da 12 spazi, 10 lettere e 2 spazi

#Le Liste 

>>> scatola=('ciao','auto','pasta','computer')
>>> print (scatola[1:3)
'auto', 'pasta' #ciao è l'elemento 0 auto 1 pasta 2 e computer 3. Il 3 non viene contanto quindi stamperà il numero 1 e 2

#Come verificare se una parlola è dentro alla lista

>>> scatola=['ciao','auto','pasta','computer'] # è meglio usare le parentesi [] per le liste, per rendere le modifiche più semplici
>>> print (scatola.count('motore')) #.count serve per verificare se c'è qualcosa dentro alla parola precedente, e dopo devo scrivere cosa voglio vereficare che ci sia dentro
0 #0 significa che non c'è
>>> print (scatola.count('auto'))
1 #1 significa che è in lista
>>> scatola.remove('auto') #.remove serve per rimuovere un oggetto dalla lista
>>> print scatola
#OPPURE
>>> del scatola[1] #per usare il del bisogna inserire il numero dell'oggetto nella lista
>>> print scatola # il del funziona solo quando la lista è compresa nelle parentesi []
['ciao','pasta','computer'] #ciao=0 auto=1 pasta=2 computer=3. auto è stato cancellato perchè è il numero 1
#Invece per aggiungere un'oggetto alla lista :
scatola.insert(2,'motore') #.insert appunto serve per aggiungere un'oggetto alla lista. Il 2 sta per dove voglio mettere l'oggetto, lo voglio mettere dopo auto (auto=1) quindi per metterlo dopo scriverò 2
scatola.append('lavandino') #con append metto l'oggetto inserito nell'ultimo posto, quindi dopo computer
scatola.reverse() #.reverse serve a capovolgere tutta la lista, quindi il lavandino da ultimo diventa primo
# Per sapere quanti oggetti appiamo in una lista uso il comando len che sta per lenght cioè lunghezza
>>> print (len(scatola))
6 #non sono 5 perchè non è l'indici cioè quando vado a modificare una lista che si parte da 0, ma qui è un semplice conteggio

# L'uso dell'if

chiave=10
>>> print chiave
10
>>>if chiave==10: # if significa SE. Con l'if se bisogna dire che qualcosa uguale all'altra, bisogna mettere 2 =
    print('ok') #In questo caso: Se la chiave è uguale a 10 stampa ok, altrimenti non scrivere nulla.
ok # i : sono un'istruzione necessaria, altrimenti da errore
>>>if chiave==9
    print('ok')
#non stamperà nella perchè la chiave non è uguale a 10

# L'uso dell'else

password=input('Inserisci la password')
if password=='giacomo':
    print ('password corretta')
else:               # else significa altrimenti, in questo caso, se(if) la password è giacomo stampa password corretta, altrimenti scrvi password errata
    print ('password errata')

# L'uso dell'elif

password = input('Inserisci la password')
if password == 'giacomo':
    print('password corretta')
elif password=='giorgio':  # elif è l'insieme fra: else e if=elif che significa altrimenti se
    print ('benvenuto ospite')
else:
    print('password errata')

# L'uso dell'and

print ('Inserisci i tuoi dati')
email=input('Scrivi la tua email ')
password=input('Scrivi la tua password ')
if email=='gg@gg.it' and password=='gg': # and significa e. Quindi se(if) l'email è gg@gg.it e(and) la password è gg, esegui l'accesso
    print ('Benventuo')
else:
    print('Accesso negato')

# L'uso dell'or

print('Inserisci i tuoi dati')
email = input('Scrivi la tua email o telefono ')
password = input('Scrivi la tua password ')
if ((email == 'gg@gg.it' or email == '3400566') and password == 'gg'):
    print('Benventuo')  # or significa oppure, quindi se l'email o il telefono(che sarebbe la seconda email) e la password sono esatti, entri nel sistema.
else:
    print('Accesso negato')

# L'uso del not

a=2
b=1
if (not(a==b)): # not significa no. Quindi se a non è uguale a b stampa ciao
    print 'ciao'

a=2
b=1
if (a!=b): #si può scrivere anche così != significa diversi e si mette al posto del ==. Quindi se a è diverso da b stampa ciao
    print 'ciao'

# L'uso dell'in

a='ciao'
if 'c' in a: # in vuol dire è dentro. Quindi se c è dentro a stampa ok
    print ('ok')

oppure

a=['ciao','bene']
if ('sicuro' not in a):  # se sicuro non è in a stampa ok
    print ('ok')

# L'uso del while

a=10
         # while è una funzione ciclica, cioè si ripete all'infinito
while a>1: # while significa fino a che. Quindi fino a che a è maggiore di uno stampa ok (stamperà all'infinito).
    print ('ok')
 # per stopparlo

a=10

while a>1:
    print ('ok') # qui si stoppa perchè il valore di a è inferiore all'1
    a=0

# L'uso del for

# Il for serve a trasferire gli oggeti di una lista in un'altra

a='ciao'
for x in a: # In questo modo creo una nuova variabile x, e trasferisco il contenuto di a in x
    print(x)

# L'uso del break

a=['ciao','ei','come']
for x in a:
    if x=='ei':
        break # questa funzione break rompe il ciclo e fa si che si blocchi
print('Finito')

# L'uso del continue

a=['ciao','ei','come']
for x in a:
    if x=='ei':
       continue # serve a continuare il ciclo senza una determinata cosa. In questo caso senza l'ei, se x=ei continua senza esso. Quindi stamperà ciao, come
print('Finito')

# L'uso del pass

a=['ciao','ei','come']
for x in a:
    if x=='ei':
        pass # il pass serve a continuare la lettura senza errori, di solito si usa quando bisogna finire ancora il codice, in tal modo python può proseguire senza errori
print('Finito')

# L'uso del range

for x in range(10):
    print('Numero',x+1) # il range dice a python che deve partire da 0 a contare, in questo caso conta da 0 a 9=10numeri come scritto

# I dizionari

x={'tubi':2,'cavi':3,} # per far si che x diventi un dizionario bisogna usare {} e per dire che un'oggetto è più di 1 basta scrivere 'nome oggetto':3 al posto del 3 puoi mettere qualsiasi vaolre
x['rame':5]
print (x['tubi'])


