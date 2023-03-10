Operatore 	Funzione
< 	minore di
<= 	minore o uguale a
> 	maggiore di
>= 	maggiore o uguale a
== 	uguale
!= 	diverso da
<> 	variante di diverso da
 ___________________________________

 range(start, stop, step)

----------------------------------------------------
 I dizionari
----------------------------------------------------
 vengono usate le parentesi {['']}
 .keys() #Chiavi di un dizionario
 es: {['gatto':'cane']} # gatto è la chiave
 .value() #Valori di un dizionario
 es: {['gatto':'cane']} # cane è il valore
 .items() #Coppie chiavi valore
 es: {['gatto''cane']} #gatto chiave, cane valore= items
 .setdefault() #Serve per aggiungere un items al dizionario
 es: lista.setdefault('motore','moto')
     lista{['gatto':'cane','motore','moto']}
 .get() #evita un crash del programma se una elemento del dizionario non è presente
 es:
lista={['ciao','cane']}
 lista.get('birra','Chiave non trovata') #Se birra è dentro la lista dirà chiave non trovata
 >>> Chiave non trovata
mentre
 lista.get('ciao','Chiave non trovata') #
 >>> ciao

 ----------------------------------------------------
