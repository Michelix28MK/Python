print("Benvenuto a: INDOVINA IL NUMERO")
print("Come ti chiami?")
nome_giocatore=input()
print("Buona fortuna " + nome_giocatore)
numero_segreto=8
print("Indovina il numero segreto, da 1 a 10")
tent=1

while(True):
    
    numero_inserito= int(input())
    if(numero_segreto == numero_inserito):
        print(nome_giocatore+"hai indovinato!!")
        break 
    if (numero_inserito > numero_segreto):
        print("Prova un po di meno")
        tent+=1
    if (numero_inserito<numero_segreto):
        print("prova un po di più")
        tent+=1
print("\nGIOCO TERMINATO in "+ str(tentativi)+" tentativi")